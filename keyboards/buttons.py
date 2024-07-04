from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def create_start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Да, конечно!'))
    keyboard.add(KeyboardButton('Нет, спасибо'))
    return keyboard


def create_game_preference_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Попробовать что-то новое'))
    keyboard.add(KeyboardButton('Предпочту любимые игры'))
    return keyboard


def create_yes_and_no_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Да'))
    keyboard.add(KeyboardButton('Нет'))
    return keyboard


def create_new_and_old_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Новая'))
    keyboard.add(KeyboardButton('Любимая'))
    return keyboard

def create_next_step_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Выбирать приоритет игр'))
    keyboard.add(KeyboardButton('Начать заново'))
    keyboard.add(KeyboardButton('Помощь'))
    return keyboard