import json
import os

# Anahtar ve engellenmiş kelimeleri yükleyen yardımcı fonksiyon
def load_keywords():
    with open("config/keywords.json", "r", encoding="utf-8") as f:
        keywords = [k.lower() for k in json.load(f)]
    # blocked words file may be empty
    blocked_file = "config/blocked.json"
    if os.path.exists(blocked_file):
        with open(blocked_file, "r", encoding="utf-8") as f:
            try:
                blocked_words = [b.lower() for b in json.load(f)]
            except json.JSONDecodeError:
                blocked_words = []
    else:
        blocked_words = []
    return keywords, blocked_words

# E-posta başlık veya gövdesinde anahtar kelime aranır
def is_important_email(subject: str, body: str) -> bool:
    text = (subject or "") + "\n" + (body or "")
    text = text.lower()
    keywords, blocked_words = load_keywords()

    if any(blocked in text for blocked in blocked_words):
        return False

    return any(keyword in text for keyword in keywords)
