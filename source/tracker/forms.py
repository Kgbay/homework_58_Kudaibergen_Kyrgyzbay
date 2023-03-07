from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.forms import widgets

from .models import Task

STATUS_CHOICES = (
    ('New', 'Новый'),
    ('In progress', 'В процессе'),
    ('Done', 'Выполнено')
)

TYPE_CHOICES = (
    ('Task', 'Задача'),
    ('Bug', 'Ошибка'),
    ('Enhancement', 'Улучшение')
)


def max_len_validator(string, field):
    if len(string) < 2:
        raise ValidationError(f'{field} должен быть длиннее 2 символов')
    return string

class TaskForm(forms.ModelForm):
    class Meta:

        model = Task
        fields = ('summary', 'description', 'status', 'type')
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'type': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-lg'})
        }
        labels = {
            'summary': 'Краткое описание',
            'status': 'Статус',
            'type': 'Тип',
            'description': 'Полное описание'
        }

    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        max_len_validator(summary, self.Meta.labels['summary'])
        if Task.objects.filter(summary=summary).exists():
            raise ValidationError("Краткое описание уже сужествует")
        return summary

    def clean_description(self):
        description = self.cleaned_data.get("description")
        max_len_validator(description, self.Meta.labels['description'])
