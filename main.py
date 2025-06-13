import imaplib
import email
import json

CONFIG_PATH = "config/accounts.json"

def load_accounts():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def connect_to_gmail(account):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(account["email"], account["app_password"])
    mail.select("inbox")
    return mail

def fetch_unread_emails(mail):
    status, response = mail.search(None, '(UNSEEN)')
    email_ids = response[0].split()
    messages = []
    for e_id in email_ids:
        status, data = mail.fetch(e_id, "(RFC822)")
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = msg["subject"]
                from_ = msg["from"]
                messages.append({
                    "from": from_,
                    "subject": subject
                })
    return messages
