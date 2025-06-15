import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QTabWidget
)
from PyQt5.QtGui import QFont, QIcon

def load_settings():
    with open("config/settings.json", "r", encoding="utf-8") as f:
        settings = json.load(f)
    with open("config/lang.json", "r", encoding="utf-8") as f:
        lang = json.load(f)
    return settings, lang[settings.get("language", "tr")]

class InfoGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.settings, self.L = load_settings()
        self.setWindowTitle("EPopup - " + self.L["app_running"])
        self.setWindowIcon(QIcon("assets/tray_icon.png"))
        self.resize(600, 500)

        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        # Sekmeler
        self.tabs.addTab(self.create_tab("config/keywords.json"), self.L["keywords"])
        self.tabs.addTab(self.create_tab("config/blocked.json"), self.L["blocked"])
        self.tabs.addTab(self.create_tab("logs/logs.txt"), self.L["logs"])
        self.tabs.addTab(self.create_info_tab(), self.L["info"])

        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def create_tab(self, file_path):
        tab = QWidget()
        layout = QVBoxLayout()

        text_edit = QTextEdit()
        text_edit.setFont(QFont("Consolas", 10))
        text_edit.setReadOnly(True)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            content = self.L["error_reading"]

        text_edit.setText(content)
        layout.addWidget(text_edit)
        tab.setLayout(layout)
        return tab

    def create_info_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        label = QLabel()
        label.setText(
            f"<b>{self.L['status']}</b><br>"
            f"{self.L['language']}: <i>{self.settings['language']}</i><br><br>"
            f"© 2025 GitHub Project - Security Email Popup Notifier"
        )
        label.setFont(QFont("Arial", 11))
        layout.addWidget(label)

        tab.setLayout(layout)
        return tab

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InfoGUI()
    window.show()
    sys.exit(app.exec_())
