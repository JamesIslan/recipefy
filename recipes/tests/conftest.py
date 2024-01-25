from django.contrib.auth.models import User
from factory import SubFactory
from factory.django import DjangoModelFactory, DjangoOptions

from recipes.models import Category, Recipe


class UserFactory(DjangoModelFactory):
    def __new__(cls, *args, **kwargs):
        return super().__new__(*args, **kwargs)

    class Meta:
        model = User

    username = 'fulanodetal'
    first_name = 'Fulano'
    last_name = 'de Tal'
    email = 'fulano@gmail.com'
    password = 'fulano123'


class CategoryFactory(DjangoModelFactory):
    def __new__(cls, *args, **kwargs):
        return super().__new__(*args, **kwargs)

    class Meta:
        model = Category

    name = 'Categoria'


class RecipeFactory(DjangoModelFactory, DjangoOptions):
    @classmethod
    def create(cls, **kwargs):
        return super().create(**kwargs)

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
