from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

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


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True, label='Краткое описание')
    description = forms.CharField(max_length=3000, required=False, label='Полное описание',
                                  widget=widgets.Textarea)
    status = forms.ChoiceField(required=True, label='Статус', choices=STATUS_CHOICES)
    type = forms.ChoiceField(required=True, label='Тип', choices=TYPE_CHOICES)

    summary.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Краткое описание'})
    description.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Полное описание'})
    status.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Статус'})
    type.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Тип'})

    def clean_title(self):
        summary = self.cleaned_data.get('title')
        if len(summary) < 2:
            raise ValidationError("Загаловок должен быть длиннее 2 символов")
        return summary
