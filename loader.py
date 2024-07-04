from telebot import TeleBot
from config_data.config import bot
from handlers.default_heandlers import start, help, echo
from handlers.custom_hendlers import (game_preference_handler, steam_id_handler, response_handler,
                                      command_history_handler)
from database.database_connector import CommandHistory, User

@bot.message_handler(commands=['history'])
def handle_history_command(message):
    command_history_handler.handle_history_command(message, bot)
    command_history_handler.record_command(message, '/history')


@bot.message_handler(commands=['help', 'Помощь'])
def handle_help(message):
    help.bot_help(message, bot)
    command_history_handler.record_command(message, '/help')


@bot.message_handler(commands=['start', 'Начать заново'])
def handle_start(message):
    start.bot_start(message, bot)
    #command_history_handler.record_command(message, '/start')


@bot.message_handler(func=lambda message: message.text in ['Да, конечно!', 'Нет, спасибо'])
def getting_response(message):
    response_handler.response_processing(message, bot)
    command_history_handler.record_command(message, message.text)


@bot.message_handler(func=lambda message: message.text)
def steam_id(message):
    steam_id_handler.get_url(message, bot)


@bot.message_handler(commands=['/preference', 'Выбирать приоритет игр'])
def game_preference(message):
    game_preference_handler.handle_game_preference(message, bot)


@bot.message_handler(func=lambda message: True)
def handle_echo(message):
    echo.bot_echo(message, bot)
    command_history_handler.record_command(message, 'Unknown command')




def load():
    return bot

