from telebot.types import Message
from telebot import TeleBot
import requests
from config_data import config
from api.steam_api import steam_url
from handlers.custom_hendlers.game_preference_handler import handle_game_preference
from states.states import user_states_dict, UserInfoState
from database.database_connector import User, UserGame, db

def handle_steam_id(message: Message, bot: TeleBot) -> None:
    """
    Функция для обработки запроса на получение списка игр пользователя Steam по его Steam ID
    с использованием Steam Web API.

    :param message:(Message): Объект сообщения от пользователя, содержащий Steam ID.
    :param bot:(TeleBot): Экземпляр бота Telegram, используемый для отправки сообщений.
    :return:- None: Функция не возвращает значения, а отправляет сообщения пользователю через бота.
    """
    try:
        bot.send_message(message.chat.id, 'Подождите немного, загружаем вашу библиотеку...')
        steam_id = message.text.strip()
        response = requests.get(steam_url(steam_id))
        data = response.json()

        if response.status_code == 200:
            games = data['response']['games']
            print(games)
            game_info = []

            user, created = User.get_or_create(username=message.from_user.username)
            UserGame.delete().where(UserGame.user == user).execute()

            for game in games:
                playtime_forever = game['playtime_forever']
                game_name = game.get('name', 'Unknown')
                game_info.append(f'Игра: {game_name}, Время игры: {playtime_forever} мин.')

                UserGame.create(user=user, game_name=game_name, playtime_minutes=playtime_forever)

            bot.send_message(message.chat.id, 'Спасибо за ожидание!')
            game_names = [game['name'] for game in games]
            game_info_str = "\n".join(game_names)
            bot.send_message(message.chat.id, f'Список ваших игр в Steam:\n{game_info_str}')

            #текущее состояние базы данных (для отладки)
            print('Текущее состояние базы данных')
            for user in User.select():
                print(f'Пользователь: {user.username}')
                for game in user.games:
                    print(f'Игра: {game.game_name}, Время игры: {game.playtime_minutes} минут')

        else:
            bot.send_message(message.chat.id, 'Ошибка: Не удалось получить данные с сервера Steam.')

    except Exception as exc:
        bot.send_message(message.chat.id, f'Произошла ошибка: проверьте корректность вашего Steam ID{exc}')
