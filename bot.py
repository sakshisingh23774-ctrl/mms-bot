<html>
        <head><title>Downloaded HTML</title></head>
        <body>
            <pre style="white-space: pre-wrap; word-wrap: break-word;">import telebot
import qrcode
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from flask import Flask
import threading

# ===== TOKEN - READY HAI =====
BOT_TOKEN = "9253380875:AAEO87fr-pBGKM-vI-QTlYVeLw9ri_yfWFs"
bot = telebot.TeleBot(BOT_TOKEN)

# ===== 15 CHANNELS - SHORT NAME - SAB 299Rs =====
COURSES = {
    1: {"name": "indian CP"}, 2: {"name": "tamil wife"}, 3: {"name": "mom son"},
    4: {"name": "indian threesome"}, 5: {"name": "indian couple"}, 6: {"name": mom son indian"},
    7: {"name": "tamil couple"}, 8: {"name": "indian wife sharing"}, 9: {"name": "punjabi couple},
    10: {"name": 'indian wife african man"}, 11: {"name": "all chennall"}, 
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
    bot.send_message(message.chat.id, "🔥 *All Courses @ 299 Rs Only* 🔥\n\n👇 *15 Courses* 👇\nDEMO, PROOF, SUPPORT check karo", reply_markup=main_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data.startswith("course_"):
        cid = int(call.data.split("_")[1])
        qr_path = generate_qr()
        caption = f"*{COURSES[cid]['name']} Course - 299 Rs*\n\n*UPI:* `{UPI_ID}`\n\n1. QR Scan karo\n2. PAYMENT button dabao\n3. SEND SCREENSHOT bhejo @saniya5666 pe"
        with open(qr_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=caption, reply_markup=payment_menu(), parse_mode="Markdown")
    elif call.data == "back":
        bot.send_message(call.message.chat.id, "👇 *15 Courses - 299Rs* 👇", reply_markup=main_menu(), parse_mode="Markdown")
    bot.answer_callback_query(call.id)

# Render ke liye server
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot Running - 15 Courses @ 299"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))</pre>
        </body>
    </html>