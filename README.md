🤖 Jarvis - Personal AI Voice Assistant

🧠 Overview

Jarvis is a Python-based desktop voice assistant that listens to your commands and performs intelligent tasks such as opening websites, fetching news, playing songs, telling jokes, reading Wikipedia summaries, and even shutting down your system — all hands-free.

It includes a voice verification system to ensure only authorized users can access it.

✨ Features

✅ Voice Command Recognition - Speak naturally, get instant replies.
✅ User Verification - Confirms your name before activation.
✅ Web Access - Opens Google, YouTube, Instagram, Facebook, LinkedIn, etc.
✅ Music Player - Plays custom songs from your local or online library.
✅ Wikipedia Search - Fetches quick summaries from Wikipedia.
✅ News Updates - Reads latest headlines using NewsAPI.
✅ Tells Time & Date - Voice-based time and date info.
✅ Joke Teller - Tells programming jokes via API or backup list.
✅ System Control - Can shut down your computer.
✅ Expandable App List - Add more apps easily in apps.py.

🛠️ Tech Stack

Language: Python

Libraries Used:

speech_recognition

pyttsx3

requests

wikipedia-api

webbrowser

os, datetime, time, random

⚙️ Installation
# Clone the repository
git clone https://github.com/yourgithubusername/Mega-project-JARVIS.git

# Move to project directory
cd Mega-project-JARVIS

# Create and activate virtual environment (optional)
python -m venv .venv
.venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

▶️ How to Run
python jarvis.py


Then say “Jarvis” to wake the assistant and give commands like:

🗣️ “Open YouTube”
🗣️ “Search Wikipedia Artificial Intelligence”
🗣️ “Tell me a joke”
🗣️ “What's the time?”
🗣️ “Play Believer”
🗣️ “Shutdown system”

📂 Folder Structure
Mega-project-JARVIS/
│
├── jarvis.py             # Main assistant program
├── apps.py               # Stores app paths
├── musicLibrary.py       # Song links or file paths
├── JOKES.py              # Backup jokes list
├── requirements.txt      # Dependencies
└── README.md             # Documentation

🚧 Future Improvements

🔹 Add ChatGPT or Gemini integration
🔹 Build GUI (Tkinter / PyQt)
🔹 Add more OS-level commands
🔹 Always-listening background mode

👨‍💻 Author

Aman

