import os
from datetime import datetime

# Log klasörü varsa dokunma, yoksa oluştur
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

def log_email(sender: str, subject: str, date: str):
    log_file = os.path.join(log_dir, "important_emails.log")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Gönderen: {sender} | Konu: {subject} | Tarih: {date}\n")
