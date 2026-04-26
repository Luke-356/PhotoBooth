# PhotoBooth Docker Setup

## Project Structure

```
PhotoBooth/
├── main.py                 # FastAPI backend
├── Dockerfile             # Docker build instructions
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
├── .dockerignore          # Files to exclude from Docker build
├── static/                # Frontend files (HTML/CSS/JS)
├── outputs/               # Generated images (mounted volume)
├── segment-anything/      # SAM model code
├── pythonenv/             # Local venv (not in Docker)
├── yolov8m.pt            # YOLO model weights
├── yolov8n.pt            # YOLO model weights
└── sam_vit_b_01ec64.pth  # SAM model weights
```

## How to Build and Run with Docker

### 1. Build the Docker Image
```bash
docker build -t photobooth:latest .
```

### 2. Run with Docker Compose (Recommended)
```bash
docker-compose up
```

This will:
- Build the image
- Start the container
- Mount `outputs/` and `static/` as volumes
- Expose port 8000

### 3. Access the Application
Open: `http://localhost:8000`

### 4. Stop the Container
```bash
docker-compose down
```

## Docker Files Explained

### **Dockerfile**
- **FROM python:3.9-slim** - Lightweight Python base image
- **System dependencies** - OpenCV requires system libs (libsm6, libxext6, etc.)
- **requirements.txt** - Installs all Python packages
- **SAM download** - Fetches the 357MB model during build
- **EXPOSE 8000** - Exposes the API port
- **CMD** - Starts uvicorn server accessible from outside the container (0.0.0.0)

### **requirements.txt**
Lists all Python dependencies with pinned versions for reproducibility

### **docker-compose.yml**
- **build**: Builds from Dockerfile
- **ports**: Maps container port 8000 to host port 8000
- **volumes**: Mounts local directories so you can access outputs and modify frontend
- **environment**: Sets Python to unbuffered output (real-time logs)
- **restart**: Restarts container if it crashes

### **.dockerignore**
Excludes unnecessary files from the Docker build context (speeds up build):
- `__pycache__/`, `.venv/`, etc.
- Large output files
- IDE config files

## Production Improvements

For production, consider:

1. **Multi-stage build** - Reduce image size by separating build and runtime stages
2. **nginx reverse proxy** - Add load balancing and static file serving
3. **GPU support** - Use `docker run --gpus all` for NVIDIA GPU acceleration
4. **.env file** - Store sensitive config (API keys, etc.)
5. **Health checks** - Monitor container health

Would you like me to create a production-ready multi-stage Dockerfile or a nginx config?
