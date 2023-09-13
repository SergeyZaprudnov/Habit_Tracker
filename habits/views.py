from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.pagination import HabitsPagination
from habits.permissions import IsOwnerPermission
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создать привычки.
       Для создания необходимо ввести (как минимум) место, время и действие."""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Просмотр списка привычек (возвращает только ваши собственные привычки).
       Имеет нумерацию страниц."""
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """Получить список привычек (возвращает только общедоступные привычки)."""
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitDetailAPIView(generics.RetrieveAPIView):
    """Получить конкретную привычку по ее идентификатору (возвращает только ваши собственные привычки)."""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Обновить привычку по ее идентификатору (вы можете обновить только свои собственные привычки)."""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Удаление привычки по ее идентификатору (удалить можно только свою привычку)."""
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
