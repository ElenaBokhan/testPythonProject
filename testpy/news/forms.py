from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={'placeholder': 'Title article'}),
            'anons': TextInput(attrs={'placeholder': 'Anons article'}),
            'full_text': Textarea(attrs={'placeholder': 'Text article'}),
            'date': DateInput(attrs={'placeholder': 'date of adding'})
        }

