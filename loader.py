from telebot import TeleBot
from config_data.config import bot
from handlers.default_heandlers import start, help, echo
from handlers.custom_hendlers import game_preference_handler, steam_id_handler, response_handler, find_steam_id_handler



@bot.message_handler(commands=['start'])
def handle_start(message):
    start.bot_start(message, bot)


@bot.message_handler(func=lambda message: message.text in ['Да, конечно!', 'Нет, спасибо'])
def getting_response(message):
    response_handler.response_processing(message, bot)


@bot.message_handler(func=lambda message: message.text)
def steam_id(message):
    steam_id_handler.get_url(message, bot)


@bot.message_handler(func=lambda message: message.text)
def game_preference(messege, bot):
    game_preference_handler.handle_game_preference((messege, bot))


#@bot.message_handler(func=lambda message: message.text in ['Попробовать что-то новое', 'Предпочту любимые игры'])
#def game_preference(message):
 #   game_preference_handler.handle_game_preference(message, bot)


def load():
    return bot
