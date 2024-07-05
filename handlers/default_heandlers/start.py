from telebot.types import Message
from keyboards.buttons import create_start_keyboard
from database.database_connector import User
from handlers.custom_hendlers.command_history_handler import record_command
from telebot import TeleBot


def bot_start(message: Message, bot: TeleBot) -> None:
    """
    Обрабатывает команду /start от пользователя. Создает клавиатуру стартового экрана и отправляет
    приветственное сообщение в зависимости от наличия пользователя в базе данных.

    :param message: (Message) Объект сообщения от пользователя.
    :param bot: (TeleBot) Экземпляр бота Telegram для отправки сообщений.
    :return: None
    """
    keyboard = create_start_keyboard()
    record_command(message, message.text)
    try:

        User.get(User.telegram_username == message.from_user.username)

        bot.send_message(message.chat.id, f'Привет, {message.from_user.full_name}!\n'
                                          f'Хочешь сегодня поиграть?', reply_markup=keyboard)
    except User.DoesNotExist:

        User.create(telegram_username=message.from_user.username)
        bot.send_message(message.chat.id, f'Привет, {message.from_user.full_name}!\n'
                                          f'Теперь вы добавлены в базу данных. Хотите сегодня поиграть?',
                         reply_markup=keyboard)
