from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """
    Класс тестирование пользователя
    """
    def setUp(self) -> None:
        self.user = User.objects.create(email="testoff@mail.ru", password="llleike11")
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """
        Тест регистрация пользователя
        """
        data = {
            "email": "test_1@mail.ru",
            "password": "qwe123",
        }
        response = self.client.post("/register/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.all().exists())
