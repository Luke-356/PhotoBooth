import os
import logging
import time
import asyncio
from io import BytesIO
from pathlib import Path
from typing import Optional

import cv2
import numpy as np
import torch
from diffusers import StableDiffusionInpaintPipeline
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
from ultralytics import YOLO

# ----------------------------
# Paths (WORKS LOCAL + DOCKER)
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
MODELS_DIR = Path(os.getenv("MODEL_DIR", BASE_DIR / "models"))

STATIC_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

os.environ["HF_HOME"] = str(MODELS_DIR)
os.environ["YOLO_CONFIG_DIR"] = str(MODELS_DIR)

# ----------------------------
# App
# ----------------------------
app = FastAPI()
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("photo-booth")

# ----------------------------
# Models
# ----------------------------
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

detector: Optional[YOLO] = None
pipe: Optional[StableDiffusionInpaintPipeline] = None

# ----------------------------
# Prompts
# ----------------------------
STYLE_PROMPTS = {
    "natural": (
        "high quality realistic background, cinematic lighting",
        "low quality, blurry, person, people, face, artifacts",
    ),
    "studio": (
        "clean studio background, soft lighting",
        "low quality, blurry, people, face",
    ),
}

# ----------------------------
# Routes
# ----------------------------
@app.get("/")
def root():
    index_file = STATIC_DIR / "index.html"
    if not index_file.exists():
        return {"message": "UI not found. Place index.html in /app/static"}
    return FileResponse(index_file)


@app.get("/health")
def health():
    return {"status": "ok", "device": DEVICE}


# ----------------------------
# Startup
# ----------------------------
@app.on_event("startup")
def startup():
    global detector, pipe

    logger.info(f"Loading models on {DEVICE}")

    detector = YOLO("yolov8n.pt")

    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        "runwayml/stable-diffusion-inpainting",
        cache_dir=str(MODELS_DIR),
        torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32,
    ).to(DEVICE)

    pipe.safety_checker = lambda images, **kwargs: (images, [False] * len(images))
    pipe.enable_attention_slicing()

    logger.info("Models loaded successfully")


# ----------------------------
# Helpers
# ----------------------------
def resize_if_needed(img, max_size=1024):
    h, w = img.shape[:2]
    if max(h, w) > max_size:
        scale = max_size / max(h, w)
        return cv2.resize(img, (int(w * scale), int(h * scale)))
    return img


def create_mask(image, boxes):
    h, w = image.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)

    for (x1, y1, x2, y2) in boxes:
        pad = int(0.05 * max(w, h))
        x1 = max(0, x1 - pad)
        y1 = max(0, y1 - pad)
        x2 = min(w, x2 + pad)
        y2 = min(h, y2 + pad)
        mask[y1:y2, x1:x2] = 255

    return cv2.GaussianBlur(mask, (21, 21), 0)


def process_image(image_bgr, prompt, negative):
    image_bgr = resize_if_needed(image_bgr)

    h, w = image_bgr.shape[:2]
    rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb)

    results = detector(image_bgr, conf=0.4)

    boxes = []
    for r in results:
        for b in r.boxes:
            if int(b.cls[0]) == 0:
                boxes.append(tuple(map(int, b.xyxy[0].cpu().numpy())))

    if not boxes:
        return image_bgr

    mask = create_mask(image_bgr, boxes)
    pil_mask = Image.fromarray(mask).convert("L")

    scale = 0.75
    small_img = pil_img.resize((int(w * scale), int(h * scale)))
    small_mask = pil_mask.resize((int(w * scale), int(h * scale)))

    with torch.no_grad():
        out = pipe(
            prompt=prompt,
            negative_prompt=negative,
            image=small_img,
            mask_image=small_mask,
            num_inference_steps=25,
            guidance_scale=7.5,
            strength=0.95,
        ).images[0]

    out = out.resize((w, h))
    return cv2.cvtColor(np.array(out), cv2.COLOR_RGB2BGR)


# ----------------------------
# API
# ----------------------------
@app.post("/remove-people/")
async def remove_people(file: UploadFile = File(...), style: str = Form("natural")):
    contents = await file.read()

    image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        raise HTTPException(400, "Invalid image")

    prompt, negative = STYLE_PROMPTS.get(style, STYLE_PROMPTS["natural"])

    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, process_image, image, prompt, negative)

    _, encoded = cv2.imencode(".jpg", result, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

    return StreamingResponse(BytesIO(encoded.tobytes()), media_type="image/jpeg")