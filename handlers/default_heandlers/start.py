from telebot.types import Message
from keyboards.buttons import create_start_keyboard
from database import database_connector

def bot_start(message: Message, bot):
    keyboard = create_start_keyboard()
    bot.send_message(message.chat.id, f'Привет, {message.from_user.full_name}\n'
                                      f'Хочешь сегодня поиграть?', reply_markup=keyboard)



