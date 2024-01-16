# from django.http import HttpResponse  # Temporary
from django.shortcuts import get_list_or_404, get_object_or_404, render

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
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )
    return render(
        request, 
        'recipes/pages/category.html', 
        context={
            'recipes': recipes,
            'page_title': f'{recipes[0].category.name} - Category | '
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
