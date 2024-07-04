
def bot_echo(message, bot):
    bot.send_message(message.chat.id, "Я не понимаю вашего сообщения. "
                                      "Пожалуйста, используйте команды или введите /help для справки.")
