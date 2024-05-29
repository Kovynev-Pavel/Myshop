from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):  # Модель базы данных с пользователями
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    class Meta: # Имя модели, если 1 пользователь то используется verbose_name, а если несколько, то verbose_name_plural
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Rewiew(models.Model):  # Модель базы данных с отзывами
    email = models.EmailField(verbose_name='Электронная почта', blank=True, max_length=254)
    first_name = models.CharField(verbose_name='Имя', blank=True,  max_length=20)
    content = models.TextField(verbose_name='Отзыв', blank=True, null=True, max_length=500)

    def __str__(self):  # В названии объекта базы данных будет имя пользователя
        return self.first_name

    class Meta:  # Имя модели, если 1 отзыв то используется verbose_name, а если несколько, то verbose_name_plural
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'



