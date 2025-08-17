# 🚦 AI-Based Intelligent Traffic Management System

## 📌 Overview

This project was developed as part of the **Smart India Hackathon (SIH)** with the vision to solve real-world urban mobility challenges.  
It leverages **Computer Vision (YOLO)** and **Python** to intelligently manage traffic by **detecting priority vehicles (e.g., ambulances, police cars, fire trucks)** and dynamically controlling traffic signals.

💡 **Key Innovation**:  
We introduce a **“White Light” Traffic Signal Concept** – when a priority vehicle is detected, all other vehicles are signaled to stop while the white light allows the emergency vehicle to pass smoothly.

---

## 🚀 Features

- ✅ **Real-Time Vehicle Detection** using YOLO object detection.
- 🚑 **Priority Vehicle Recognition** (ambulances, police cars, etc.).
- ⚡ **Dynamic Traffic Light Control** to optimize traffic flow.
- 🔦 **White Light Signal Concept** – a novel solution for emergency response.
- 🎥 **Live Camera Feed Integration** with external devices (CCTV / USB cameras).
- 🛠️ **Fully Python-Based Implementation** – no extra backend/frontend needed.

---

## 🏗️ Project Structure

```
📂 AI-Traffic-Management
├── 📂 Test_Resource/          # Sample traffic video footage
├── 📂 traffic/              # Traffic signal control scripts
│   ├── edit1_vehicle.py
│   ├── led_on.py
│   ├── newtrafic.py
│   └── traffic.py
├── 📂 Yolo/                 # YOLO detection & model scripts
│   ├── cam.py
│   ├── cam_class.py
│   ├── traffic_main.py
│   ├── trafic2.py
│   └── timer.py
├── .gitignore
└── README.md
```

---

## ⚙️ Tech Stack

- **Programming Language**: Python
- **Deep Learning Model**: YOLO (You Only Look Once)
- **Libraries**:
  - `opencv-python` (image/video processing)
  - `numpy`
  - `torch / ultralytics-yolo`
- **Hardware**: External camera device / CCTV integration

---

## 🔧 Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/vishalsoni2005/AI-Traffic-Management.git
   cd AI-Traffic-Management
   ```

2. **Run Detection Script**
   ```bash
   python traffic/traffic.py
   # OR
   python Yolo/traffic_main.py
   ```

---

## 🎥 Demonstration

- Priority vehicle detected in video → system switches signal to **White Light**.
- All non-priority vehicles are stopped automatically.
- Emergency vehicle passes **without delay**.

---

## 📈 Impact

- ⏱️ **Faster emergency response times**.
- 🚗 **Reduced congestion for priority vehicles**.
- 🧠 **Scalable system** – can be deployed at smart intersections.
- 🌍 **Real-World Application** for smart cities & intelligent transport systems.

---

## 📂 Future Enhancements

- 🔄 Integration with **IoT-enabled smart traffic lights**.
- 🌐 Deployment on **edge devices (Raspberry Pi, Jetson Nano)**.
- 🛰️ Integration with **GPS & live traffic APIs** for route optimization.
- 🤖 Expansion to handle **pedestrian & cycle detection**.

---

## 👥 Contributors

- **Vishal Soni**
- **Shivam Chopade**
- **Khusagrah**
- **Avishkar**

---

## 🏆 Recognition

Developed as part of **Smart India Hackathon (SIH)** to showcase AI’s role in transforming urban traffic systems.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and improve it.

---
