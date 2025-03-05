from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """APIView для создания пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Создание пользователя."""
        password = serializer.validated_data.get("password")
        user = serializer.save(is_active=True)
        user.set_password(password)
        user.save()
