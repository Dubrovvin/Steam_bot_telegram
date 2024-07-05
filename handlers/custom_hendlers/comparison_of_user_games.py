from telebot.types import Message
from telebot import TeleBot
from database.database_connector import User, UserGame
from peewee import fn, JOIN


def handle_user_selection(message: Message, bot: TeleBot) -> None:
    """
    Обрабатывает выбор пользователей, выводя список игр, которые есть у всех активных пользователей.

    Функция проверяет, какие игры присутствуют у всех зарегистрированных пользователей
    и выводит их список в порядке возрастания среднего значения позиции (ordering).

    :param message: (Message) Объект сообщения от пользователя.
    :param bot: (TeleBot) Экземпляр бота Telegram.
    """

    # Определяем время неактивности (6 часов)
    all_games = UserGame.select(UserGame.game_name).distinct()

    # Получаем список всех пользователей, у которых есть telegram_username
    all_users = User.select().where(User.telegram_username.is_null(False))

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

    # Формируем строку для списка пользователей
    all_users_str = ', '.join([user.telegram_username for user in all_users])

    bot.send_message(message.chat.id, f'Актуальный список игр для активных участников ({all_users_str}):')

    sequence_number = 0
    for game_name, avg_ordering in average_orderings_sorted:
        sequence_number += 1
        bot.send_message(message.chat.id, f'{sequence_number}. {game_name}')
