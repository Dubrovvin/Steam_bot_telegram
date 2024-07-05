from keyboards.buttons import create_help_keyboard
from telebot.types import Message
from telebot import TeleBot


def bot_help(message: Message, bot: TeleBot) -> None:
    """
    Отправляет пользователю справочное сообщение с описанием доступных команд и предложением помощи.

    :param message: Объект сообщения от пользователя.
    :param bot: Экземпляр бота Telegram для отправки сообщений.
    """
    help_text = 'Этот бот помогает вам находить игры на основе ваших предпочтений. ' \
                'Доступные команды:\n' \
                '/start - Начало взаимодейсвия, при котором загружаются твои данные\n' \
                '/preference - выбрать каким играм отдаёшь приоритет сегодня, новым или старым\n' \
                '/history - показать историю ваших последних запросов\n'\
                '/users - список всех желающих поиграть\n'\
                '/help - показать эту справку\n' \
                '\n'\

    keyboard = create_help_keyboard()
    bot.send_message(message.chat.id, help_text, reply_markup=keyboard)
