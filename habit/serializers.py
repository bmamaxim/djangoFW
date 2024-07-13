from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор модели привычки.
    """

    class Meta:
        model = Habit
        exclude = ("last_try",)
