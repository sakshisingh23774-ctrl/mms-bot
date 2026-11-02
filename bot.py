import telebot
import qrcode
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from flask import Flask
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

COURSES = {
    1: "Trading", 2: "Crypto", 3: "Dropshipping",
    4: "Editing", 5: "Stock Market", 6: "AI Tools",
    7: "YouTube", 8: "Instagram", 9: "Freelancing",
    10: "Affiliate", 11: "Coding", 12: "English",
    13: "Business", 14: "Ebooks", 15: "MEGA PACK",
}

DEMO_LINK = "https://t.me/+bx0nRQTYEJg0M2Y1"
PROOF_LINK = "https://t.me/prooftelegarmmafiya"
SUPPORT_LINK = "https://t.me/saniya5666"
UPI_ID = "rkrj55055@okicici"
UPI_PAY = f"upi://pay?pa={UPI_ID}&pn=Course&am=299&cu=INR"

def main_menu():
    markup = InlineKeyboardMarkup()
    # 15 Channels - 3 ek line me
    markup.add(InlineKeyboardButton(f"📚 {COURSES[1]}", callback_data="course_1"), InlineKeyboardButton(f"📚 {COURSES[2]}", callback_data="course_2"), InlineKeyboardButton(f"📚 {COURSES[3]}", callback_data="course_3"))
    markup.add(InlineKeyboardButton(f"📚 {COURSES[4]}", callback_data="course_4"), InlineKeyboardButton(f"📚 {COURSES[5]}", callback_data="course_5"), InlineKeyboardButton(f"📚 {COURSES[6]}", callback_data="course_6"))
    markup.add(InlineKeyboardButton(f"📚 {COURSES[7]}", callback_data="course_7"), InlineKeyboardButton(f"📚 {COURSES[8]}", callback_data="course_8"), InlineKeyboardButton(f"📚 {COURSES[9]}", callback_data="course_9"))
    markup.add(InlineKeyboardButton(f"📚 {COURSES[10]}", callback_data="course_10"), InlineKeyboardButton(f"📚 {COURSES[11]}", callback_data="course_11"), InlineKeyboardButton(f"📚 {COURSES[12]}", callback_data="course_12"))
    markup.add(InlineKeyboardButton(f"📚 {COURSES[13]}", callback_data="course_13"), InlineKeyboardButton(f"📚 {COURSES[14]}", callback_data="course_14"), InlineKeyboardButton(f"📚 {COURSES[15]}", callback_data="course_15"))
    markup.add(InlineKeyboardButton("🎬 DEMO", url=DEMO_LINK), InlineKeyboardButton("✅ PROOF", url=PROOF_LINK))
    markup.add(InlineKeyboardButton("🛠 SUPPORT @saniya5666", url=SUPPORT_LINK))
    return markup

def pay_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💳 PAYMENT 299Rs", url=UPI_PAY), InlineKeyboardButton("📲 SEND SCREENSHOT", url=SUPPORT_LINK))
    markup.add(InlineKeyboardButton("🎬 DEMO", url=DEMO_LINK), InlineKeyboardButton("✅ PROOF", url=PROOF_LINK))
    markup.add(InlineKeyboardButton("🔙 BACK", callback_data="back"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    text = f"🔥 Welcome {message.from_user.first_name} 🔥\n\n*All Courses @ 299 Rs Only*\n\n👇 *Yaha 15 Courses Hai - Select Karo* 👇"
    bot.send_message(message.chat.id, text, reply_markup=main_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def all_callbacks(call):
    if call.data.startswith("course_"):
        cid = int(call.data.split("_")[1])
        qr = qrcode.make(UPI_PAY)
        qr.save("/tmp/qr.png")
        caption = f"*{COURSES[cid]} Course*\n\n💵 Price: 299 Rs\nUPI: `{UPI_ID}`\n\n1. QR Scan karo\n2. PAYMENT button dabao\n3. SEND SCREENSHOT bhejo"
        with open("/tmp/qr.png", "rb") as f:
            bot.send_photo(call.message.chat.id, f, caption=caption, reply_markup=pay_menu(), parse_mode="Markdown")
    elif call.data == "back":
        bot.send_message(call.message.chat.id, "👇 *15 Courses - 299Rs* 👇", reply_markup=main_menu(), parse_mode="Markdown")
    bot.answer_callback_query(call.id)

app = Flask(__name__)
@app.route('/')
def home(): return "Bot Running"
def run_bot(): bot.infinity_polling(skip_pending=True)
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
