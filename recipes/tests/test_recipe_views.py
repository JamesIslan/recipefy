from django.urls import resolve, reverse

from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):
    # Home related tests
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        assert view.func is views.home
        self.assertIs(view.func, views.home)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response_content = self.client.get(reverse('recipes:home')).content.decode(
            'utf-8'
        )
        self.assertIn(
            'Não há receitas cadastradas!',
            response_content,
        )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()

        response = self.client.get(
            reverse(
                'recipes:home',
            )
        )
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Uma receita genérica', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_doesnt_load_non_published_recipes(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn(
            'Não há receitas cadastradas!',
            content,
        )

    # Category related tests
    def test_recipe_category_template_loads_recipes(self):
        desired_title = 'This is a category test'
        self.make_recipe(title=desired_title)

        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        content = response.content.decode('utf-8')

        self.assertIn(desired_title, content)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_template_doesnt_load_non_existent_category(self):
        self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': 1}
            )
        )

        self.assertEqual(response.status_code, 404)

    # Detail related tests
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_template_loads_correct_recipe(self):
        desired_title = 'This is a detail page - It loads only one recipe'
        self.make_recipe(title=desired_title)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(desired_title, content)

    def test_recipe_detail_template_doesnt_load_non_published_recipe(self):
        self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={'id': 1}
            )
        )

        self.assertEqual(response.status_code, 404)
