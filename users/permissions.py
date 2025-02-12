from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Класс для проверки разрешений."""

    def has_object_permission(self, request, view, obj):
        """Проверка разрешений."""
        if request.method == "GET":
            return True
        return obj.user == request.user
