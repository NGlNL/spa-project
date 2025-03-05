from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from .models import Habit


class HabitTestCase(APITestCase):
    """Тестовый класс для HabitViewSet."""

    def setUp(self):
        """Настраивает тестовую среду перед выполнением тестов."""
        self.user = User.objects.create_user(
            email="testuser@example.com", password="testpassword"
        )
        self.habit = Habit.objects.create(
            action="Test Habit",
            time="15:00:00",
            place="Test Place",
            duration=120,
            user=self.user,
            is_public=False,
            reward="reward",
            is_pleasant=False,
        )

    def test_update_habit(self):
        """Тестирование обновления привычки"""
        self.client.force_authenticate(user=self.user)
        url = f"/habits/{self.habit.id}/"
        data = {
            "action": "New Habit",
            "time": "11:00:00",
            "place": "Test Place",
            "duration": 120,
            "is_public": False,
            "reward": "reward",
            "is_pleasant": False,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        """Тестирование создания привычки"""
        self.client.force_authenticate(user=self.user)
        url = "/habits/"
        data = {
            "action": "New Habit",
            "time": "11:00:00",
            "place": "Test Place",
            "duration": 120,
            "is_public": False,
            "reward": "reward",
            "is_pleasant": False,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)
        new_habit = Habit.objects.get(action="New Habit")
        self.assertEqual(new_habit.user, self.user)
        self.assertEqual(new_habit.action, "New Habit")
        self.assertEqual(new_habit.place, "Test Place")
        self.assertEqual(new_habit.duration, 120)
        self.assertFalse(new_habit.is_public)
        self.assertEqual(new_habit.reward, "reward")
        self.assertFalse(new_habit.is_pleasant)

    def test_list_habit(self):
        """Тестирование получения списка привычек"""
        self.client.force_authenticate(user=self.user)
        url = "/habits/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.count(), 1)

    def test_public_habit(self):
        """Тестирование получения публичных привычек"""
        self.client.force_authenticate(user=self.user)
        url = "/habits/public/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.count(), 1)
