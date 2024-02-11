from django import forms
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'author': forms.HiddenInput(),
        }

        def __int__(self, *args, **kwargs):
            super(RecipeForm, self).__init__(*args, **kwargs)
            self.fields['image'].required = True


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное Поле. Добавьте электронную почту')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['login', 'password']
