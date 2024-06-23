from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}

class User(AbstractUser):
    """
    Класс модели польлзователя.
    """
    username = None
    email = models.EmailField(unique=True, verbose_name="Элктронная почта", help_text="Укажите электронную почту")
    avatar = models.ImageField(
        upload_to="image/", verbose_name="Изображение", help_text="Аватарка", **NULLABLE
    )
    tg_nick = models.CharField(max_length=200, verbose_name="Телеграмм", help_text="Укажите ник телеграмма", **NULLABLE)
    ver_code = models.CharField(
        max_length=4, verbose_name="Код верификации", help_text="Код верификации", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.email} {self.tg_nick}"
