import schedule
import time
from datetime import datetime
from database.database_connector import User, UserGame, db, CommandHistory


def clear_database():
    """
    Очищает базу данных от всех записей пользователей и игр.
    """
    try:
        with db.atomic():
            UserGame.delete().execute()
            User.delete().execute()
            CommandHistory.delete().execute()
        print("База данных очищена в", datetime.now())
    except Exception as exc:
        print("Ошибка при очистке базы данных:", exc)


def schedule_database_clearing():
    """
    Устанавливает расписание для очистки базы данных в 00:00, 12:00 и 18:00 по московскому времени.
    """
    schedule.every().day.at("00:00").do(clear_database)
    schedule.every().day.at("12:00").do(clear_database)
    schedule.every().day.at("18:00").do(clear_database)


if __name__ == '__main__':
    schedule_database_clearing()

    while True:
        schedule.run_pending()
        time.sleep(1)
