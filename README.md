# 📸 PhotoBooth AI App (Docker + AWS EC2 Deployment)

An AI-powered PhotoBooth application built with **FastAPI**, computer vision models, and deployed using **Docker on AWS EC2**.  
This project demonstrates full-stack deployment, ML inference serving, and DevOps practices.

---

# 🚀 Live Demo

http://3.144.175.277:8000

<!-- Demo temporarily offline (AWS cost optimization) -->

---

# 🧠 Overview

This project is a containerized AI web application that:
- Accepts image input
- Detects people using YOLO models
- Applies optimized image processing (CPU-friendly pipeline)
- Serves results through a FastAPI backend
- Runs fully inside Docker on an AWS EC2 instance

---

# 🏗️ Architecture

Client (Browser)  
      ↓  
EC2 Instance (Ubuntu)  
      ↓  
Docker Compose  
      ↓  
FastAPI Backend (Uvicorn)  
      ↓  
AI Processing Pipeline (YOLO + OpenCV + PyTorch)

---

# ⚙️ Tech Stack

## Backend
- FastAPI
- Uvicorn

## AI / ML
- PyTorch
- OpenCV
- Ultralytics (YOLO)
- NumPy

## DevOps
- Docker
- Docker Compose
- AWS EC2 (Ubuntu)

---

# 🖥️ EC2 Deployment Details

- AWS EC2 Ubuntu Server  
- Instance type: m7i-flex.large  

Ports:
- 8000 → FastAPI app

---

# 📦 Setup Instructions

## 1. Clone repository
```bash
git clone https://github.com/Luke-356/PhotoBooth.git
cd PhotoBooth
```

---

## 2. Build and run
```bash
docker-compose up -d --build
```

---

## 3. Check containers
```bash
docker ps
```

---

## 4. Open app

Local:
http://localhost:8000

EC2:
http://your-ec2-public-ip:8000

---

# 🧾 Docker Commands

Start:
```bash
docker-compose up -d
```

Stop:
```bash
docker-compose down
```

Logs:
```bash
docker logs <container_id>
```

---

# ⚠️ Common Issues

## No space left
```bash
docker system prune -a
```

## Restart on reboot
Add in docker-compose.yml:
```yaml
restart: unless-stopped
```

## Port not accessible
- Check AWS Security Group
- Allow inbound traffic on port 8000

---

# 🔐 Security Notes

- This is a demo/portfolio deployment
- No authentication enabled
- Port 8000 is publicly exposed

---

# 📊 DevOps Highlights

- Dockerized AI application
- Cloud deployment on AWS EC2
- ML inference served via REST API
- Container-based deployment workflow
- Handles real-world performance constraints (CPU-only)

---

# ⚠️ Limitations

- Uses optimized (CPU-friendly) processing instead of full inpainting
- Processing time depends on image size
- Not production-hardened (demo project)

---

# 🚧 Future Improvements

- Add CI/CD pipeline (GitHub Actions)
- Add Nginx reverse proxy
- Enable GPU support (g4/g5 instances)
- Improve processing quality
- Add monitoring/logging

---

# 👨‍💻 Author

Nyi Nyi Lwin  
Master’s in Computer Science  
Pace University
