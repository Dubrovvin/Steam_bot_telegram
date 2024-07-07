Dubrovvin`s_chat_bot

1. Описание проекта

    Этот проект представляет собой Telegram-бота, который помогает пользователям находить игры на основе их
    предпочтений. Он интегрируется с Steam API для получения информации о играх пользователя и предлагает пользователю
    выбрать игры для добавления в список предпочтений.

2. Как пользоваться

    Бот поддерживает следующие команды:

    /start - Начало взаимодействия с ботом. Загружает данные пользователя и предлагает выбрать, хочет ли пользователь
    поиграть сегодня.
    /preference - Выбор приоритета игр (новые или любимые).
    /history - Показывает историю последних запросов.
    /users - Показывает список всех желающих поиграть.
    /help - Показывает справку по доступным командам.

3. Примеры
    3.1 Пример диалога

        Пользователь: /start
        Бот: Привет, [Имя пользователя]! Хочешь сегодня поиграть?
        (Бот отображает клавиатуру с вариантами ответа)

        Пользователь: Да, конечно!
        Бот: Отлично! Пожалуйста, отправь ссылку на свой профиль в Steam для загрузки списка игр.
        (Пользователь отправляет ссылку на профиль)

        Пользователь: https://steamcommunity.com/id/your_steam_profile
        Бот: Загружаю список игр для [Имя пользователя]...
        (Бот загружает список игр пользователя)

        Пользователь: Любимые игры
        Бот: Формирую список твоих любимых игр (игр, в которые ты провел более 5 часов)...
        (Бот обрабатывает выбор пользователя)

        Пользователь: (Бот выводит список игр)
        (Пользователь просматривает список и делает выбор)

        Далее бот может предложить пользователю добавить новую игру или перейти к выбору приоритета игр.

    3.2 Пример url запроса API:

        "http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={config.STEAM_API_KEY}&'steamid={id}&include_appinfo=true&include_played_free_games=true&l=ru&format=json"

    3.3 Пример ответа:

        data = {
                'response': {
                             'game_count': 45, 'games': [{
                                                           'appid': 24240,
                                                           'name': 'PAYDAY: The Heist',
                                                           'playtime_forever': 2609,
                                                           'img_icon_url': 'a07ceea8808f1a2104ed1c864756f263ec67df49',
                                                           'has_community_visible_stats': True,
                                                           'playtime_windows_forever': 0,
                                                           'playtime_mac_forever': 0,
                                                           'playtime_linux_forever': 0,
                                                           'playtime_deck_forever': 0,
                                                           'rtime_last_played': 1444183341,
                                                           'has_leaderboards': True,
                                                           'playtime_disconnected': 0
                                                           },
                                                           {
                                                           'appid': 55230,
                                                           'name': 'Saints Row: The Third',
                                                           'playtime_forever': 3533,
                                                           'img_icon_url': 'ec83645f13643999e7c91da75d418053d6b56529',
                                                           'has_community_visible_stats': True,
                                                           'playtime_windows_forever': 4,
                                                           'playtime_mac_forever': 0,
                                                           'playtime_linux_forever': 0,
                                                           'playtime_deck_forever': 0,
                                                           'rtime_last_played': 1586738091,
                                                           'content_descriptorids': [5],
                                                           'playtime_disconnected': 0
                                                           }]
                             }
                }

    3.4 Пример url запроса API:

       "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={config.STEAM_API_KEY}&vanityurl={name}"

    3.5 Пример ответа:

        data = {
                'response': {
                             'steamid': '76561198073890670',
                             'success': 1
                             }
                }
    3. Как запустить

4. Для запуска проекта на своем ПК выполните следующие шаги:

    3.1 Установка зависимостей:

        Убедитесь, что у вас установлен Python 3.
        Установите необходимые библиотеки, выполнив команду:
            Копировать код
            pip install -r requirements.txt

    3.2 Настройка конфигурации:

        Создайте файл config.py и укажите в нем токен вашего Telegram-бота.

    3.3 Запуск бота:

        Запустите файл main.py, который является точкой входа в приложение.
        Запустите файл scheduler.py, для очистки базы данных по расписанию.
        Эти инструкции помогут вам настроить и запустить Telegram-бота для управления игровыми предпочтениями.
