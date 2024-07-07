from telebot.types import Message
from telebot import TeleBot


def bot_echo(message: Message, bot: TeleBot) -> None:
    """
    Отправляет сообщение пользователю, если бот не понимает его сообщение.

    :param message: Объект сообщения от пользователя.
    :param bot: Экземпляр бота Telegram для отправки сообщений.
    """
    bot.send_message(message.chat.id, "Я не понимаю вашего сообщения. "
                                      "Пожалуйста, используйте команды или введите /help для справки.")
