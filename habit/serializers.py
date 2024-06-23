from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор модели привычки.
    """
    class Meta:
        model = Habit
        fields = '__all__'
