from telebot.handler_backends import State, StatesGroup

user_states_dict = {}


class UserInfoState(StatesGroup):
    users_games = State()
    games_preference = State()