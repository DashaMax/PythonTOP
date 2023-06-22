from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User, Profile, Skill


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'username',
            'password1',
            'password2',
        ]
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input'
            })


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'email',
            'username',
            'short_info',
            'bio',
            'profile_image',
            'social_github',
            'social_youtube',
            'social_website'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input'
            })


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = [
            'owner',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input'
            })