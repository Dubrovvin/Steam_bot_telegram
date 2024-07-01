from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config
from handlers.default_heandlers import start, help, echo
from handlers.custom_hendlers import game_preference_handler, steam_id_handler, response_handler



storage = StateMemoryStorage()
bot = TeleBot(token=config.TELEGRAM_BOT_TOKEN, state_storage=storage)

@bot.message_handler(commands=['start'])
def handle_start(message):
    start.bot_start(message, bot)

@bot.message_handler(func=lambda message: message.text in ['Да, конечно!', 'Нет, спасибо'])
def getting_response(message):
    response_handler.response_processing(message, bot)

@bot.message_handler(func=lambda message: message.text)
def steam_id(message):
    steam_id_handler.handle_steam_id(message, bot)

@bot.message_handler(func=lambda message: message.text in ['Любимые игры', 'Новые игры'])
def game_preference(message):
    game_preference_handler.handle_game_preference(message, bot)

def load():
    return bot
