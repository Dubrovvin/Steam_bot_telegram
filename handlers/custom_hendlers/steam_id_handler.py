import requests
from telebot.types import Message
from telebot import TeleBot
from telebot import types
from api.steam_api import steam_info_url, steam_id_url
from database.database_connector import User, UserGame, db
from keyboards.buttons import create_yes_and_no_keyboard
from keyboards.buttons import create_new_and_old_keyboard
from keyboards.buttons import create_next_step_keyboard
from api.telegram_api import MAX_MESSAGE_LENGTH
from handlers.custom_hendlers.game_preference_handler import handle_game_preference
from handlers.custom_hendlers.command_history_handler import record_command
from handlers.default_heandlers import start, help, echo


def search_steam_id(message: Message, bot: TeleBot) -> None:
    """
    Извлекает Steam ID пользователя из введенной ссылки на его профиль в Steam.

    :param message: (Message) Объект сообщения от пользователя с ссылкой на профиль в Steam.
    :param bot: (TeleBot) Экземпляр бота Telegram.
    """

    def request_profile_url(msg: Message):
        bot.send_message(msg.chat.id, 'Введите ссылку на ваш профиль в Steam')
        bot.register_next_step_handler(message, lambda msg: search_steam_id(msg, bot))

    profile_url = message.text.strip()
    vanity_url = extract_vanity_url(profile_url)
    record_command(message, profile_url)

    if not vanity_url:
        bot.send_message(message.chat.id, 'Некорректная ссылка на профиль. Попробуйте еще раз.')
        request_profile_url(message)
        return

    try:
        if int(vanity_url) and len(vanity_url) == 17:
            bot.send_message(message.chat.id, f'Steam ID для пользователя: {vanity_url}')
            handle_steam_id(message, bot, vanity_url)
            return
    except ValueError:
        print('В ссылке нет Steam ID64. Запрашиваем через Steam API')

    url = steam_id_url(vanity_url)

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data)
        if data['response']['success'] == 1:
            steam_id = data['response']['steamid']
            bot.send_message(message.chat.id, f'Steam ID для пользователя: {steam_id}')
            handle_steam_id(message, bot, steam_id)
            return
        else:
            bot.send_message(message.chat.id, f'Не удалось найти Steam ID для пользователя "{vanity_url}". Попробуйте еще раз или введите /cancel, чтобы отменить.')
            bot.register_next_step_handler(message, request_profile_url)

    except requests.exceptions.RequestException as e:
        bot.send_message(message.chat.id, f'Произошла ошибка при выполнении запроса: {e}. Попробуйте еще раз или введите /cancel, чтобы отменить.')
        bot.register_next_step_handler(message, request_profile_url)


def extract_vanity_url(profile_url: str) -> str or None:
    """
    Извлекает vanity URL из ссылки на профиль Steam.

    :param profile_url: (str) Ссылка на профиль в Steam.
    :return: (str or None) Vanity URL профиля Steam, если он найден, иначе None.
    """
    if profile_url.startswith('https://steamcommunity.com/profiles/'):
        parts = profile_url.split('/profiles/')
        if len(parts) == 2:
            steam_id_part = parts[1].strip('/')
            if steam_id_part.isdigit() and len(steam_id_part) == 17:
                return steam_id_part

    elif profile_url.startswith('https://steamcommunity.com/id/'):
        parts = profile_url.split('/id/')
        if len(parts) == 2:
            vanity_url = parts[1].strip('/')
            return vanity_url

    return None


def handle_steam_id(message: Message, bot: TeleBot, steam_id: str) -> None:
    """
    Обрабатывает Steam ID пользователя, загружая список его игр с использованием Steam Web API.

    :param message: (Message) Объект сообщения от пользователя с Steam ID.
    :param bot: (TeleBot) Экземпляр бота Telegram.
    :param steam_id: (str) Steam ID пользователя.
    """
    print(f"Получен запрос на обработку Steam ID: {steam_id}")
    try:
        bot.send_message(message.chat.id, 'Подождите немного, загружаем вашу библиотеку...')
        info_url = steam_info_url(steam_id)
        response = requests.get(info_url)
        data = response.json()

        if response.status_code == 200:
            games = data['response']['games']
            game_info = []
            total_playtime = 0
            user, created = User.get_or_create(telegram_username=message.from_user.username)
            user.steam_id = steam_id
            user.save()
            UserGame.delete().where(UserGame.user == user).execute()

            for game in games:
                playtime_forever = game['playtime_forever']
                game_name = game.get('name', 'Unknown')
                total_playtime += playtime_forever

                UserGame.select().where(UserGame.user == user, UserGame.game_name == game_name).first()
                UserGame.create(user=user, game_name=game_name, playtime_minutes=playtime_forever)

                game_info.append(f'Игра:\t\t{game_name}\nВремя игры:\t{playtime_forever} мин.')

            bot.send_message(message.chat.id, 'Спасибо за ожидание!')

            current_message = 'Список ваших игр в Steam:\n'
            for game_info_str in game_info:
                if len(current_message) + len(game_info_str) > MAX_MESSAGE_LENGTH:
                    bot.send_message(message.chat.id, current_message)
                    current_message = ''
                current_message += game_info_str + '\n'

            if current_message:
                bot.send_message(message.chat.id, current_message)

            total_playtime_hours = total_playtime // 60
            total_playtime_days = total_playtime_hours // 24
            bot.send_message(message.chat.id, f'Общее время игры в Steam: {total_playtime} минут = '
                                              f'{total_playtime_hours} часов = {total_playtime_days} дней')

            keyboard = create_yes_and_no_keyboard()
            bot.send_message(message.chat.id, 'Хочешь добавить свой вариант c другой платформы?',
                             reply_markup=keyboard)
            bot.register_next_step_handler(message, lambda msg: asking_about_new_game(msg, bot))
            return
        else:
            bot.send_message(message.chat.id, 'Ошибка: Не удалось получить данные с сервера Steam.')
    except Exception as exc:
        bot.send_message(message.chat.id, f'Произошла ошибка: проверьте корректность вашего Steam ID {exc}')


