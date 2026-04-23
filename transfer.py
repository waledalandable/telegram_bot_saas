from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
from accounts import get_account
from anti_ban import delay, long_break
from config import API_ID, API_HASH
import time

def run_transfer(source, target, bot, chat_id):
    account = get_account()
    with TelegramClient(account, API_ID, API_HASH) as client:
        users = client.get_participants(source)
        success = 0
        for i, user in enumerate(users):
            try:
                client.invite_to_channel(target, [user.id])
                success += 1
                delay()
                if i % 20 == 0:
                    long_break()
            except FloodWaitError as e:
                time.sleep(e.seconds)
            except Exception:
                continue
    bot.send_message(chat_id, f"✅ تم نقل {success} عضو")
