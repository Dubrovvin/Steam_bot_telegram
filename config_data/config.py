import telebot
from dotenv import load_dotenv
import os
from telebot.storage import StateMemoryStorage


# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение ключей API и токена бота из переменных окружения
STEAM_API_KEY = os.getenv('API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('BOT_TOKEN')

# Список стандартных команд бота с их описаниями
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('id', "Ввод Steam ID"),
    ('preference', "Выбор сортировки игр")
)

# Базовый URL для API Steam
STEAM_API_URL = "http://api.steampowered.com"

# Инициализация хранилища состояний для бота
storage = StateMemoryStorage()

# Создание экземпляра бота Telegram с использованием токена и указанием хранилища состояний
bot = telebot.TeleBot(token=TELEGRAM_BOT_TOKEN, state_storage=storage)
