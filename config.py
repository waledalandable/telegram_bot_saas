import os

BOT_TOKEN = os.getenv("7787809968:AAHpKbErc_GmNfFaK0uLmlD__4taeNojSLQ")
ADMIN_ID = int(os.getenv("ADMIN_ID", "7496673554"))

API_ID = int(os.getenv("API_ID", "26310454"))
API_HASH = os.getenv("41e23da71019b8f6de44e601d029e6e7")

PLANS = {
    "basic": {"price": "10$", "limit": 100},
    "pro": {"price": "25$", "limit": 500},
    "vip": {"price": "50$", "limit": 2000}
}
