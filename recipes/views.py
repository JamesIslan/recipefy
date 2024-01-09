from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', status=404, context={
        'recipe_type': 'sobremesa'
    })