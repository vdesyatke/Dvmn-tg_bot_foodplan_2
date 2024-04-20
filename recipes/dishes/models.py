from django.db import models
from django.conf import settings

class Dishes(models.Model):
    name = models.CharField(verbose_name='Название блюда', max_length=100)
    ingredients = models.TextField(verbose_name='Ингредиенты')
    recipe = models.TextField(verbose_name='Рецепт')
    cooktime = models.IntegerField(verbose_name='Время приготовления')
    images = models.FileField(verbose_name='Фотография', blank=True)
    # bad_for_diets =

    def __str__(self):
        return f'{self.name}, время приготовления {self.cooktime} мин'

