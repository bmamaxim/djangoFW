from rest_framework import generics
from rest_framework.permissions import AllowAny

from habit.models import Habit
from habit.paginations import HabitPaginator
from habit.serializers import HabitSerializer
from habit.permissions import IsUser


class HomeListAPIView(generics.ListAPIView):
    """
    Класс вывода привычек с флагом публичные.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(publication_sign=True)
    permission_classes = (AllowAny,)
    pagination_class = HabitPaginator


class HabitListAPIView(generics.ListAPIView):
    """
    Класс просмотра привычек пользователя.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator


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
    pagination_class = (IsUser,)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Класс изменения привычки.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsUser,)

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
    permission_classes = (IsUser,)
