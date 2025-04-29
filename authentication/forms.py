from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from authentication.models import User


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
            'username': forms.TextInput(attrs={'placeholder': 'Введите логин'}),
            'email': forms.TextInput(attrs={'placeholder': 'Введите email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Введите логин'}),
            'password': forms.TextInput(attrs={'placeholder': 'Введите пароль'}),
        }
