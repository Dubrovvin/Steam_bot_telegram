def bot_help(message, bot):
    """Обработчик команды /help."""
    help_text = "Этот бот помогает вам находить игры на основе ваших предпочтений. " \
                "Доступные команды:\n" \
                "/start - начать взаимодействие с ботом\n" \
                "/help - показать эту справку\n" \
                "\n" \

    bot.send_message(message.chat.id, help_text)