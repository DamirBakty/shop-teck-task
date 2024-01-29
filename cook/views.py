from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db import transaction
from cook.models import Product, Recipe, Ingredient
from django.db.models import Q


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    receipts = Recipe.objects.filter(
        ~Q(ingredients__product_id=product_id, ingredients__weight__gte=10)
    )

    return render(request, 'cook/index.html', context={
        'receipts': receipts,
        'product_id': product_id
    })


@transaction.atomic
def add_product_to_recipe(request):
    receipt_id = request.GET.get('receipt_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')
    recipe = get_object_or_404(Recipe, pk=receipt_id)
    product = get_object_or_404(Product, pk=product_id)
    Ingredient.objects.update_or_create(
        recipe=recipe,
        product=product,
        defaults={
            'weight': weight
        }
    )
    return redirect(reverse(f'cook:show_recipes_without_product') + f'?product_id={product_id}')


@transaction.atomic
def cook_recipe(request):
    receipt_id = request.GET.get('receipt_id')
    recipe = get_object_or_404(Recipe, pk=receipt_id)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    for ingredient in ingredients:
        ingredient.use_product()
    return redirect('cook:show_recipes_without_product')
