from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'specialty', 'rating']
        labels = {
            'name': 'Ваше имя',
            'email': 'Email',
            'message': 'Сообщение',
            'specialty': 'Какую специальность вы бы выбрали?',
            'rating': 'Оцените сайт (от 1 до 10)'
        }
        help_texts = {
            'message': 'Поделитесь мнением о сайте, дополните любыми идеями.'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@mail.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Напишите ваше сообщение...'
            }),
            'specialty': forms.Select(attrs={
                'class': 'form-select'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10
            })
        }