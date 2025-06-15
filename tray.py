import sys
import json
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
import subprocess

# Ayar ve dil dosyalarını yükle
def load_lang():
    with open("config/settings.json", "r", encoding="utf-8") as f:
        settings = json.load(f)
    language = settings.get("language", "tr")

    with open("config/lang.json", "r", encoding="utf-8") as f:
        lang = json.load(f)
    return lang.get(language, lang["tr"]), language

# Tray ikonunu başlat
def start_tray():
    app = QApplication(sys.argv)
    tray = QSystemTrayIcon()
    tray.setIcon(QIcon("assets/tray_icon.png"))
    tray.setVisible(True)

    L, current_language = load_lang()

    # Menü oluştur
    menu = QMenu()

    # --- Dil Seçimi ---
    lang_menu = QMenu(L["language"], menu)

    def switch_language(lang_code):
        with open("config/settings.json", "r+", encoding="utf-8") as f:
            data = json.load(f)
            data["language"] = lang_code
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
        QMessageBox.information(None, "Info", "Please restart the app to apply language changes.")

    action_tr = QAction("🇹🇷 Türkçe", menu)
    action_tr.triggered.connect(lambda: switch_language("tr"))
    lang_menu.addAction(action_tr)

    action_en = QAction("🇬🇧 English", menu)
    action_en.triggered.connect(lambda: switch_language("en"))
    lang_menu.addAction(action_en)

    menu.addMenu(lang_menu)

    # --- GUI'yi Aç (şimdilik uyarı veriyoruz) ---
    def open_gui():
        try:
            subprocess.Popen(["python", "gui.py"])
        except Exception as e:
            QMessageBox.critical(None, "Error", f"GUI could not be launched: {e}")

    open_gui_action = QAction(L["open_gui"], menu)
    open_gui_action.triggered.connect(open_gui)
    menu.addAction(open_gui_action)

    # --- Çıkış ---
    quit_action = QAction(L["quit"], menu)
    quit_action.triggered.connect(QCoreApplication.quit)
    menu.addAction(quit_action)

    tray.setContextMenu(menu)
    sys.exit(app.exec_())
