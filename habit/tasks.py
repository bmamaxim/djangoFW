import datetime
from habit.models import Habit
from django.utils import timezone

from celery import shared_task

from habit.services import send_telegram_message


@shared_task
def send_tg_message():
    """
    Функция проверки отправки сообщений
    с ориентированнием на последнее отправленное сообщение.
    """
    datetime_now = timezone.now()
    time_now = datetime.datetime.now(datetime.timezone.utc)

    habits = Habit.objects.all()
    for habit in habits:
        last_try_date = habit.last_try or datetime_now - datetime.timedelta(
            days=999
        )  # Используем очень старую дату, если нет last_try_date
        send_message = False

        if habit.periodicity == Habit.PERIOD_DAILY:
                send_message = (datetime_now - last_try_date).days >= 1
        elif habit.periodicity == Habit.EVERY_OTHER_DAYS:
                send_message = (datetime_now - last_try_date).days >= 2
        elif habit.periodicity == Habit.WEEKEND:
                send_message = (
                    datetime_now.weekday() in (6, 7)
                    and (datetime_now - last_try_date).days >= 1
                )

        if send_message:
            if time_now.time() >= habit.time:
                chat_id = habit.user.tg_nick
                massage = habit.action
                send_telegram_message(chat_id, massage)
                habit.last_try = datetime_now
                habit.save()
