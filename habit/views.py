from rest_framework import generics

from habit.models import Habit
from habit.serializers import HabitSerializer
from users.permissions import IsUser


class HabitListAPIView(generics.ListAPIView):
    """
    Класс просмотра привычки.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Класс создания привычки.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        """
        Привязка привычки к пользователю.
        :param serializer:
        :return:
        """
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс просмотра подробностей привычки.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Класс изменения привычки.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = IsUser

    def perform_create(self, serializer):
        """
        Привязка привычки к пользователю.
        :param serializer:
        :return:
        """
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Класс удаления привычки.
    """
    queryset = Habit.objects.all()
    permission_classes = IsUser
