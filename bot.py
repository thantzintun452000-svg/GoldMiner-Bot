import logging
from telegram.ext import Updater, CommandHandler

# 👉 Bot Token ကို တိုက်ရိုက် ထည့်ထားသည်
TOKEN = "8261763462:AAFLl4RTMctrrLMU4_0kPJ2vkdUuwVXd7"

# Log config
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def start(update, context):
    update.message.reply_text("မင်္ဂလာပါ 👋 LuckyMinerMyanmarBot အလုပ်လုပ်နေပါပြီ!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
