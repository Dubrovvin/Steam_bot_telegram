from telebot.types import Message
from telebot import TeleBot
import requests
from config_data import config

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
        url = (f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={config.STEAM_API_KEY}&'
               f'steamid={steam_id}&include_appinfo=true&include_played_free_games=true&l=ru&format=json')
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            games = data['response']['games']
            print(games)
            game_info = []
            for game in games:
                playtime_forever = game['playtime_forever']
                game_name = game.get('name', 'Unknown')
                game_info.append(f'Игра: {game_name}, Время игры: {playtime_forever} мин.')
            bot.send_message(message.chat.id, 'Спасибо за ожидание!')
            game_names = [game['name'] for game in games]
            game_info_str = "\n".join(game_names)
            bot.send_message(message.chat.id, f'Список ваших игр в Steam:\n{game_info_str}')
        else:
            bot.send_message(message.chat.id, 'Ошибка: Не удалось получить данные с сервера Steam.')

    except Exception as exc:
        bot.send_message(message.chat.id, f'Произошла ошибка: проверьте корректность вашего Steam ID')
