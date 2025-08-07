# 🔫 Weapon Detection System using Deep Learning & YOLOv8

![Weapon Detection Banner](https://img.shields.io/badge/Weapon%20Detection-YOLOv8-brightgreen?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Python-3.8-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Real%20Time%20Detection-red?style=for-the-badge&logo=opencv)
![License](https://img.shields.io/github/license/dhivyadharshini15102005/Weapon_Detection?style=for-the-badge)

> 🚨 Real-time surveillance solution to detect weapons using computer vision and deep learning. Built with YOLOv8 and OpenCV to enhance public safety through smart monitoring.

---

## 📸 Demo

https://github.com/dhivyadharshini15102005/Weapon_Detection/assets/demo_weapon_detection.mp4 *(Add your actual demo video or GIF link here)*

---

## 🧠 Overview

This project is designed to detect **weapons (guns, knives, etc.)** in real-time using a webcam or surveillance feed. It helps in enhancing public safety in high-risk areas like:

- Airports ✈️  
- Schools 🏫  
- Banks 🏦  
- Malls 🏬  
- Events & Concerts 🎤

Using **YOLOv8** from the Ultralytics library, it processes video streams with high-speed and accuracy, triggering alerts when weapons are detected.

---

## 🛠️ Technologies Used

| Tool/Tech         | Description                            |
|-------------------|----------------------------------------|
| 🐍 Python 3.8+     | Core programming language              |
| 🧠 YOLOv8 (Ultralytics) | State-of-the-art object detection |
| 🎥 OpenCV          | Real-time image & video processing     |
| 📁 LabelImg        | Annotation tool (for training data)    |
| 🖼️ Custom Dataset | Weapon images/videos (sourced & trained) |

---

## 🚀 Features

✅ Real-time Weapon Detection  
✅ High accuracy with YOLOv8  
✅ Easy to use with webcam or CCTV input  
✅ Modular codebase  
✅ Alarm trigger integration possible  
✅ Visual bounding boxes on detected weapons

---

## 📂 Project Structure

```bash
Weapon_Detection/
├── yolov8n.pt                  # Pretrained YOLOv8 model (or fine-tuned)
├── detect.py                   # Main detection script
├── data/
│   └── test_video.mp4          # Input test video file
├── requirements.txt            # Required Python packages
├── README.md                   # Project documentation
└── outputs/                    # Saved output video/images


