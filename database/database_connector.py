#Модуль для работы с базой данных SQLite
from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, IntegerField

db = SqliteDatabase('users_games.db')


class User(Model):
    telegram_username = CharField(unique=True)  # Уникальный username пользователя Telegram
    steam_id = CharField(unique=True, null=True)

    class Meta:
        database = db


class UserGame(Model):
    user = ForeignKeyField(User, backref='games')
    game_name = CharField()
    playtime_minutes = IntegerField()

    class Meta:
        database = db


db.connect()
db.create_tables([User, UserGame])
print("Таблицы созданы и приложение готово к работе.")