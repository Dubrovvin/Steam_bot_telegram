import telebot
from config_data.config import TELEGRAM_BOT_TOKEN, API_KEY
from handlers.default_heandlers.echo import bot_echo
from handlers.default_heandlers.help import bot_help
from handlers.default_heandlers.start import bot_start
from handlers.game_preference_handler import handle_game_preference
from handlers.steam_id_handler import handle_steam_id

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot_start(message, bot)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot_help(message, bot)



bot.polling()