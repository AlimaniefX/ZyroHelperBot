import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

def start(update, context):
    update.message.reply_text("أهلاً! 👋 أنا بوت المساعد جاهز أساعدك.")

def joke(update, context):
    update.message.reply_text("😂 نكتة: مرة واحد راح للدكتور، قاله عندي نسيان شديد، قاله من متى؟ قاله من متى إيش؟")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("joke", joke))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
