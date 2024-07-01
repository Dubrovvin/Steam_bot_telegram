#Модуль с настройками бота
from dotenv import load_dotenv
import os


load_dotenv()

STEAM_API_KEY = os.getenv('API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('BOT_TOKEN')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку")
)
