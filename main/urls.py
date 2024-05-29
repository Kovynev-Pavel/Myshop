from django.urls import path
from . import views

urlpatterns = [  # url адрес страниц приложения main, переход на них
    path('', views.registrate, name='registrate'),  # '' - переход на начальную страницу
    path('login1', views.login, name='login1'),
    path('home', views.main, name='home'),
    path('rewiew', views.rewiew, name='rewiew'),
    path('addRewiew', views.addRewiew, name='addRewiew'),
]