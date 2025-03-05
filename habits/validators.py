from rest_framework.exceptions import ValidationError


def validate_habit(habit):
    # Проверка, что заполнено только одно из полей вознаграждение или связанная привычка
    if habit.reward and habit.linked_habit:
        raise ValidationError(
            "Нельзя одновременно указать вознаграждение и связанную привычку."
        )

    # Проверка, что время выполнения не превышает 120 секунд
    if habit.duration > 120:
        raise ValidationError("Время выполнения не должно превышать 120 секунд.")

    # Проверка, что связанная привычка является приятной привычкой
    if habit.linked_habit and not habit.linked_habit.is_pleasant:
        raise ValidationError("Связанная привычка должна быть приятной привычкой.")

    # Проверка, что приятная привычка не имеет вознаграждения или связанной привычки
    if habit.is_pleasant and (habit.reward or habit.linked_habit):
        raise ValidationError(
            "Приятная привычка не может иметь вознаграждения или связанной привычки."
        )

    # Проверка, что привычка выполняется не реже, чем 1 раз в 7 дней
    if habit.periodicity > 7:
        raise ValidationError(
            "Привычка должна выполняться не реже, чем 1 раз в 7 дней."
        )
