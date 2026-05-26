import telebot
import socket
import psutil
import json
import os

# =========================
# BOT TOKEN
# =========================
TOKEN = "8942738355:AAGbhwKSybNuQdJzUVXn0hg2HNiaFoCjXI8"

bot = telebot.TeleBot(TOKEN)

# =========================
# USERS FILE
# =========================
USERS_FILE = "users.json"

# Create users file if missing
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump({}, f)

# =========================
# LOAD DATA
# =========================
def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return {}

# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🤖 DRX BOT IS ONLINE ✅")

# =========================
# MYINFO COMMAND
# =========================
@bot.message_handler(commands=['myinfo'])
def myinfo(m):

    users = load_data(USERS_FILE)

    user_id = str(m.from_user.id)

    if user_id in users:

        bot.reply_to(
            m,
            f"👤 User Info:\n"
            f"Plan: {users[user_id].get('plan', 'Free')}\n"
            f"Status: Active ✅"
        )

    else:
        bot.reply_to(
            m,
            "❌ No active plan found."
        )

# =========================
# STATUS COMMAND
# =========================
@bot.message_handler(commands=['status'])
def status(m):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(2)

    try:
        s.connect(('127.0.0.1', 8080))
        api_status = "Online 🟢"
        s.close()

    except:
        api_status = "Offline 🔴"

    cpu_usage = psutil.cpu_percent(interval=1)

    ram_usage = psutil.virtual_memory().percent

    load_icon = (
        "🟢" if cpu_usage < 50
        else "🟡" if cpu_usage < 80
        else "🔴"
    )

    status_text = (
        "📊 DRX POWER LIVE STATUS\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"🤖 Bot Status: Active ✅\n"
        f"🔌 API Connection: {api_status}\n"
        f"🖥️ CPU Load: {cpu_usage}% {load_icon}\n"
        f"💾 RAM Usage: {ram_usage}% 🟢\n"
        f"🚀 VPS Power: 32GB OPTIMIZED\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    bot.reply_to(m, status_text)

# =========================
# RUN BOT
# =========================
print("BOT IS RUNNING...")

bot.infinity_polling(skip_pending=True) 

