from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    telegram = models.CharField(max_length=200, verbose_name='Телеграмм')
    chat_id = models.CharField(max_length=300, default=None, **NULLABLE, verbose_name='Чат Айди')

    REQUIRED_FIELDS = ['email', 'telegram']
