# 📸 PhotoBooth AI Platform (Full-Stack + Cloud Deployment)

An AI-powered full-stack web application built with **FastAPI**, modern frontend technologies, computer vision pipelines, and deployed using **Docker on AWS EC2**.

This project demonstrates:
- Full-stack application development
- REST API architecture
- AI/ML integration
- Cloud deployment workflows
- Containerized infrastructure
- Real-world deployment and optimization practices

---

# 🚀 Live Demo

http://3.134.80.193:8000
(Currently paused for AWS budget purposes) 
<!--*Currently suspended for AWS budget optimization. Deployment will be restored soon.*-->

---

# 🧠 Project Overview

PhotoBooth is a full-stack AI image processing application that allows users to upload images through a web interface and automatically process them using computer vision models.

The platform:
- Accepts image uploads from users
- Detects people using YOLO-based computer vision models
- Processes images through an optimized AI pipeline
- Returns transformed images through a responsive frontend experience
- Runs inside Docker containers deployed on AWS EC2

The project focuses on combining:
- frontend user experience
- backend API engineering
- AI inference pipelines
- cloud deployment infrastructure

into a complete production-style application workflow.

---

# 🏗️ Full-Stack Architecture

Frontend (HTML/CSS/JavaScript)  
↓  
FastAPI REST API Backend  
↓  
AI Processing Pipeline (YOLO + OpenCV + PyTorch)  
↓  
Docker Containerization  
↓  
AWS EC2 Cloud Infrastructure

---

# ⚙️ Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript
- Responsive UI Design

## Backend
- FastAPI
- Uvicorn
- REST API Architecture

## AI / Machine Learning
- PyTorch
- OpenCV
- Ultralytics YOLO
- NumPy

## DevOps & Cloud
- Docker
- Docker Compose
- AWS EC2 (Ubuntu)
- Linux Server Management

---

# 🌐 Key Features

- AI-powered image processing
- RESTful API backend
- Responsive frontend interface
- Real-time image upload workflows
- Dockerized deployment pipeline
- Cloud-hosted infrastructure
- CPU-optimized inference pipeline
- End-to-end full-stack integration

---

# 🖥️ Cloud Deployment

The application was deployed on:
- AWS EC2 Ubuntu Server
- Dockerized container environment
- Publicly accessible REST API architecture

### Infrastructure Details
- Instance Type: m7i-flex.large
- FastAPI application exposed on Port 8000
- Containerized deployment using Docker Compose

---

# 📦 Local Development Setup

## 1. Clone Repository

```bash
git clone https://github.com/Luke-356/PhotoBooth.git
cd PhotoBooth
```

---

## 2. Build & Run Containers

```bash
docker-compose up -d --build
```

---

## 3. Verify Running Containers

```bash
docker ps
```

---

## 4. Access Application

Local:
```bash
http://localhost:8000
```

Cloud:
```bash
http://your-ec2-public-ip:8000
```

---

# 🧾 Docker Workflow

### Start Containers
```bash
docker-compose up -d
```

### Stop Containers
```bash
docker-compose down
```

### View Logs
```bash
docker logs <container_id>
```

---

# 🔐 Security & Infrastructure Notes

- Portfolio/demo deployment
- Public API exposure on port 8000
- Dockerized isolated runtime environment
- AWS Security Group configuration required for inbound traffic

---

# 📊 Engineering & Full-Stack Highlights

- Designed and deployed a complete full-stack AI platform
- Developed scalable FastAPI backend services
- Integrated frontend upload workflows with backend AI processing
- Containerized the entire application using Docker
- Deployed and managed cloud infrastructure on AWS EC2
- Optimized AI inference workflows for CPU-only environments
- Implemented end-to-end REST API communication
- Managed Linux server deployment and runtime operations

---

# ⚠️ Current Limitations

- Optimized for CPU-based inference instead of GPU acceleration
- Processing speed depends on image resolution
- Authentication and production hardening not yet implemented

---

# 🚧 Future Improvements

- React/Next.js frontend migration
- CI/CD pipeline using GitHub Actions
- Nginx reverse proxy configuration
- HTTPS domain setup
- GPU-enabled cloud inference
- Monitoring and logging dashboards
- User authentication and storage system
- Database integration for image history

---

# 👨‍💻 Author

Nyi Nyi Lwin  
M.S. Computer Science Candidate  
Pace University

Portfolio: https://nyinyilwin.com  
GitHub: https://github.com/Luke-356