def asking_about_new_game(message: Message, bot: TeleBot) -> None:
    """
    Ожидает ответ пользователя на вопрос о добавлении новой игры.

    :param message: (Message) Объект сообщения от пользователя с ответом.
    :param bot: (TeleBot) Экземпляр бота Telegram.
    """
    record_command(message, message.text)
    if message.text == "Да":
        bot.send_message(message.chat.id, 'Введите название игры', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, lambda msg: new_game(msg, bot))
    elif message.text == "Нет":
        bot.send_message(message.chat.id, 'Список игр составлен.', reply_markup=types.ReplyKeyboardRemove())
        keyboard = create_next_step_keyboard()
        bot.send_message(message.chat.id, 'Переходим к шагу выбора приоритета?', reply_markup=keyboard)
        bot.register_next_step_handler(message, lambda msg: asking_about_next_step(msg, bot))


def new_game(message: Message, bot: TeleBot) -> None:
    """
    Обрабатывает запрос пользователя на добавление новой игры.

    :param message: (Message) Объект сообщения от пользователя с названием новой игры.
    :param bot: (TeleBot) Экземпляр бота Telegram.
    """
    game_name = message.text.strip()

    user, created = User.get_or_create(telegram_username=message.from_user.username)
    existing_game = UserGame.select().where(UserGame.user == user, UserGame.game_name == game_name).first()

    if existing_game:
        bot.send_message(message.chat.id, f'Игра "{game_name}" уже добавлена в ваш список.')
        bot.send_message(message.chat.id, 'Хотите добавить другую игру?', reply_markup=create_yes_and_no_keyboard())
        bot.register_next_step_handler(message, lambda msg: asking_about_new_game(msg, bot))
        record_command(message, f'{message.text}')
        return

    keyboard = create_new_and_old_keyboard()
    bot.send_message(message.chat.id, f'Это новая игра, в которую вы хотите поиграть, или любимая игра с другой платформы?',
                     reply_markup=keyboard)
    record_command(message, f'{message.text}')
    bot.register_next_step_handler(message, lambda msg: add_game(msg, bot, user, game_name))


def add_game(message: Message, bot: TeleBot, user: User, game_name: str) -> None:
    """
    Обрабатывает запрос пользователя на добавление игры в базу данных.

    :param message: (Message) Объект сообщения от пользователя с выбором типа игры (новая или любимая).
    :param bot: (TeleBot) Экземпляр бота Telegram.
    :param user: (User) Объект пользователя, для которого добавляется игра.
    :param game_name: (str) Название игры, которую пользователь хочет добавить.
    """
    try:
        if message.text == 'Новая':
            UserGame.create(user=user, game_name=game_name, playtime_minutes=0)
        elif message.text == 'Любимая':
            UserGame.create(user=user, game_name=game_name, playtime_minutes=99999999)

        bot.send_message(message.chat.id, f'Игра "{game_name}" успешно добавлена!', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Хотите добавить ещё игру?', reply_markup=create_yes_and_no_keyboard())
        record_command(message, message.text)
        bot.register_next_step_handler(message, lambda msg: asking_about_new_game(msg, bot))
    except Exception as exc:
        bot.send_message(message.chat.id, f'Произошла ошибка при добавлении игры: {exc}')


def asking_about_next_step(message: Message, bot: TeleBot) -> None:
    """
    Ожидает ответ пользователя на вопрос о следующем шаге в работе бота.

    :param message: Объект сообщения от пользователя с ответом.
    :param bot: Экземпляр бота Telegram.
    """
    print(message.text)
    record_command(message, message.text)
    if message.text == 'Выбирать приоритет игр':
        bot.send_message(message.chat.id, 'Хорошо, приступим', reply_markup=types.ReplyKeyboardRemove())
        handle_game_preference(message, bot)
    elif message.text == 'Начать заново':
        bot.send_message(message.chat.id, 'Давайте попробуем ещё раз', reply_markup=types.ReplyKeyboardRemove())
        start.bot_start(message, bot)
    elif message.text == 'Помощь':
        bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=types.ReplyKeyboardRemove())
        help.bot_help(message, bot)
