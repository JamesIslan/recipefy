# from django.http import HttpResponse  # Temporary
from django.http import Http404
from django.shortcuts import render

from recipes.models import Category, Recipe
from utils.recipes.dummy import make_recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(
        request, 
        'recipes/pages/home.html', 
        context={
            'recipes': recipes,
        }
        )

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True)
    print(recipes) # Remove later
    if not recipes:
        raise Http404('Lamentamos, esta página não pode ser encontrada 😓')
    return render(
        request, 
        'recipes/pages/category.html', 
        context={
            'recipes': recipes,
            'page_title': f'{recipes.first().category.name} - Category | '
        }
    )

def recipe(request, id):
    return render(
        request, 
        'recipes/pages/recipe-view.html',
        context={
            'recipe': make_recipe(),
            'is_detail_page': True
        }
    )
