from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def create_start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Да, конечно!'))
    keyboard.add(KeyboardButton('Нет, спасибо'))
    return keyboard
