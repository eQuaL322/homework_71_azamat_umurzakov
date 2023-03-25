from django import forms
from django.contrib.auth import get_user_model

from accounts.models import GenderChoices


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя или эл. адрес'}))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='',
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )
    password_confirm = forms.CharField(
        label='',
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}),
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'password', 'password_confirm', 'first_name', 'last_name', 'email', 'avatar', 'birth_date',
            'phone', 'sex', 'about_me')
        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'avatar': '',
            'birth_date': '',
            'phone': '',
            'about_me': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'avatar': forms.ClearableFileInput(attrs={'placeholder': 'Аватар'}),
            'birth_date': forms.DateInput(attrs={'placeholder': 'Дата рождения'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'about_me': forms.TextInput(attrs={'placeholder': 'Информация о пользователе'}),
            'sex': forms.Select(attrs={'placeholder': 'Пол'}, choices=GenderChoices.choices),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        # user.group.add('user')
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'avatar', 'birth_date')
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}
