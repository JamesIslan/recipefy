from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')

    return render(
        request,
        'recipes/pages/home.html',
        context={
            'recipes': recipes,
        },
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
            'page_title': f'{recipes[0].category.name} - Category | ',
        },
    )


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(
        request,
        'recipes/pages/recipe-view.html',
        context={'recipe': recipe, 'is_detail_page': True},
    )


def search(request):
    query_string = request.GET.get('q', '').strip()

    if not query_string:
        raise Http404()

    search_result = Recipe.objects.filter(
        Q(Q(title__icontains=query_string) | Q(description__icontains=query_string))
        & Q(is_published=True),
    ).order_by('-id')

    return render(
        request,
        'recipes/pages/search.html',
        context={
            'page_title': f'Resultados da busca por "{query_string}" | ',
            'query_string': query_string,
            'search_result': search_result,
        },
    )
