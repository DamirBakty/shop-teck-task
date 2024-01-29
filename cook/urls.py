from django.urls import path
from .views import show_recipes_without_product, add_product_to_recipe, cook_recipe

app_name = 'cook'


urlpatterns = [
    path('show_recipes_without_product/', show_recipes_without_product, name='show_recipes_without_product'),
    path('add_product_to_recipe/', add_product_to_recipe,
         name='add_product_to_recipe'),
    path('cook_recipe/', cook_recipe, name='cook_recipe'),
]
