from telebot.types import Message
from telebot import TeleBot
from config_data.config import bot
from handlers.default_heandlers import start, help, echo
from handlers.custom_hendlers import (game_preference_handler, steam_id_handler, response_handler,
                                      command_history_handler, active_users_handler)

@bot.message_handler(commands=['history'])
def handle_history_command(message: Message) -> None:
    """
    Обработчик команды /history.

    :param message: Объект сообщения от пользователя (telebot.types.Message).
    """
    command_history_handler.handle_history_command(message, bot)
    command_history_handler.record_command(message, '/history')


@bot.message_handler(commands=['help'])
def handle_help(message: Message) -> None:
    """
    Обработчик команды /history.

    :param message: Объект сообщения от пользователя (telebot.types.Message).
    """
    help.bot_help(message, bot)
    command_history_handler.record_command(message, '/help')


@bot.message_handler(commands=['preference'])
def game_preference(message: Message) -> None:
    """
    Обработчик команды /preference.

    :param message: Объект сообщения от пользователя (telebot.types.Message).
    """
    game_preference_handler.handle_game_preference(message, bot)
    command_history_handler.record_command(message, '/preference')


@bot.message_handler(commands=['users'])
def active_users(message: Message) -> None:
    """
    Обработчик команды /users.

    :param message: Объект сообщения от пользователя (telebot.types.Message).
    """
    active_users_handler.get_users(message, bot)
    command_history_handler.record_command(message, '/users')


@bot.message_handler(commands=['start'])
def handle_start(message: Message) -> None:
    """
    Обработчик команды /start.

    :param message: Объект сообщения от пользователя (telebot.types.Message).
    """
    start.bot_start(message, bot)


@bot.message_handler(func=lambda message: message.text in ['Да, конечно!', 'Нет, спасибо'])
def getting_response(message: Message) -> None:
    """
    Обработчик ответа пользователя на предложение поиграть.

    :param message: Объект сообщения от пользователя (telebot.types.Message).
    """
    response_handler.response_processing(message, bot)
    command_history_handler.record_command(message, message.text)


@bot.message_handler(func=lambda message: True)
def handle_echo(message: Message) -> None:
    """
    Обработчик неизвестных команд (echo).

    :param message: Объект сообщения от пользователя (telebot.types.Message).
    """
    echo.bot_echo(message, bot)
    command_history_handler.record_command(message, 'Unknown command')


def load() -> TeleBot:
    """
    Возвращает экземпляр бота Telegram.

    :return: Экземпляр бота Telegram (TeleBot).
    """
    return bot
