from django.urls import path
from . import views

urlpatterns = [
    path('katalog', views.katalog, name='katalog'),
    path('basket', views.basket, name='basket'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    path('category/<int:pk>/', views.products, name='tovars'),
]