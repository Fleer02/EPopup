import imaplib
import email
from email.header import decode_header
import time
import json
from filter import is_important_email
from notifier import show_notification
from logger import log_email

# Ayarları ve hesap bilgilerini yükle
with open("config/settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)
with open("config/accounts.json", "r", encoding="utf-8") as f:
    accounts = json.load(f)

EMAIL = accounts["email"]
PASSWORD = accounts["password"]
IMAP_SERVER = settings.get("gmail_imap_server", "imap.gmail.com")
IMAP_PORT = settings.get("imap_port", 993)
CHECK_INTERVAL = settings.get("check_interval_seconds", 60)

# E-postaları oku ve işle
def check_email():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        # Sadece son 10 e-postayı kontrol et
        result, data = mail.search(None, "UNSEEN")
        email_ids = data[0].split()[-10:]

        for email_id in email_ids:
            result, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8", errors="ignore")
                    from_ = msg.get("From")
                    date_ = msg.get("Date")

                    # Önemli e-posta tespiti
                    if is_important_email(subject):
                        if settings.get("show_popup", True):
                            show_notification(from_, subject)
                        if settings.get("log_emails", True):
                            log_email(from_, subject, date_)
        mail.logout()
    except Exception as e:
        print(f"[ERROR] E-posta kontrolünde hata: {e}")

# Sürekli çalışacak döngü
if __name__ == "__main__":
    print("E-posta dinleyici başlatıldı.")
    while True:
        check_email()
        time.sleep(CHECK_INTERVAL)
