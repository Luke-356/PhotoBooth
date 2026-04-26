# 🧠 AI PhotoBooth – Remove People from Images

A Dockerized AI web application that detects and removes people from images using computer vision and diffusion models.

Built as a **DevOps-focused portfolio project** demonstrating containerization, cloud deployment, and scalable architecture.

---

## 🚀 Features

* 📸 Upload an image via web UI
* 🧍 Detect people using YOLOv8
* 🧠 Generate masks and remove people
* 🎨 Inpaint background using Stable Diffusion
* 🐳 Fully Dockerized (production-ready)
* ☁️ Deployable on AWS EC2

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **AI Models:**

  * YOLOv8 (object detection)
  * Stable Diffusion Inpainting (image generation)
* **Image Processing:** OpenCV, PIL
* **Containerization:** Docker & Docker Compose
* **Deployment:** AWS EC2

---

## 📂 Project Structure

```id="projstruct1"
PhotoBooth/
│
├── app/
│   ├── main.py              # FastAPI app
│   └── static/              # Frontend (HTML, JS, CSS)
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User uploads an image
2. YOLO detects people in the image
3. Masks are generated for detected regions
4. Stable Diffusion fills in the removed areas
5. Final image is returned without people

---

## 🐳 Run with Docker (Local)

### 1. Build and run

```bash id="dock1"
docker compose up --build
```

### 2. Open in browser

```
http://localhost:8000
```

---

## ☁️ Deploy on AWS EC2

### 1. SSH into instance

```bash id="ssh1"
ssh -i your-key.pem ubuntu@<EC2_IP>
```

### 2. Install Docker

```bash id="dock2"
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

### 3. Clone repo

```bash id="clone1"
git clone https://github.com/Luke-356/PhotoBooth.git
cd PhotoBooth
```

### 4. Run app

```bash id="run1"
docker compose up -d
```

### 5. Open in browser

```
http://<EC2_IP>:8000
```

---

## 🔐 Security Group Setup (IMPORTANT)

Allow inbound traffic:

| Type       | Port | Source    |
| ---------- | ---- | --------- |
| Custom TCP | 8000 | 0.0.0.0/0 |
| SSH        | 22   | Your IP   |

---

## ⚠️ Notes

* AI models are downloaded at runtime (not stored in repo)
* First request may take longer due to model loading
* CPU mode is supported, but GPU is recommended for performance

---

## 📈 DevOps Highlights

* Containerized ML application using Docker
* Cloud deployment on AWS EC2
* Clean repository (no large model files)
* Scalable architecture for production extension

---

## 🔗 Acknowledgements

This project uses:

* Meta AI’s Segment Anything model for image segmentation
* Ultralytics YOLOv8 for object detection
* Stable Diffusion for inpainting

Special thanks to the open-source community.

---

## 🔮 Future Improvements

* Add Nginx reverse proxy
* Enable HTTPS (Let’s Encrypt)
* Add CI/CD pipeline (GitHub Actions)
* Use S3 for model storage
* GPU acceleration support

---

## 👨‍💻 Author

**Nyi Nyi Lwin**
Master’s in Computer Science – Pace University
Aspiring DevOps Engineer

---

## ⭐ If you like this project

Give it a star on GitHub!
