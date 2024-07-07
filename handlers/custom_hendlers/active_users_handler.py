from database.database_connector import User  # Импортируем модель User из вашего модуля
from telebot import TeleBot, types
from telebot.types import Message


def get_users(message: Message, bot: TeleBot) -> None:
    """
    Отправляет список зарегистрированных пользователей Telegram из базы данных.

    :param message: (Message) Объект сообщения от пользователя.
    :param bot: (TeleBot) Экземпляр бота Telegram.
    """
    all_users = User.select()

    # Если нет пользователей в базе данных, сообщаем об этом
    if not all_users:
        bot.send_message(message.chat.id, 'В базе данных нет зарегистрированных пользователей.')
        return

    # Формируем сообщение со списком пользователей
    user_list_message = 'Список зарегистрированных пользователей:\n'
    for idx, user in enumerate(all_users, start=1):
        user_list_message += f'{idx}. @{user.telegram_username}\n'

    # Отправляем сообщение с списком пользователей
    bot.send_message(message.chat.id, user_list_message)
