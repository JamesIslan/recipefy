from django.contrib.auth.models import User
from factory import SubFactory
from factory.django import DjangoModelFactory

from recipes.models import Category, Recipe


class UserFactory(DjangoModelFactory):
    def __init__(self) -> None:
        super().__init__()

    class Meta:
        model = User

    username = 'fulanodetal'
    first_name = 'Fulano'
    last_name = 'de Tal'
    email = 'fulano@gmail.com'
    password = 'fulano123'


class CategoryFactory(DjangoModelFactory):
    def __init__(self) -> None:
        super().__init__()

    class Meta:
        model = Category

    name = 'Categoria'


class RecipeFactory(DjangoModelFactory):
    def __init__(self) -> None:
        super().__init__()

    class Meta:
        model = Recipe

    title = 'Uma receita genérica'
    description = 'Uma receita deliciosa e muito fácil de fazer'
    slug = 'uma-receita-generica'
    preparation_time = 30
    preparation_time_unit = 'minutos'
    servings = 5
    servings_unit = 'pessoas'
    preparation_steps = 'Aqui virá o passo a passo de preparo'
    preparation_steps_is_html = False
    is_published = False
    author = SubFactory(UserFactory)
    category = SubFactory(CategoryFactory)
