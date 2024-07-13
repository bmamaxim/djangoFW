from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="testoff@mail.ru", password="llleike11")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            action="test_test",
        )

    def test_create_habit(self):
        """
        Тест создать привычку.
        :return:
        """
        data = {
            "user": self.user.pk,
            "action": "test",
        }
        response = self.client.post("/habit/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())

    def test_home_list(self):
        """
        Тест список привычек в публичном доступе.
        :return:
        """
        response = self.client.get("/habit/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "count": 0,
                "next": None,
                "previous": None,
                "results": [],
            },
        )

    def test_habit_list(self):
        """
        Список привычек пользователя
        """
        response = self.client.get("/habit/habits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.habit.pk,
                        "action": "test_test",
                        "place": None,
                        "time": None,
                        "duration": None,
                        "periodicity": "daily",
                        "publication_sign": False,
                        "reward": None,
                        "nice_habit": False,
                        "user": self.user.pk,
                        "associated_habit": None,
                    }
                ],
            },
        )

    def test_retrieve_habit(self):
        """
        Тест подробности привычки.
        :return:
        """
        url = reverse("habit:habit-view", args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": self.habit.pk,
                "action": "test_test",
                "place": None,
                "time": None,
                "duration": None,
                "periodicity": "daily",
                "publication_sign": False,
                "reward": None,
                "nice_habit": False,
                "user": self.user.pk,
                "associated_habit": None,
            },
        )

    def test_update_habit(self):
        """
        Тест изменить привычку.
        :return:
        """
        url = reverse("habit:habit-update", args=(self.habit.pk,))
        data = {
            "place": "test",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": self.habit.pk,
                "action": "test_test",
                "place": "test",
                "time": None,
                "duration": None,
                "periodicity": "daily",
                "publication_sign": False,
                "reward": None,
                "nice_habit": False,
                "user": self.user.pk,
                "associated_habit": None,
            },
        )

    def test_delete_habit(self):
        """
        Тест удалить привычку.
        :return:
        """
        url = reverse("habit:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Habit.objects.all().count(), 0)
