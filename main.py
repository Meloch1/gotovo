import os
import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher
from threading import Thread

# ================= MINI APP =================
app = Flask(__name__)

@app.route("/")
def home():
    return "Mini App OK 🚀"

def run_web():
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)


# ================= BOT =================
TOKEN = "8764130569:AAFd981I0jKeDPWmgEU0IzsLPV1nT8yQdvc"
print("TOKEN =", TOKEN)

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def start_bot():
    print("BOT STARTING...")
    await dp.start_polling(bot)


# ================= RUN =================
if __name__ == "__main__":
    Thread(target=run_web).start()

    print("WEB STARTED")
    asyncio.run(start_bot())
