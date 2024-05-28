from django.db import models
from main.models import Users
from django.shortcuts import reverse

class ProductCategory(models.Model):
    name = models.CharField('Категории', max_length=40, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tovars', kwargs={'pk': self.pk})

class Product(models.Model):
    image = models.ImageField('Фото', blank=True, upload_to='media/images')
    model = models.CharField('Модель', max_length=40, db_index=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=0)
    categories = models.ManyToManyField('ProductCategory', blank=True, related_name='products')

    def __str__(self):
        return self.model

class Basket(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Количество', default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('basket_add', kwargs={'pk': self.pk})

    def sum(self):
        return self.product.price * self.quantity


