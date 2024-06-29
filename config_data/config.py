from dotenv import load_dotenv
import os

if not found_dotenv():
    exit("Переменные окружения не загруженны т.к. отсутствует файл .env")
else:
    load_dotenv()

API_KEY = os.getenv('API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('BOT_TOKEN')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку")
)
