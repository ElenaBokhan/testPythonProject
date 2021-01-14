from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Articles


class ArticlesForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={'placeholder': 'Заголовок'}),
            'anons': TextInput(attrs={'placeholder': 'Анонс новости'}),
            'full_text':  Textarea(attrs={'placeholder': 'Содержание'}),
            'date': DateTimeInput(attrs={'placeholder': 'Дата добавления'}),
        }
