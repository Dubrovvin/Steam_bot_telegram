import telebot
from config_data.config import TELEGRAM_BOT_TOKEN
from loader import load
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


if __name__ == "__main__":
    bot = load()
    bot.polling(none_stop=True)
