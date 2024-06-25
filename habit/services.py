import requests
import datetime
from config import settings
from habit.models import Habit


def send_telegram_message(chat_id, message):
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'T{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/s', params=params)


def send_massage():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)
    for massage in Habit.objects.filter(periodicity=Habit.PERIOD_DAILY):
        if massage.periodicity == Habit.PERIOD_DAILY:
              if (datetime_now - last_try_date).days >= 1: # от сюда прекратил реализацию функции
                            _send_mail(mailing_letters, mailing_client)
                    elif mailing_letters.period == MailingLetters.PERIOD_WEEKLY:
                        if (datetime_now - last_try_date).days >= 7:
                            _send_mail(mailing_letters, mailing_client)
                    elif mailing_letters.period == MailingLetters.PERIOD_MONTHLY:
                        if (datetime_now - last_try_date).days >= 28:
                            _send_mail(mailing_letters, mailing_client)
                else:
                    _send_mail(mailing_letters, mailing_client)