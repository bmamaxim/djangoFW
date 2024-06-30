from django.urls import path
from rest_framework.permissions import AllowAny

from habit.apps import HabitConfig
from habit.views import (
    HabitListAPIView,
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    HomeListAPIView,
)

app_name = HabitConfig.name

urlpatterns = [
    path(
        "", HomeListAPIView.as_view(permission_classes=(AllowAny,)), name="home-habits"
    ),
    path("habits/", HabitListAPIView.as_view(), name="habits"),
    path("create/", HabitCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-view"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit-delete"),
]
