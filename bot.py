import telebot
import qrcode
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from flask import Flask
import threading

# ===== TOKEN - READY HAI =====
BOT_TOKEN = "9253380875:AAHp41XT_Iz1fHzw3LWZPAsNa3zsCe22r4Y
bot = telebot.TeleBot(BOT_TOKEN)

# ===== 15 CHANNELS - SHORT NAME - SAB 299Rs =====
COURSES = {
    1: {"name": "Premium CP}, 2: {"name": "Indian CP"}, 3: {"name": "gay CP"},
    4: {"name": "RAP forestg"}, 5: {"name": "Mom SON CCTV"}, 6: {"name": "BAD Parents CP"},
    7: {"name": "Indian Hidden"}, 8: {"name": "Shemale"}, 9: {"name": "Sister Spy"},
    10: {"name": "Teen Girls"}, 11: {"name": "School GIRL"}, 12: {"name": "Bro Sister"},
    13: {"name": "Indian Mom son "}, 14: {"name": "Oyo leked"}, 
}

# ===== FINAL LINKS =====
DEMO_LINK = "https://t.me/+bx0nRQTYEJg0M2Y1"
PROOF_LINK = "https://t.me/prooftelegarmmafiya"
SUPPORT_LINK = "https://t.me/saniya5666"
UPI_ID = "rkrj55055@okicici"
UPI_PAY_STRING = f"upi://pay?pa={UPI_ID}&pn=CourseSeller&am=299&cu=INR&tn=Course 299"

def generate_qr():
    qr = qrcode.make(UPI_PAY_STRING)
    path = "/tmp/payment_qr.png"
    qr.save(path)
    return path

def main_menu():
    markup = InlineKeyboardMarkup(row_width=3)
    btns = [InlineKeyboardButton(f"{COURSES[i]['name']}", callback_data=f"course_{i}") for i in range(1, 16)]
    markup.add(*btns)
    markup.row(InlineKeyboardButton("🎬 DEMO", url=DEMO_LINK), InlineKeyboardButton("✅ PROOF", url=PROOF_LINK))
    markup.row(InlineKeyboardButton("🛠 SUPPORT", url=SUPPORT_LINK))
    return markup

def payment_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(InlineKeyboardButton("💳 PAYMENT 299Rs", url=UPI_PAY_STRING), InlineKeyboardButton("📲 SEND SCREENSHOT", url=SUPPORT_LINK))
    markup.row(InlineKeyboardButton("✅ PROOF", url=PROOF_LINK), InlineKeyboardButton("🎬 DEMO", url=DEMO_LINK))
    markup.row(InlineKeyboardButton("🔙 BACK", callback_data="back"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🔥 *Welcom All video Mms bot
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data.startswith("course_"):
        cid = int(call.data.split("_")[1])
        qr_path = generate_qr()
        caption = f"*{COURSES[cid]['name']} Course - 299 Rs*\n\n*UPI:* `{UPI_ID}`\n\n1. QR Scan karo\n2. PAYMENT button dabao\n3. SEND SCREENSHOT bhejo @saniya5666 pe"
        with open(qr_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=caption, reply_markup=payment_menu(), parse_mode="Markdown")
    elif call.data == "back":
        bot.send_message(call.message.chat.id, "👇 *group price - 299Rs* 👇", reply_markup=main_menu(), parse_mode="Markdown")
    bot.answer_callback_query(call.id)

# Render ke liye server
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot Running - 15 Groups @ 299"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
