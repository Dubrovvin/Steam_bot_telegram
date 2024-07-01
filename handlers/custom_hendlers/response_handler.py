from telebot.types import Message
from telebot import TeleBot
from telebot import types

def response_processing(message: Message, bot: TeleBot) -> None:
    """
    Функция для обработки ответов пользователя и отправки соответствующих сообщений или изображений.

    :param message:(Message): Объект сообщения от пользователя.
    :param bot:(TeleBot): Экземпляр бота Telegram, используемый для отправки сообщений.
    :return:None: Функция не возвращает значения, а отправляет сообщения пользователю через бота.
    """
    if message.text == 'Да, конечно!':
        bot.send_message(message.chat.id, 'Введите, пожалуйста, ваш Steam ID',
                         reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'Нет, спасибо':
        bot.send_message(message.chat.id, "Хорошо, вернусь позже...")
        image_url = ("https://yt3.googleusercontent.com/5Wc_-fTDdrZ8d4WQrQGkBVTPFUoYk311jBGqwytXxp1UyKglaqqEjz8bGdGCd"
                     "DjJDFxKsUCz2w=s900-c-k-c0x00ffffff-no-rj")
        bot.send_photo(message.chat.id, image_url, reply_markup=types.ReplyKeyboardRemove())
