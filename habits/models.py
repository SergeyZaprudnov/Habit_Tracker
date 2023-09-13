from django.db import models

from users.models import User, NULLABLE


class Habit(models.Model):
    """Model description"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=200, verbose_name='Место')
    time = models.DateTimeField(verbose_name='Время')
    action = models.CharField(max_length=250, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная привычка')
    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Связанная привычка')

    frequency = models.ImageField(default=1, verbose_name='Частота')
    reward = models.CharField(max_length=250, **NULLABLE, verbose_name='Награда')

    execution_time = models.ImageField(**NULLABLE, verbose_name='Время выполнения')
    is_public = models.BooleanField(default=False, verbose_name='Является общедоступным')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
