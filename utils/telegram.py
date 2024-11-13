import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "7611987840:AAF2UYDYT7tNXjYdYFDGYIkOHG0ZpI52Wg4")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "-1002367381381")

def send_error_to_telegram(error_message: str, topic: int = None):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": error_message,
        "parse_mode": "HTML",
        # "message_thread_id": topic
    }
    response = requests.post(url, data=payload)
    return response.status_code, response.json()

