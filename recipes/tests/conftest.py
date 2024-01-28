from django.contrib.auth.models import User
from factory import SubFactory
from factory.django import DjangoModelFactory
from pytest_factoryboy import register as register_factory

from recipes.models import Category, Recipe


@register_factory
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = 'fulanodetal'
    first_name = 'Fulano'
    last_name = 'de Tal'
    email = 'fulano@gmail.com'
    password = 'fulano123'


@register_factory
class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = 'Categoria'


@register_factory
class RecipeFactory(DjangoModelFactory):
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
