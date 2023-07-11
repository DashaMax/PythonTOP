from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Blog


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'slug',
            'content',
            'photo',
            'is_published',
            'cat',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-input'
                }
            ),
            'slug': forms.TextInput(
                attrs={
                    'class': 'form-input'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'cols': 60,
                    'rows': 10,
                    'class': 'form-input'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) > 100:
            raise ValidationError('Len > 100')

        return title


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={
            'class': 'form-input'
        }
    ))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(
        attrs={
            'class': 'form-input'
        }
    ))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-input'
        }
    ))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={
            'class': 'form-input'
        }
    ))
