from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Rewiew, Users
from django import forms

class UserLoginForm(AuthenticationForm):  # Форма авторизации
    username = forms.CharField(widget=forms.TextInput(attrs={  # input для ввода имени пользователя
        'class': 'form control py-4',  # Атрибуты поля
        'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={  # input для ввода пароля
        'class': 'form control py-4',
        'placeholder': 'Введите пароль'}))

    class Meta:
        model = Users  # Модель, нужная для работы с формой
        fields = ('username', 'password')  # Поля, нужные для работы с формой

class UserRegistrationForm(UserCreationForm):  # Форма регистрации
    username = forms.CharField(widget=forms.TextInput(attrs={  # input для ввода имени пользователя
        'class': 'form control py-4',  # Атрибуты поля
        'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={  # input для ввода эл. почты
        'class': 'form control py-4',
        'placeholder': 'Введите почту'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={  # input для ввода пароля
        'class': 'form control py-4',
        'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={  # input для подтверждения пароля
        'class': 'form control py-4',
        'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = Users  # Модель, нужная для работы
        fields = ('username', 'email', 'password1', 'password2')


class AddRewiew(forms.ModelForm):  # Форма добавления отзывов
    first_name = forms.CharField(widget=forms.TextInput(attrs={  # input для ввода имени
        'class': 'form control py-4',  # Атрибуты поля
        'placeholder': 'Введите имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={  # input для ввода эл. почты
        'class': 'form control py-4',
        'placeholder': 'Введите почту'}))
    content = forms.CharField(widget=forms.Textarea(attrs={  # textarea для ввода отзыва
        'class': 'form control py-4',
        'placeholder': 'Введите отзыв'}))

    class Meta:
        model = Rewiew  # Модель, нужная для работы с формой
        fields = {'first_name', 'email', 'content'}  # Поля, нужные для работы с формой
