#Модуль для работы с базой данных SQLite
from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, IntegerField, DateTimeField
from datetime import datetime

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


class CommandHistory(Model):
    user = ForeignKeyField(User, backref='commands')
    command_text = CharField()
    timestamp = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        order_by = ('-timestamp',)

#User.delete().execute()
#UserGame.delete().execute()
#CommandHistory.delete().execute()
db.connect()
db.create_tables([User, UserGame, CommandHistory])
print("Таблицы созданы и приложение готово к работе.")
