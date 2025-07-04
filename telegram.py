import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

MAX_MESSAGE_LENGTH = 4096

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    # Split the message if it's too long
    parts = [message[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(message), MAX_MESSAGE_LENGTH)]

    for idx, part in enumerate(parts):
        print(f"📤 Sending message chunk {idx + 1} of {len(parts)}...")
        response = requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": part
        })

        if not response.ok:
            print(f"❌ Failed to send chunk {idx + 1}: {response.text}")
            break
