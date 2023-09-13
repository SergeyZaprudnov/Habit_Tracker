from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя.
       Для создания необходимо ввести логин, пароль и логин Telegram."""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
