from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


class AddItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Item
        fields = ['title', 'slug', 'description',
                  'photo', 'is_active', 'cat'
                  ]
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длинна превышает 200 симмволов')

        return title


class RegisterUserForm(UserCreationForm):
    pass


class LoginUserForm(AuthenticationForm):
    pass


class ContactForm(forms.Form):
    pass