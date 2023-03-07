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

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['summary'] == cleaned_data['description']:
            raise ValidationError("Краткое и полное описание задачи не должны совпадать")
        if len(cleaned_data['summary']) < 2 or len(cleaned_data['description']) < 2:
            raise ValidationError("Длина поле должна быть больше двух символов")
        return cleaned_data
