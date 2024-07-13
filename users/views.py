from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.paginations import UsersPaginator
from users.permissions import IsUser
from users.serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):
    """
    Класс список пользователей.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = UsersPaginator


class UserCreateAPIView(generics.CreateAPIView):
    """
    Класс создания пользователя.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс - логин.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsUser)


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Изменить пользователя.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsUser,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление пользователя.
    """

    queryset = User.objects.all()
    permission_classes = (IsUser,)
