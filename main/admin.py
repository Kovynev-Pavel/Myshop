from .models import Rewiew, Users
from django.contrib import admin

#Регистрация баз дынных в админ панель
admin.site.register(Users)
admin.site.register(Rewiew)