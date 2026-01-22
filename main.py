import time
import requests

TOKEN = "METTI_TOKEN"
CHAT_ID = "METTI_CHAT_ID"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

send_telegram("🚀 Bot LEGO online e funzionante!")

while True:
    time.sleep(60)
