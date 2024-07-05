from database.database_connector import User, UserGame, CommandHistory
from peewee import fn
from datetime import datetime, timedelta
from api.telegram_api import MAX_MESSAGE_LENGTH
from peewee import JOIN

def handle_user_selection(message, bot):
    # Определяем время неактивности (6 часов)
    all_games = UserGame.select(UserGame.game_name).distinct()

    # Получаем список всех пользователей
    all_users = User.select(User.id)

    # Список для хранения средних значений ordering и названий игр
    average_orderings = []

    # Для каждой игры проверяем, есть ли она у всех пользователей
    for game in all_games:
        game_name = game.game_name
        users_with_game = (
            User
            .select()
            .join(UserGame, JOIN.LEFT_OUTER)
            .where(UserGame.game_name == game_name)
        )

        if users_with_game.count() == all_users.count():
            # Вычисляем среднее значение ordering для текущей игры
            avg_ordering = (
                UserGame
                .select(fn.AVG(UserGame.ordering).alias('avg_ordering'))
                .where(UserGame.game_name == game_name)
                .scalar()
            )

            # Добавляем в список результатов
            average_orderings.append((game_name, avg_ordering))

    # Сортируем по возрастанию среднего значения ordering
    average_orderings_sorted = sorted(average_orderings, key=lambda x: x[1])

    bot.send_message(message.chat.id, f'Актуальный список игр для активных участвников ():')

    sequence_number = 0
    for game_name, avg_ordering in average_orderings_sorted:
        sequence_number += 1
        bot.send_message(message.chat.id, f'{sequence_number}. {game_name}')
