from loader import load, bot
from telebot.custom_filters import StateFilter


if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    bot = load()
    bot.polling(none_stop=True)
