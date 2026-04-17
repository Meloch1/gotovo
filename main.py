import os
import threading
import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher

# =========================
# 🌐 MINI APP (FLASK)
# =========================
app = Flask(__name__)

@app.route("/")
def home():
    return "Mini App работает 🚀"


def run_web():
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)


# =========================
# 🤖 TELEGRAM BOT
# =========================
TOKEN = "8764130569:AAFd981I0jKeDPWmgEU0IzsLPV1nT8yQdvc"

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def start_bot():
    await dp.start_polling(bot)


# =========================
# 🚀 START BOTH
# =========================
if __name__ == "__main__":
    # веб (mini app)
    threading.Thread(target=run_web).start()

    # бот
    asyncio.run(start_bot())
