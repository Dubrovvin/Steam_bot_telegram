Dubrovvin`s_chat_bot

1. Описание
    - Бот для поиска игры на вечер исходя из предпочтения(новая игра или из перечня любимых) и перечня
    имеющихся игр в библиотеке Steam.

2. Начало работы
2.1 Установка
    Для работы с ботом требуется наличие следующих компонентов:
    - Python 3.12 (или более поздняя версия)
    - Установка необходимых библиотек, указанных в файле requirements.txt, выполнив команду:
    pip install -r requirements.txt
2.2 Настройка бота
    Для настройки бота выполните следующие шаги:
    - Получите токен Telegram бота, используя @BotFather.
    - При необходимости настройте доступ к Steam API для получения данных о пользователях.

3. Использование бота
3.1 Основные команды
    - '/start' - начало работы с ботом
    - '/help' - информация по работе бота
3.2 Процесс работы с ботом
    - Спрашивает у пользователя о желании поиграть.
    - Запрашивает Steam ID пользователя для загрузки списка игр.
    - Предлагает выбор ориентации на часто играемые или непроигранные игры.
    - Отправляет сообщение о загрузке базы игр.
    - При наличии 2ух и более желающих, отправляет участникам предложение посмотреть актуальный список
3.3. Организация игр
    - Бот находит общие игры с другими пользователями, учитывая приоритеты игр в списках пользователей.

4. Пример диалога
    Пользователь:   /start
    Бот:            Привет, 'Пользователь'! Хочешь сегодня поиграть?
    Пользователь:   Да, конечно!
    Бот:            Отлично! Пожалуйста, отправь свой Steam ID для загрузки списка игр.
    Пользователь:   123456789
    Бот:            Хочешь поиграть в свои любимые игры или попробуем что-то из забытых игр твоей библиотеки?
    Пользователь:   Любимые игры(более 5 часов в игре)
    Бот:            Загружаю список игр для 'Пользователь'...

5. Заключение
    - Бот предназначен для удобной организации игровых сессий среди пользователей Telegram на основе данных из Steam.