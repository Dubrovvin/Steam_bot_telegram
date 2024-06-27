
def handle_hello(message, bot):
    text = "Привет!"
    bot.send_message(message.chat.id, text)
