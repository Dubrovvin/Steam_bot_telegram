from telebot.types import Message
from database.database_connector import User, UserGame, CommandHistory, db
from telebot import TeleBot


def handle_history_command(message: Message, bot: TeleBot) -> None:
    user = User.get(User.telegram_username == message.from_user.username)
    history_commands = (CommandHistory.select().where(CommandHistory.user == user).limit(10).
                       order_by(CommandHistory.timestamp.desc()))
    if history_commands:
        history_text = 'Последние команды:\n'
        for command in history_commands:
            history_text += f'{command.timestamp.strftime("%Y-%m-%d %H:%M:%S")} - {command.command_text}\n'

        bot.send_message(message.chat.id, history_text)
    else:
        bot.send_message(message.chat.id, 'У вас пока нет истории команд.')


def record_command(message, command_text):
    try:
        user = User.get(User.telegram_username == message.from_user.username)
        CommandHistory.create(user=user, command_text=command_text)
    except User.DoesNotExist:
        print(f"Пользователь с именем '{message.from_user.username}' не найден.")