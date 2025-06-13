# Gmail Keyword Notifier 📧🔔

This Python-based desktop application monitors your Gmail inbox for emails containing **important keywords**, and notifies you with a **popup alert** and a **ding sound**. It also includes a lightweight **PyQt5 GUI** and runs in the system tray.

## 🚀 Features

- ✅ Checks Gmail for incoming emails
- 🔍 Matches subject/body with custom keywords
- 🔕 Blocks emails with specified ignored words
- 🔔 Popup notification with **sound alert**
- 🪟 Simple GUI showing:
  - Matched emails (sender, subject, timestamp)
  - Configured keywords and blocked words
  - Activity logs
- 🧰 System tray icon with menu (hide/show/quit)
- 📝 Logs all triggered emails with timestamp

## 🗂️ Folder Structure

gmail-alert-tray/
├── main.py                 # Entry point of the application
├── gmail_reader.py         # Handles Gmail API connection and email fetching
├── notifier.py             # Handles popup notifications and sound alerts
├── gui.py                  # PyQt5-based interface to show logs and keywords
├── tray.py                 # System tray icon and menu control
├── requirements.txt        # List of Python dependencies
├── config/
│   ├── keywords.json       # Keywords to detect important emails
│   ├── blocked.json        # Words to filter out irrelevant emails
├── logs/
│   └── mail_log.txt        # Log file storing alerts (timestamp, sender, subject)
├── assets/
│   ├── ding.mp3            # Sound played for new email alerts
│   └── tray_icon.png       # Icon for the system tray
