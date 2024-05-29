from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm, AddRewiew
from .models import Rewiew
from products.models import Basket

def main(request):  # Вывод шаблона главной страницы
    return render(request, 'main/main.html')  # Показ главной страницы

def registrate(request):  # Вывод шаблона страницы с регистрацией, контроллер формы
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():  # Проверка правильности введения данных формы
            form.save()  # Сохранение данных формы в базу данных
            return redirect('login1')  # Переход на страницу с авторизацией
    else:
        form = UserRegistrationForm()  # Запись формы в переменную
    content = {'form': form}  # Запись переменной в словарь
    return render(request, 'main/regestration.html', content)  # Показ страницы с регистрацией, передача словаря

def login(request):  # Вывод шаблона страницы с авторизацией, контроллер формы
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():  # Проверка правильности введения данных формы
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:  # Проверка, есть ли такой пользователь
                auth.login(request, user)  # Авторизация пользователя
                return redirect('home')  # Переход на главную страницу
    else:
        form = UserLoginForm()  # Запись формы в переменную
    content = {'form': form}  # Запись переменной в словарь
    return render(request, 'main/avtorizacya.html', content)  # Показ страницы с авторизацией, передача словаря

def addRewiew(request):  # Вывод шаблона страницы с отзывами
    rewiews = Rewiew.objects.all()  # Запись данных отзывов в перменную
    return render(request, 'main/addrewiew.html', {'rewiews': rewiews}) # Показ страницы с отзывами, передача переменной

def rewiew(request):  # Вывод шаблона страницы с добавлением отзыва, контроллер формы
    form = AddRewiew(data=request.POST)
    if form.is_valid():  # Проверка правильности введения данных формы
        form.save()  # Сохранение данных формы в базу данных
        return redirect('addRewiew')  # Переход на страницу с отзывами
    else:
        form = AddRewiew()  # Запись формы в переменную
    content = {'form': form}  # Запись переменной в словарь
    return render(request, 'main/rewiews.html', content)  # Показ страницы с добавлением отзыва, передача словаря