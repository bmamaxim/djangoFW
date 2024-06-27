import requests
import datetime
from config import settings
from habit.models import Habit
from django.utils import timezone


def send_telegram_message(chat_id, message):
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'T{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/s', params=params)


def send_message():
    datetime_now = timezone.now()

    habits = Habit.objects.all()
    for habit in habits:
        last_try_date = habit.last_try_date or datetime_now - datetime.timedelta(days=999)  # Используем очень старую дату, если нет last_try_date
        send_message = False

        if habit.periodicity == Habit.PERIOD_DAILY:
            send_message = (datetime_now - last_try_date).days >= 1
        elif habit.periodicity == Habit.EVERY_OTHER_DAYS:
            send_message = (datetime_now - last_try_date).days >= 2
        elif habit.periodicity == Habit.WEEKEND:
            send_message = datetime_now.weekday() in (5, 6) and (datetime_now - last_try_date).days >= 1

        if send_message:
            _send_mail(habit)
            habit.last_try_date = datetime_now
            habit.save()
