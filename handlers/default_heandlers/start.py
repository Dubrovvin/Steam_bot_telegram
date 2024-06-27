from telebot.types import Message
from loader import bot


def bot_start(message: Message, bot):
    bot.send_message(message, f'Привет, {message.from_user.full_name}\n'
                              f' Хочешь сегодня поиграть?')