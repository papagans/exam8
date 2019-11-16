from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='Категория')
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


OCENKA_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Otziv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Автор', related_name='otziv')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='product_otziv')
    description = models.TextField(max_length=400, null=False, blank=False, verbose_name='Отзыв')
    ocenka = models.IntegerField(choices=OCENKA_CHOICES, default=OCENKA_CHOICES[0][0],
                                verbose_name='Оценка')

    def __str__(self):
        return str(self.user)
# Create your models here.
