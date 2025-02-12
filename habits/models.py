from django.db import models


class Habit(models.Model):
    """Модель привычки"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=255, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    linked_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
    )
    periodicity = models.IntegerField(default=1, verbose_name="Периодичность")
    reward = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Вознаграждение"
    )
    duration = models.IntegerField(default=0, verbose_name="Длительность")
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")
    last_performed = models.DateTimeField(
        null=True, blank=True, verbose_name="Последнее выполнение"
    )

    objects = models.Manager()

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return (
            f"{'Приятная' if self.is_pleasant else 'Полезная'} привычка\n"
            f"Я буду {self.action} в {self.place} в {self.time}"
        )
