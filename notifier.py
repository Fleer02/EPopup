import os
import json
import platform
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import QTimer

# Bildirimde kullanılacak dil ayarını ve metinleri yükle
with open("config/settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)
language = settings.get("language", "tr")

with open("config/lang.json", "r", encoding="utf-8") as f:
    lang = json.load(f)
L = lang.get(language, lang["tr"])

# Bildirim işlevi
def show_notification(sender: str, subject: str):
    app = QApplication([])

    tray = QSystemTrayIcon()
    tray.setIcon(QIcon("assets/icon.png"))
    tray.setVisible(True)

    title = L["notification_title"]
    message = f"{L['from']}: {sender}\n{L['subject']}: {subject}"

    tray.showMessage(title, message, QSystemTrayIcon.Information, 10000)  # 10 saniye

    # Ses efekti çal
    if settings.get("play_sound", True):
        sound_path = os.path.abspath("assets/ding.wav")
        if os.path.exists(sound_path):
            QSound.play(sound_path)

    # Bildirim sonra kapat (görünmez uygulama)
    QTimer.singleShot(11000, app.quit)
    app.exec_()
