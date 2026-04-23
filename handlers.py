from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import PLANS, ADMIN_ID
from database import add_user, get_user, set_plan
from queue_system import add_task

user_states = {}

def register(bot):

    @bot.message_handler(commands=['start'])
    def start(m):
        add_user(m.from_user.id)
        kb = InlineKeyboardMarkup()
        kb.add(
            InlineKeyboardButton("📦 الاشتراك", callback_data="plans"),
            InlineKeyboardButton("📤 نقل أعضاء", callback_data="transfer")
        )
        kb.add(InlineKeyboardButton("📊 حسابي", callback_data="profile"))
        bot.send_message(m.chat.id, "👋 أهلاً بك", reply_markup=kb)

    @bot.callback_query_handler(func=lambda c: c.data == "plans")
    def plans(call):
        kb = InlineKeyboardMarkup()
        for plan, data in PLANS.items():
            kb.add(InlineKeyboardButton(f"{plan} - {data['price']}", callback_data=f"buy_{plan}"))
        bot.edit_message_text("📦 اختر الباقة:", call.message.chat.id, call.message.message_id, reply_markup=kb)

    @bot.callback_query_handler(func=lambda c: c.data.startswith("buy_"))
    def buy(call):
        plan = call.data.split("_")[1]
        set_plan(call.from_user.id, plan)
        bot.send_message(call.message.chat.id, "💳 أرسل صورة التحويل")

    @bot.callback_query_handler(func=lambda c: c.data == "profile")
    def profile(call):
        user = get_user(call.from_user.id)
        plan = user["plan"] if user else "لا يوجد"
        bot.send_message(call.message.chat.id, f"📊 الباقة: {plan}")

    @bot.callback_query_handler(func=lambda c: c.data == "transfer")
    def transfer(call):
        user_states[call.from_user.id] = "transfer"
        bot.send_message(call.message.chat.id, "📤 أرسل source,target")

    @bot.message_handler(func=lambda m: True, content_types=['text','photo'])
    def handle(m):
        if user_states.get(m.from_user.id) == "transfer":
            try:
                source, target = m.text.split(",")
                add_task({"source": source.strip(), "target": target.strip(), "chat_id": m.chat.id})
                bot.send_message(m.chat.id, "⏳ تم إضافة المهمة")
                user_states[m.from_user.id] = None
            except:
                bot.send_message(m.chat.id, "❌ صيغة خاطئة")
        elif m.photo:
            bot.forward_message(ADMIN_ID, m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "⏳ تم إرسال طلبك")
