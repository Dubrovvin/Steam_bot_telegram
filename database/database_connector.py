#Модуль для работы с базой данных SQLite
from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, IntegerField

db = SqliteDatabase('users_games.db')


class User(Model):
    username = CharField(unique=True)

    class Meta:
        database = db


class UserGame(Model):
    user = ForeignKeyField(User, backref='games')
    game_name = CharField(unique=True)
    playtime_minutes = IntegerField()

    class Meta:
        database = db

#db.drop_tables([User, UserGame])
db.connect()
db.create_tables([User, UserGame])

