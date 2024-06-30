from django.db import models

from config import settings
from users.models import NULLABLE


class Habit(models.Model):
    """
    Класс модели "привычка".
    """

    PERIOD_DAILY = "daily"
    EVERY_OTHER_DAYS = "every other days"
    WEEKEND = "weekend"

    PERIOD = (
        (PERIOD_DAILY, "Ежедневно"),
        (EVERY_OTHER_DAYS, "Каждые два дня"),
        (WEEKEND, "Выходные"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    action = models.CharField(
        verbose_name="Привычки",
        max_length=500,
        help_text="Опишите свою привычку",
        **NULLABLE,
    )
    place = models.CharField(
        verbose_name="Место",
        max_length=200,
        help_text="Опишите место выполнения",
        **NULLABLE,
    )
    time = models.TimeField(
        verbose_name="Время", help_text="Начало выполнения", **NULLABLE
    )
    duration = models.TimeField(
        verbose_name="Продолжительность", help_text="Время на выполнение", **NULLABLE
    )
    periodicity = models.CharField(
        max_length=50,
        choices=PERIOD,
        default=PERIOD_DAILY,
        verbose_name="Периодичность",
        help_text="Частота выполнения",
        **NULLABLE,
    )
    publication_sign = models.BooleanField(
        verbose_name="Признак публикации",
        help_text="Публикация привычки",
        default=False,
        **NULLABLE,
    )
    associated_habit = models.ForeignKey(
        "self",
        verbose_name="Связзанная привычка",
        help_text="Свяжите привычки",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )
    reward = models.CharField(
        max_length=500,
        verbose_name="Вознаграждение",
        help_text="Награда за выполнение привычки",
        **NULLABLE,
    )
    nice_habit = models.BooleanField(
        verbose_name="Приятная привычка",
        help_text="Выберите приятную привычку",
        default=False,
        **NULLABLE,
    )
    last_try = models.DateTimeField(
        auto_now_add=True, verbose_name="последняя рассылка", **NULLABLE
    )

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"

    def __str__(self):
        return (
            f"{self.user}"
            f"{self.action}"
            f"{self.time}"
            f"{self.associated_habit}"
            f"{self.reward}"
        )
