# ping.py
import requests
from datetime import datetime

URL = "https://legal-chatbot-gah7.onrender.com/health"  # 👉 Thay bằng URL app Flask của bạn

def ping():
    try:
        response = requests.get(URL, timeout=10)
        print(f"[{datetime.now()}] Pinged {URL} - Status: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] Error pinging: {e}")

if __name__ == "__main__":
    ping()
