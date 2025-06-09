
# ✋ Hand Gesture Controlled Hill Climb Racing 🚗

Bring touchless control to your favorite game!  
This project lets you control the **Hill Climb Racing** game using **hand gestures** through your webcam — no keyboard needed! Built with real-time computer vision using **OpenCV** and **MediaPipe**, and keyboard automation using **Pynput**.

---

## 🎬 Demo Preview

<img src="hand_landmarks.png" width="600" alt="Gesture Demo"/>

> ✋ **Open Hand = GAS** (Right Arrow Key)  
> ✊ **Closed Fist = BRAKE** (Left Arrow Key)  
> ✅ Works with **either hand**, palm **or** back side!
---
![image alt](https://github.com/ShivakotiShambhavi/Hill-Climb/blob/3cb317eb7d654073bd26ffbbe581d735c473aae2/images/Screenshot%202025-06-09%20142024.png)
![image alt](https://github.com/ShivakotiShambhavi/Hill-Climb/blob/3cb317eb7d654073bd26ffbbe581d735c473aae2/images/Screenshot%202025-06-09%20142047.png)
---

## ✨ Features

- 🖐️ Real-time hand tracking with gesture detection
- 🧠 Smart recognition (ignores thumb for robustness)
- 🧭 Supports both left and right hands
- 🎮 Control vehicle in Hill Climb Racing using natural gestures
- 🪟 Auto-popup OpenCV window to stay on top during play
- 🔄 Cross-platform Python-based implementation

---

## 🛠️ Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| 🧠 MediaPipe | Real-time hand tracking          |
| 📷 OpenCV    | Video capture and frame handling |
| ⌨️ Pynput     | Keyboard automation (GAS/BRAKE)  |
| 🐍 Python 3  | Core programming language         |

---

## 📦 Installation

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/your-username/gesture-hill-climb.git
cd gesture-hill-climb
```

### 2️⃣ Install dependencies:
```bash
pip install opencv-python mediapipe pynput
```

### 3️⃣ Run the script:
```bash
python main.py
```

---

## 🕹️ Gameplay Instructions

- **Start Hill Climb Racing** on your PC ([Get it here](https://www.microsoft.com/en-us/p/hill-climb-racing/9wzdncrdcwk8))
- **Ensure your webcam is working**
- **Use hand gestures:**
  - ✋ Open hand = accelerate (`→`)
  - ✊ Closed fist = brake (`←`)
- **Press `q` to quit** the gesture controller

---

## 📁 Folder Structure

```
gesture-hill-climb/
├── main.py               # Core gesture detection and control logic
├── hand_landmarks.png    # Reference image used in README/demo
├── README.md             # This file
└── .gitignore            # Ignore Python artifacts
```

---

## 🧠 How It Works

- Detects 21 key hand landmarks using **MediaPipe**
- Analyzes fingertip positions to determine open/closed hand state
- If any hand is open (4 fingers up): ➡️ press Right Arrow (`GAS`)
- If any hand is closed (all fingers down): ⬅️ press Left Arrow (`BRAKE`)
- Uses OpenCV to show a live feed and annotate gestures

---

## ✅ Requirements

- Python 3.6+
- A working webcam
- Hill Climb Racing installed (Windows version recommended)

---
## ⚖️ License

This project is licensed under the [MIT License](LICENSE).

---

> 📌 Tip: Want to extend it? Add more gestures for turning, horn, or nitro boosts!
