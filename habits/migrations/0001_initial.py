# Generated by Django 5.1.4 on 2025-02-05 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=100, verbose_name="Место")),
                ("time", models.TimeField(verbose_name="Время")),
                ("action", models.CharField(max_length=255, verbose_name="Действие")),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False, verbose_name="Приятная привычка"
                    ),
                ),
                (
                    "periodicity",
                    models.IntegerField(default=1, verbose_name="Периодичность"),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "duration",
                    models.IntegerField(default=0, verbose_name="Длительность"),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="Публичная привычка"
                    ),
                ),
                (
                    "last_performed",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Последнее выполнение"
                    ),
                ),
                (
                    "linked_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
