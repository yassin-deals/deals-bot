import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_message(text):
    if not TOKEN or not CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/test")
def test():
    send_message("✅ البوت خدام مزيان! هادي رسالة تجريبية من deals-bot")
    return "Message sent!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
