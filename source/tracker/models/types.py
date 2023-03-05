from django.db import models
from django.db.models import TextChoices


class TypeChoice(TextChoices):
    TASK = ('Task', 'Задача')
    BUG = ('Bug', 'Ошибка')
    ENHANCEMENT = ('Enhancement', 'Улучшение')


class Type(models.Model):
    type_name = models.CharField(
        max_length=20,
        null=False,
        choices=TypeChoice.choices,
        default=TypeChoice.TASK,
        verbose_name='Наименование типа')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создание"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    def __str__(self):
        return f"{self.type_name}"
