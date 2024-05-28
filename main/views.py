from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm, AddRewiew
from .models import Rewiew
from products.models import Basket


def main(request):
    return render(request, 'main/main.html')

def registrate(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login1')
    else:
        form = UserRegistrationForm()
    content = {'form': form}
    return render(request, 'main/regestration.html', content)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    content = {'form': form}
    return render(request, 'main/avtorizacya.html', content)

def addRewiew(request):
    rewiews = Rewiew.objects.all()
    return render(request, 'main/addrewiew.html', {'rewiews': rewiews})

def rewiew(request):
    form = AddRewiew(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('addRewiew')
    else:
        form = AddRewiew()
    content = {'form': form}
    return render(request, 'main/rewiews.html', content)





