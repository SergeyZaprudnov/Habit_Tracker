from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Значение переданное пользователем"""
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = '__all__'
