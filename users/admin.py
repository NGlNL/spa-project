from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для работы с пользователями в админке."""

    list_filter = ("id", "email")
