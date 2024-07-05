from telebot.types import Message
from telebot import TeleBot
from telebot import types
from handlers.custom_hendlers.steam_id_handler import search_steam_id
from handlers.custom_hendlers.command_history_handler import record_command


def response_processing(message: Message, bot: TeleBot) -> None:
    """
    Функция для обработки ответов пользователя и отправки соответствующих сообщений или изображений.

    :param message:(Message): Объект сообщения от пользователя.
    :param bot:(TeleBot): Экземпляр бота Telegram, используемый для отправки сообщений.
    :return:None: Функция не возвращает значения, а отправляет сообщения пользователю через бота.
    """
    if message.text == 'Да, конечно!':
        bot.send_message(message.chat.id, 'Введите ссылку на ваш профиль в Steam',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, lambda msg: search_steam_id(msg, bot))

        return
    elif message.text == 'Нет, спасибо':
        bot.send_message(message.chat.id, "Хорошо, возвращайся...")
        image_url = ("https://yt3.googleusercontent.com/5Wc_-fTDdrZ8d4WQrQGkBVTPFUoYk311jBGqwytXxp1UyKglaqqEjz8bGdGCd"
                     "DjJDFxKsUCz2w=s900-c-k-c0x00ffffff-no-rj")
        bot.send_photo(message.chat.id, image_url, reply_markup=types.ReplyKeyboardRemove())
