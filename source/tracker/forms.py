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

    # summary = forms.CharField(max_length=100, required=True, label='Краткое описание')
    # status = forms.ChoiceField(required=True, label='Статус', choices=STATUS_CHOICES)
    # type = forms.ChoiceField(required=True, label='Тип', choices=TYPE_CHOICES)
    # description = forms.CharField(max_length=3000, required=False, label='Полное описание',
    #                               widget=widgets.Textarea)
    #
    #
    # summary.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Краткое описание'})
    # description.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Полное описание'})
    # status.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Статус'})
    # type.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Тип'})

    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        if len(summary) < 2:
            raise ValidationError("Краткое описание меньше 2 символов")
        if Task.objects.filter(summary=summary).exists():
            raise ValidationError("Краткое описание уже сужествует")
        return summary

