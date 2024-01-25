from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

from .conftest import RecipeFactory, UserFactory


class ViewsTest(TestCase):
    # Home related tests
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        assert view.func is views.home
        self.assertIs(view.func, views.home)

    def test_home_template_shows_no_recipes_found_if_no_recipes(self):
        response_content = self.client.get(reverse('recipes:home')).content.decode(
            'utf-8'
        )
        self.assertIn(
            'Não há receitas cadastradas!',
            response_content,
        )

    def test_home_template_uses_recipes_template(self):
        RecipeFactory(is_published=True)
        response = self.client.get(
            reverse(
                'recipes:home',
            )
        )
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Uma receita genérica', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_home_template_doesnt_load_non_published_recipes(self):
        RecipeFactory(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn(
            'Não há receitas cadastradas!',
            content,
        )

    # Category related tests
    def test_category_template_loads_recipes(self):
        desired_title = 'This is a category test'
        RecipeFactory(title=desired_title, is_published=True)

        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        content = response.content.decode('utf-8')

        self.assertIn(desired_title, content)

    def test_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_category_template_doesnt_load_non_existent_category(self):
        RecipeFactory(is_published=False)
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertEqual(response.status_code, 404)

    # Detail related tests
    def test_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_detail_template_loads_correct_recipe(self):
        desired_title = 'This is a detail page - It loads only one recipe'
        RecipeFactory(title=desired_title, is_published=True)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(desired_title, content)

    def test_detail_template_doesnt_load_non_published_recipe(self):
        RecipeFactory(is_published=False)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 404)

    # Search related tests
    def test_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)

    def test_search_can_find_recipe_by_title(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'

        recipe1 = RecipeFactory(
            slug='one',
            title=title1,
            author=UserFactory(username='james'),
            is_published=True,
        )

        recipe2 = RecipeFactory(
            slug='two',
            title=title2,
            author=UserFactory(username='james2'),
            is_published=True,
        )
        search_url = reverse('recipes:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=recipe')

        self.assertIn(recipe1, response1.context['search_result'])
        self.assertNotIn(recipe2, response1.context['search_result'])

        self.assertIn(recipe2, response2.context['search_result'])
        self.assertNotIn(recipe1, response2.context['search_result'])

        self.assertIn(recipe1 and recipe2, response_both.context['search_result'])
