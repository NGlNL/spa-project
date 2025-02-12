from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Habit."""

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        """Проверка валидности данных."""
        habit = Habit(**data)
        validate_habit(habit)
        return data
