from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):
    email = forms.EmailField(label='Введите Email', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'}))
    username = forms.CharField(label='Введите логин', required=True,
                               help_text='Нельзя вводить символы: @, /, _',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Логин'}))
    password1 = forms.CharField(label='Введите пароль', required=True,
                                help_text='Пароль не должен быть коротким и простым',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтвердите пароль', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторно введите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Введите Email', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'}))
    username = forms.CharField(label='Введите логин', required=True,
                               help_text='Нельзя вводить символы: @, /, _',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Логин'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileImageForm, self).__init__(*args, **kwargs)
        self.fields['img'].label = 'Изображение профиля'
        self.fields['gender'].label = 'Выберите пол'
        self.fields['accept'].label = 'Соглашение на отправку уведомлений на почту'

    class Meta:
        model = Profile
        fields = ['img', 'gender', 'accept']


