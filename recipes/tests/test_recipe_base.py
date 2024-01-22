from django.test import TestCase

from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Categoria'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='Fulano',
        last_name='de Tal',
        username='fulanodetal',
        email='fulano@gmail.com',
        password='fulano123',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

    def make_recipe(
        self,
        category_data={},
        author_data={},
        title='Uma receita genérica',
        description='Uma receita deliciosa e muito fácil de fazer',
        slug='uma-receita-generica',
        preparation_time=30,
        preparation_time_unit='minutos',
        servings=5,
        servings_unit='pessoas',
        preparation_steps='Aqui virá o passo a passo de preparo',
        preparation_steps_is_html=False,
        is_published=True,
    ):
        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )
