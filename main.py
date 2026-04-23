import telebot
from config import BOT_TOKEN
from handlers import register
from keep_alive import keep_alive
from threading import Thread
from worker import start_worker

bot = telebot.TeleBot(BOT_TOKEN)

register(bot)

Thread(target=start_worker, args=(bot,), daemon=True).start()

keep_alive()

print("Bot is running...")
bot.infinity_polling()
