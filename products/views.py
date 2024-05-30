from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from main.models import Users

def katalog(request):  # Вывод шаблона страницы с каталогом
    categories = ProductCategory.objects.all()  # Запись категорий в переменную
    return render(request, 'products/katalog.html', context={ #Показ страницы с каталогом, передача словаря с переменной
        'categories': categories,
        }
                )

def products(request, pk):  # Вывод шаблона страницы с продуктами
    categories = ProductCategory.objects.all()  # Запись категорий в переменную
    category = ProductCategory.objects.get(pk=pk)  # категория с нужным индексом
    products = category.products.all() # Запись продуктов нужной категории в переменную
    return render(request, 'products/tovars.html', context={#Показ страницы с продуктами, передача словаря с переменными
        'products': products,
        'category': category,
        'categories': categories
        }
    )

def basket(request):  # Вывод шаблона страницы с корзиной
    baskets = Basket.objects.filter(user=request.user)  # Запись в переменную объектов корзины пользователя
    total_quantity = 0
    for basket in baskets:
        total_quantity = total_quantity + basket.quantity  # кол-во всех продуктов
    context = {
        'baskets': Basket.objects.filter(user=request.user),
        'total_quantity': total_quantity,
    }
    return render(request, 'products/basket.html', context)  # Показ страницы с продуктами, передача словаря

def basket_add(request, product_id):  # Добавление продукта в корзину
    product = Product.objects.get(id=product_id)  # продукт с нужным индексом
    baskets = Basket.objects.filter(user=request.user, product=product)  # Запись в переменную фильтрованных объктов

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])  # Переход на эту же страницу

def basket_remove(request, basket_id):  # Удаление продукта из корзины
    basket = Basket.objects.get(id=basket_id)  # Запись в переменную объекта для удаления
    basket.delete()  # Удаление продукта
    return HttpResponseRedirect(request.META['HTTP_REFERER'])  # Переход на эту же страницу