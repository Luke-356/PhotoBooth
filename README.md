# 📸 PhotoBooth AI App (Docker + AWS EC2 Deployment)

An AI-powered PhotoBooth application built with **FastAPI**, computer vision models, and deployed using **Docker on AWS EC2**.  
This project demonstrates full-stack deployment, ML inference serving, and DevOps practices.

---

# 🚀 Live Demo

[http://<YOUR-EC2-PUBLIC-IP>:8000](http://3.144.175.227:8000)


<!--Demo temporarily offline (AWS cost optimization)-->

---

# 🧠 Overview

This project is a containerized AI web application that:
- Accepts image input
- Processes images using computer vision / ML models
- Serves results through a FastAPI backend
- Runs fully inside Docker on an AWS EC2 instance

---

# 🏗️ Architecture

Client (Browser)
      |
      v
EC2 Instance (Ubuntu)
      |
      v
Docker Compose
      |
      v
FastAPI Backend (Uvicorn)
      |
      v
AI Models (Torch / Diffusers / OpenCV / Ultralytics)

---

# ⚙️ Tech Stack

## Backend
- FastAPI
- Uvicorn

## AI / ML
- PyTorch
- Diffusers
- OpenCV
- Ultralytics (YOLO models)
- NumPy

## DevOps
- Docker
- Docker Compose
- AWS EC2 (Ubuntu)

---

# 🖥️ EC2 Deployment Details

- AWS EC2 Ubuntu Server
- Instance type: m7i-flex.large (or your selected type)

Ports:
- 8000 → FastAPI app

---

# 📦 Setup Instructions

## 1. Clone repository
git clone https://github.com/Luke-356/photobooth.git
cd photobooth

---

## 2. Build and run
docker-compose up -d --build

---

## 3. Check containers
docker ps

---

## 4. Open app

Local:
http://localhost:8000

EC2:
http://<EC2-PUBLIC-IP>:8000

---

# 🧾 Docker Commands

Start:
docker-compose up -d

Stop:
docker-compose down

Logs:
docker logs <container_id>

---

# ⚠️ Common Issues

## No space left
docker system prune -a

## Restart on reboot
restart: unless-stopped (in docker-compose.yml)

## Port not accessible
Check AWS Security Group (allow 8000)

---

# 🔐 Security Notes

- This is a demo/portfolio deployment
- No authentication enabled
- Port 8000 is publicly exposed

---

# 📊 DevOps Highlights

- Dockerized AI application
- Cloud deployment on AWS EC2
- ML inference serving via API
- Production-style container setup
- Basic infrastructure troubleshooting

---

# 👨‍💻 Author

Nyi Nyi Lwin  
Master’s in Computer Science  
Pace University
