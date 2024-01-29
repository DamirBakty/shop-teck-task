from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    cooked_times = models.IntegerField(default=0, verbose_name='Использовано')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingredients')
    weight = models.IntegerField(default=0, verbose_name='Вес')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = "Ингредиенты"

    def use_product(self):
        self.product.cooked_times += 1
        self.product.save()
