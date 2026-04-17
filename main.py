import os
import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher
from threading import Thread

# ================= MINI APP =================
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Mini App</title>
    </head>
    <body>
        <h1>Мой Mini App 🚀</h1>
        <button onclick="alert('Работает!')">Нажми меня</button>
    </body>
    </html>
    """

def run_web():
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)


# ================= BOT =================
TOKEN = "8709032546:AAFhAcwfj5kpszP4NWr8LtGSMpIxpKkOvuY"
print("TOKEN =", TOKEN)

bot = Bot(token=TOKEN)
dp = Dispatcher()
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Открыть Mini App 🚀",
        web_app=WebAppInfo(url="gotovo-production.up.railway.app")
    )]
])

from aiogram import types, F

@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer("Бот работает 🚀")

async def start_bot():
    print("BOT STARTING...")
    await dp.start_polling(bot)


# ================= RUN =================
if __name__ == "__main__":
    Thread(target=run_web).start()

    print("WEB STARTED")
    asyncio.run(start_bot())

from aiogram import types

@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет 👋 бот работает!")
