from django.db import models
from main.models import Users
from django.shortcuts import reverse

class ProductCategory(models.Model):  # Модель базы данных с категориями продуктов
    name = models.CharField('Категории', max_length=40, unique=True)

    def __str__(self):  # В названии объекта базы данных будет название категории
        return self.name

    class Meta:  # Имя модели, если 1 категория то используется verbose_name, а если несколько, то verbose_name_plural
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):  # Переход на страницу с продуктами нужной категории
        return reverse('tovars', kwargs={'pk': self.pk})

class Product(models.Model):  # Модель базы данных с продуктами
    image = models.ImageField('Фото', blank=True, upload_to='media/images')
    model = models.CharField('Модель', max_length=40, db_index=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=0)
    categories = models.ManyToManyField('ProductCategory', blank=True, related_name='products')

    def __str__(self):  # В названии объекта базы данных будет модель продукта
        return self.model

    class Meta:  # Имя модели, если 1 продукт то используется verbose_name, а если несколько, то verbose_name_plural
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Basket(models.Model):  # Модель базы данных корзины
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Количество', default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:  # Имя модели
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def sum(self):  # Счёт общей стоимости товаров одной модели
        return self.product.price * self.quantity