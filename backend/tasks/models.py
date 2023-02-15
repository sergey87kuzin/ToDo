from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    header = models.CharField(
        verbose_name='Заголовок',
        max_length=70
    )
    text = models.TextField(
        verbose_name='Текст задачи'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='tasks'
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('-id',)

    def __str__(self):
        return self.header
