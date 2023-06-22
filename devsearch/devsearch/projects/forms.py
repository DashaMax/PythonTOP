from django.forms import ModelForm, forms
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'feature_image',
            'description',
            'demo_link',
            'source_link',
            'tags'
        ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input'
            })