import time
import requests

TOKEN = "7788467209:AAFg-h8YbMGNdgrD5u0ynLih5_ZQFWUDgxI"
CHAT_ID = "737397778"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

send_telegram("🚀 Bot LEGO online e funzionante!")

while True:
    time.sleep(60)
