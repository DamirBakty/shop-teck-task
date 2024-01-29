from django.contrib import admin

from cook.models import Recipe, Product, Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cooked_times')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'product', 'weight')