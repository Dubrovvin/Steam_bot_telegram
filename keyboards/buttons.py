from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def create_start_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для начала взаимодействия с ботом.

    :return: (ReplyKeyboardMarkup) Клавиатура с кнопками "Да, конечно!" и "Нет, спасибо".
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Да, конечно!'))
    keyboard.add(KeyboardButton('Нет, спасибо'))
    return keyboard


def create_game_preference_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для выбора предпочтений игры.

    :return: (ReplyKeyboardMarkup) Клавиатура с кнопками "Попробовать что-то новое" и "Предпочту любимые игры".
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Попробовать что-то новое'))
    keyboard.add(KeyboardButton('Предпочту любимые игры'))
    return keyboard


def create_yes_and_no_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для ответа "Да" или "Нет".

    :return: (ReplyKeyboardMarkup) Клавиатура с кнопками "Да" и "Нет".
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Да'))
    keyboard.add(KeyboardButton('Нет'))
    return keyboard


def create_new_and_old_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для выбора типа игры: "Новая" или "Любимая".

    :return: (ReplyKeyboardMarkup) Клавиатура с кнопками "Новая" и "Любимая".
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Новая'))
    keyboard.add(KeyboardButton('Любимая'))
    return keyboard


def create_next_step_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для выбора следующего шага действий.

    :return: (ReplyKeyboardMarkup) Клавиатура с кнопками "Выбирать приоритет игр", "Начать заново" и "Помощь".
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Выбирать приоритет игр'))
    keyboard.add(KeyboardButton('Начать заново'))
    keyboard.add(KeyboardButton('Помощь'))
    return keyboard


def create_help_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру с командами для вызова помощи.

    :return: (ReplyKeyboardMarkup) Клавиатура с кнопками команд "/start", "/preference", "/history", "/users", "/help".
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        KeyboardButton(text='/start'),
        InlineKeyboardButton(text='/preference'),
        InlineKeyboardButton(text='/history'),
        InlineKeyboardButton(text='/users'),
        InlineKeyboardButton(text='/help')
    ]
    keyboard.add(*buttons)
    return keyboard
