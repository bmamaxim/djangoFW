from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from habit.models import Habit
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор модели Пользователя
    """

    habit = SerializerMethodField()

    def get_habit(self, user):
        """
        Метод выводит количество привычек пользователя
        """
        return Habit.objects.filter(user=user).count()

    class Meta:
        model = User
        fields = (
            "first_name",
            "tg_nick",
            "email",
            "habit",
            "password",
        )
