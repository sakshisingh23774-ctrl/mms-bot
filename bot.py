import telebot
import qrcode
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from flask import Flask
import threading
import io

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
UPI_PAY = f"upi://pay?pa={UPI_ID}&pn=Course&am=299&cu=INR&tn=Course299"

def make_qr():
    qr_img = qrcode.make(UPI_PAY)
    bio = io.BytesIO()
    qr_img.save(bio, 'PNG')
    bio.seek(0)
    return bio

def main_menu():
    m = InlineKeyboardMarkup()
    m.add(InlineKeyboardButton(f"📚 {COURSES[1]}", callback_data="course_1"), InlineKeyboardButton(f"📚 {COURSES[2]}", callback_data="course_2"), InlineKeyboardButton(f"📚 {COURSES[3]}", callback_data="course_3"))
    m.add(InlineKeyboardButton(f"📚 {COURSES[4]}", callback_data="course_4"), InlineKeyboardButton(f"📚 {COURSES[5]}", callback_data="course_5"), InlineKeyboardButton(f"📚 {COURSES[6]}", callback_data="course_6"))
    m.add(InlineKeyboardButton(f"📚 {COURSES[7]}", callback_data="course_7"), InlineKeyboardButton(f"📚 {COURSES[8]}", callback_data="course_8"), InlineKeyboardButton(f"📚 {COURSES[9]}", callback_data="course_9"))
    m.add(InlineKeyboardButton(f"📚 {COURSES[10]}", callback_data="course_10"), InlineKeyboardButton(f"📚 {COURSES[11]}", callback_data="course_11"), InlineKeyboardButton(f"📚 {COURSES[12]}", callback_data="course_12"))
    m.add(InlineKeyboardButton(f"📚 {COURSES[13]}", callback_data="course_13"), InlineKeyboardButton(f"📚 {COURSES[14]}", callback_data="course_14"), InlineKeyboardButton(f"📚 {COURSES[15]}", callback_data="course_15"))
    m.add(InlineKeyboardButton("🎬 DEMO", url=DEMO_LINK), InlineKeyboardButton("✅ PROOF", url=PROOF_LINK))
    m.add(InlineKeyboardButton("🛠 SUPPORT", url=SUPPORT_LINK))
    return m

def pay_menu():
    m = InlineKeyboardMarkup()
    m.add(InlineKeyboardButton("💳 PAYMENT 299Rs", url=UPI_PAY), InlineKeyboardButton("📲 SEND SCREENSHOT", url=SUPPORT_LINK))
    m.add(InlineKeyboardButton("✅ PROOF", url=PROOF_LINK), InlineKeyboardButton("🎬 DEMO", url=DEMO_LINK))
    m.add(InlineKeyboardButton("🔙 BACK", callback_data="back"))
    return m

# ===== PRIVATE ME /start PE =====
@bot.message_handler(commands=['start'], chat_types=['private'])
def start_private(msg):
    bot.send_message(msg.chat.id, f"🔥 Welcome {msg.from_user.first_name} 🔥\n\n*All Courses @ 299 Rs*\n\n👇 15 Courses 👇", reply_markup=main_menu(), parse_mode="Markdown")

# ===== GROUP ME KOI BHI TOUCH KAREGA TO QR JAYEGA =====
@bot.message_handler(func=lambda m: True, content_types=['text'], chat_types=['group', 'supergroup'])
def group_touch(msg):
    # Agar group me koi bhi message likhega to QR bhej dega
    if "/start" in msg.text or "course" in msg.text.lower() or "price" in msg.text.lower() or "hi" in msg.text.lower() or True: # True matlab har message pe
        qr_bio = make_qr()
        cap = f"🔥 *All Courses @ 299 Rs Only* 🔥\n\n*UPI:* `{UPI_ID}`\n\n1. QR Scan karo\n2. PAYMENT karo\n3. SEND SCREENSHOT bhejo @saniya5666 pe"
        bot.send_photo(msg.chat.id, qr_bio, caption=cap, reply_markup=pay_menu(), parse_mode="Markdown")

# ===== BUTTONS KA REPLY =====
@bot.callback_query_handler(func=lambda call: True)
def cb(call):
    if call.data.startswith("course_"):
        cid = int(call.data.split("_")[1])
        qr_bio = make_qr()
        cap = f"*{COURSES[cid]} Course - 299 Rs*\n\n*UPI ID:* `{UPI_ID}`\n\nQR Scan karke PAYMENT karo"
        bot.send_photo(call.message.chat.id, qr_bio, caption=cap, reply_markup=pay_menu(), parse_mode="Markdown")
    elif call.data == "back":
        bot.send_message(call.message.chat.id, "👇 *15 Courses - 299Rs* 👇", reply_markup=main_menu(), parse_mode="Markdown")
    bot.answer_callback_query(call.id)

app = Flask(__name__)
@app.route('/')
def home(): return "Bot Running - Group QR Active"

def run_bot(): bot.infinity_polling(skip_pending=True)
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
