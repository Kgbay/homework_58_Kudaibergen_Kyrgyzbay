from django.db import models
from django.utils import timezone


class Task(models.Model):
    summary = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Краткое описание")
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name="Полное описание")
    status = models.ForeignKey(
        'tracker.Status',
        related_name='statuses',
        on_delete=models.CASCADE,
        verbose_name='Статус'
    )
    type = models.ForeignKey(
        'tracker.Type',
        related_name='types',
        on_delete=models.CASCADE,
        verbose_name='Тип'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создание"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=True,
        default=False)
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.summary}, {self.status}, {self.type}"