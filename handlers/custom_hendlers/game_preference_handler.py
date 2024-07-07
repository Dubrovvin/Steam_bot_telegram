from api.telegram_api import MAX_MESSAGE_LENGTH
from database.database_connector import UserGame, User
from keyboards.buttons import create_game_preference_keyboard
from telebot import TeleBot, types
from handlers.custom_hendlers.comparison_of_user_games import handle_user_selection


def handle_game_preference(message: types.Message, bot: TeleBot) -> None:
    """
    Обрабатывает сообщение о предпочтениях игр пользователя и отправляет клавиатуру с выбором.

    :param message: Объект сообщения от пользователя Telegram.
    :param bot: Экземпляр бота Telegram.
    """
    keyboard = create_game_preference_keyboard()
    bot.send_message(message.chat.id, 'Хочешь поиграть в свои любимые игры или попробуем что-то новое?',
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, lambda msg: handle_game_preference_response(msg, bot))


def handle_game_preference_response(message: types.Message, bot: TeleBot) -> None:
    """
    Обрабатывает ответ пользователя на вопрос о предпочтениях игр.

    :param message: Объект сообщения от пользователя Telegram.
    :param bot: Экземпляр бота Telegram.
    :return: None
    """
    user = User.get(telegram_username=message.from_user.username)
    games = UserGame.select().where(UserGame.user == user)

    if message.text == 'Предпочту любимые игры':
        bot.send_message(message.chat.id, 'Вы выбрали играть в свои любимые игры.')
        sorted_games = games.order_by(UserGame.playtime_minutes.desc())
    elif message.text == 'Попробовать что-то новое':
        bot.send_message(message.chat.id, 'Вы выбрали попробовать что-то новое.')
        sorted_games = games.order_by(UserGame.playtime_minutes.asc())
    else:
        bot.send_message(message.chat.id, 'Не понимаю вас, выберите кнопку.')
        handle_game_preference(message, bot)
        return

    for i, game in enumerate(sorted_games, start=1):
        game.ordering = i
        game.save()

    game_names = [game.game_name for game in sorted_games]
    current_message = 'Отсортированный список ваших игр:\n'
    for game_name in game_names:
        if len(current_message) + len(game_name) > MAX_MESSAGE_LENGTH:
            bot.send_message(message.chat.id, current_message.strip())
            current_message = ''
        current_message += f'{game_name}\n'

    if current_message:
        bot.send_message(message.chat.id, current_message.strip(), reply_markup=types.ReplyKeyboardRemove())

    handle_user_selection(message, bot)
