from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import MyPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwnerOrReadOnly


class HabitViewSet(ModelViewSet):
    """ViewSet для работы с привычками."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = MyPagination
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        """Обрабатывает создание привычки."""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Возвращает привычки пользователя."""
        return Habit.objects.filter(user=self.request.user)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[permissions.IsAuthenticatedOrReadOnly],
    )
    def public(self, request):
        """Возвращает публичные привычки."""
        public_habits = Habit.objects.filter(is_public=True)
        page = self.paginate_queryset(public_habits)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(public_habits, many=True)
        return Response(serializer.data)
