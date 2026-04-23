import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))

API_ID = int(os.getenv("API_ID", "12345"))
API_HASH = os.getenv("API_HASH")

PLANS = {
    "basic": {"price": "10$", "limit": 100},
    "pro": {"price": "25$", "limit": 500},
    "vip": {"price": "50$", "limit": 2000}
}
