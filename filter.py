import json
import os

# Anahtar ve engellenmiş kelimeleri yükleyen yardımcı fonksiyon
def load_keywords():
    with open("config/keywords.json", "r", encoding="utf-8") as f:
        keywords = [k.lower() for k in json.load(f)]
    with open("config/blocked_words.json", "r", encoding="utf-8") as f:
        blocked_words = [b.lower() for b in json.load(f)]
    return keywords, blocked_words

# E-posta konusu analiz edilir
def is_important_email(subject: str) -> bool:
    if not subject:
        return False

    subject = subject.lower()
    keywords, blocked_words = load_keywords()

    # Engellenmiş kelime geçiyorsa önemli değildir
    if any(blocked in subject for blocked in blocked_words):
        return False

    # Anahtar kelime geçiyorsa önemli sayılır
    if any(keyword in subject for keyword in keywords):
        return True

    return False
