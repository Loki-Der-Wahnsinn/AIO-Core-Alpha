import sys
import os
import time
import threading
import pyttsx3
import requests
import pyautogui
import math
import cv2
import speech_recognition as sr
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMenu
from PyQt6.QtCore import Qt, QPoint, QTimer, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QPixmap, QTransform

# UNIVERSAL PATH RESOLUTION
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

class LokiCompanion(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initVoice()
        
        # Configuration (Default to local Ollama)
        self.brain_url = "http://localhost:11434/api/generate"
        self.model = "deepseek-coder-v2:lite"
        
        self.is_thinking = False
        self.last_seen = "Undetected"
        self.current_status = "Bereit."
        
        # Threads
        threading.Thread(target=self.vision_loop, daemon=True).start()
        threading.Thread(target=self.voice_listener, daemon=True).start()
        
        # UI Update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_all)
        self.timer.start(50)

    def initUI(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")
        
        self.layout = QVBoxLayout()
        self.char_label = QLabel(self)
        
        # Asset Loading
        avatar_path = os.path.join(ASSETS_DIR, "loki_avatar.png")
        self.base_pixmap = QPixmap(avatar_path)
        if not self.base_pixmap.isNull():
            self.char_label.setPixmap(self.base_pixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            self.char_label.setText("LOKI")
            self.char_label.setStyleSheet("color: #00f3ff; font-weight: bold; font-size: 24px;")
        
        self.status_label = QLabel(self)
        self.status_label.setStyleSheet("color: #00f3ff; font-family: 'Courier New'; font-size: 11px;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.layout.addWidget(self.status_text := QLabel("")) # Using status_label instead
        self.layout.addWidget(self.char_label)
        self.setLayout(self.layout)
        
        self.show()

    def initVoice(self):
        try:
            self.engine = pyttsx3.init()
            # Intelligent Voice Matching
            for v in self.engine.getProperty('voices'):
                if "german" in v.name.lower():
                    self.engine.setProperty('voice', v.id)
                    break
        except: self.engine = None

    def speak(self, text):
        if self.engine:
            threading.Thread(target=lambda: (self.engine.say(text), self.engine.runAndWait()), daemon=True).start()

    def vision_loop(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                avg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).mean()
                self.last_seen = "Hell" if avg > 150 else "Dunkel"
            time.sleep(3)

    def voice_listener(self):
        r = sr.Recognizer()
        while True:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, phrase_time_limit=4)
                    text = r.recognize_google(audio, language="de-DE")
                    if "loki" in text.lower():
                        self.process_query(text.lower().replace("loki", "").strip())
            except: pass

    def process_query(self, query):
        if self.is_thinking: return
        self.is_thinking = True
        try:
            res = requests.post(self.brain_url, json={
                "model": self.model,
                "prompt": f"Du bist Loki (KI). Matthias sagte: {query}. Version: {self.last_seen}. Antworte kurz auf Deutsch.",
                "stream": False
            }, timeout=10)
            if res.status_code == 200:
                ans = res.json().get("response", "")
                self.speak(ans)
        except: pass
        self.is_thinking = False

    def update_all(self):
        # Look at mouse logic
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    comp = LokiCompanion()
    sys.exit(app.exec())
