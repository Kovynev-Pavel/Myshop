from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Rewiew(models.Model):
    email = models.EmailField(verbose_name='Электронная почта', blank=True, max_length=254)
    first_name = models.CharField(verbose_name='Имя', blank=True,  max_length=20)
    content = models.TextField(verbose_name='Отзыв', blank=True, null=True, max_length=500)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'



