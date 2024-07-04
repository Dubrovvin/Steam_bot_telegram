import telebot
from keyboards.buttons import create_game_preference_keyboard


def handle_game_preference(message, bot):
    keyboard = create_game_preference_keyboard()
    bot.send_message(message.chat.id, 'Хочешь поиграть в свои любимые игры или попробуем что-то новое?',
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, handle_game_preference_response)

def handle_game_preference_response(message, bot):
    if message.text == 'Предпочту любимые игры':
        bot.send_message(message.chat.id, 'Вы выбрали играть в свои любимые игры.')

    elif message.text == 'Попробовать что-то новое':
        bot.send_message(message.chat.id, 'Вы выбрали попробовать что-то новое.')

    else:
        bot.send_message(message.chat.id, 'Я не понимаю, выберите кнопку.')
