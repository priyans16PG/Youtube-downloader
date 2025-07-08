📄 Project Description: YouTube Downloader Web App (Flask + yt-dlp)

This is a lightweight web application built using Flask that lets you download YouTube videos in various resolutions (240p, 480p, or 1080p) using yt-dlp. The app runs in a browser, and the user can input a URL and select the quality—then the backend handles the downloading.

This is ideal for use on Android with Termux, internal servers, or even local LAN devices to easily fetch and store YouTube videos to a custom folder like SD card storage.


---

✅ Features

🎥 Download YouTube videos directly from a simple web interface

🎚 Choose video quality: 240p, 480p, or 1080p

🧠 Uses yt-dlp under the hood for powerful download options

📂 Saves downloaded videos to a predefined folder

⚡ Live status with auto-redirect after starting a download

💡 Clean, mobile-friendly UI



---

📦 Dependencies

Install the required Python packages:

pip install flask

Also make sure you have yt-dlp installed:

pip install -U yt-dlp

You should also have FFmpeg installed for merging audio and video:

pkg install ffmpeg  # for Termux


---

📁 Folder Structure

your_project/
│
├── main.py               # Your Flask app (provided below)
├── README.md             # This file
└── /storage/.../Movies/yt  # Output folder (SD card or internal)


---

🚀 How to Run

On Android via Termux:

1. Save the script as main.py


2. Run:



python main.py

3. Open a browser and go to:



http://localhost:8080

You can also use your phone’s IP address to access the app from other devices on the same network.
