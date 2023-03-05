from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW = ('New', 'Новый')
    IN_PROGRESS = ('In progress', 'В процессе')
    DONE = ('Done', 'Выполнено')

class Status(models.Model):
    status_name = models.CharField(
        max_length=20,
        choices=StatusChoice.choices,
        default=StatusChoice.NEW,
        null=False,
        verbose_name='Наименование статуса')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создание"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    def __str__(self):
        return f"{self.status_name}"
