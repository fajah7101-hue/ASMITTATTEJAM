import telebot
import psutil
import socket

TOKEN = "8942738355:AAGbhwKSybNuQdJzUVXn0hg2HNiaFoCjXI8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is running ✅")

@bot.message_handler(commands=['status'])
def status(message):

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    text = f"""
🤖 BOT ONLINE ✅

CPU: {cpu}%
RAM: {ram}%
"""

    bot.reply_to(message, text)

print("BOT STARTED")

bot.infinity_polling()
