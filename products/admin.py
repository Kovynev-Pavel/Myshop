from .models import Product, ProductCategory, Basket
from django.contrib import admin

#Регистрация баз дынных в админ панель
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)
