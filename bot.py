import logging
from telegram.ext import Updater, CommandHandler

# 👉 မင်းရဲ့ Bot Token
TOKEN = "8401563933:AAHg8-cST_r4W1HHxSHUpHjZacz9WdtVVlA"

# Log config
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def start(update, context):
    update.message.reply_text("မင်္ဂလာပါ 👋 Bot အလုပ်လုပ်နေပါပြီ ✅")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
