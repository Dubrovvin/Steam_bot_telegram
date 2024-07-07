from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, IntegerField, DateTimeField
from datetime import datetime
import schedule

# Инициализация SQLite базы данных и указание файла для хранения
db = SqliteDatabase('users_games.db')


class User(Model):
    """
    Модель для хранения информации о пользователях Telegram.
    """
    telegram_username = CharField(unique=True)  # Уникальный username пользователя Telegram
    steam_id = CharField(unique=True, null=True)  # Уникальный Steam ID пользователя, может быть пустым

    class Meta:
        database = db


class UserGame(Model):
    """
    Модель для хранения информации о играх пользователей.
    """
    user = ForeignKeyField(User, backref='games')  # Связь с моделью User, каждая игра принадлежит пользователю
    game_name = CharField()  # Название игры
    playtime_minutes = IntegerField()  # Время игры в минутах
    ordering = IntegerField(default=0)  # Порядковый номер сортировки игр

    class Meta:
        database = db


class CommandHistory(Model):
    """
    Модель для хранения истории команд, отправленных пользователями.
    """
    user = ForeignKeyField(User, backref='commands')  # Связь с моделью User, каждая команда принадлежит пользователю
    command_text = CharField()  # Текст команды
    timestamp = DateTimeField(default=datetime.now)  # Временная метка команды

    class Meta:
        database = db
        order_by = ('-timestamp',)  # Сортировка по убыванию времени


#User.delete().execute()
#UserGame.delete().execute()
#CommandHistory.delete().execute()

#db.drop_tables([User, UserGame, CommandHistory])
# Подключение к базе данных и создание таблиц, если они не существуют
db.connect()
db.create_tables([User, UserGame, CommandHistory])
print("Таблицы созданы и приложение готово к работе.")


def clear_database():
    """
    Очищает базу данных от всех записей пользователей и игр.
    """
    with db.atomic():
        UserGame.delete().execute()
        User.delete().execute()
        print("База данных очищена")


def schedule_database_clearing():
    """
    Устанавливает расписание для очистки базы данных в 00:00, 12:00 и 18:00.
    """
    schedule.every().day.at("00:00").do(clear_database)
    schedule.every().day.at("12:00").do(clear_database)
    schedule.every().day.at("18:00").do(clear_database)
