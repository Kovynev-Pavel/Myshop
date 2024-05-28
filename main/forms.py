from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Rewiew, Users
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form control py-4',
        'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form control py-4',
        'placeholder': 'Введите пароль'}))

    class Meta:
        model = Users
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form control py-4',
        'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form control py-4',
        'placeholder': 'Введите почту'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form control py-4',
        'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form control py-4',
        'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = Users
        fields = ('username', 'email', 'password1', 'password2')

class AddRewiew(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form control py-4',
        'placeholder': 'Введите имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form control py-4',
        'placeholder': 'Введите почту'}))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form control py-4',
        'placeholder': 'Введите отзыв'}))

    class Meta:
        model = Rewiew
        fields = {'first_name', 'email', 'content'}

