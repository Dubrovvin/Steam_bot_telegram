#Модуль с настройками бота
import telebot
from dotenv import load_dotenv
import os
from telebot.storage import StateMemoryStorage


load_dotenv()

STEAM_API_KEY = os.getenv('API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('BOT_TOKEN')

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('id', "Ввод Steam ID"),
    ('preference', "Выбор сортировки игр")
)

STEAM_API_URL = "http://api.steampowered.com"
storage = StateMemoryStorage()
bot = telebot.TeleBot(token=TELEGRAM_BOT_TOKEN, state_storage=storage)
