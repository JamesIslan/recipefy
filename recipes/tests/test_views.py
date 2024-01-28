from django.urls import resolve, reverse
from pytest import mark

from recipes import views

from .conftest import RecipeFactory, UserFactory


@mark.django_db
class TestViews:
    # Home related tests
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        assert view.func is views.home
        assert view.func is views.home

    def test_home_template_shows_no_recipes_found_if_no_recipes(self, client):
        response_content = client.get(reverse('recipes:home')).content.decode('utf-8')
        assert 'Não há receitas cadastradas!' in response_content

    def test_home_template_uses_recipes_template(self, client):
        RecipeFactory(is_published=True)
        response = client.get(
            reverse(
                'recipes:home',
            )
        )
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        assert 'Uma receita genérica' in content
        assert len(response_context_recipes) == 1

    def test_home_template_doesnt_load_non_published_recipes(self, client):
        RecipeFactory(is_published=False)

        response = client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        assert 'Não há receitas cadastradas!' in content

    # Category related tests
    def test_category_template_loads_recipes(self, client):
        desired_title = 'This is a category test'
        RecipeFactory(title=desired_title, is_published=True)

        response = client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        assert desired_title in content

    def test_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        assert view.func is views.category

    def test_category_template_doesnt_load_non_existent_category(self, client):
        RecipeFactory(is_published=False)
        response = client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        assert response.status_code == 404

    # Detail related tests
    def test_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        assert view.func is views.recipe

    def test_detail_template_loads_correct_recipe(self, client):
        desired_title = 'This is a detail page - It loads only one recipe'
        RecipeFactory(title=desired_title, is_published=True)

        response = client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        assert desired_title in content

    def test_detail_template_doesnt_load_non_published_recipe(self, client):
        RecipeFactory(is_published=False)

        response = client.get(reverse('recipes:recipe', kwargs={'id': 1}))

        assert response.status_code == 404

    # Search related tests
    def test_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        assert resolved.func is views.search

    def test_search_can_find_recipe_by_title(self, client):
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
        response1 = client.get(f'{search_url}?q={title1}')
        response2 = client.get(f'{search_url}?q={title2}')
        response_both = client.get(f'{search_url}?q=recipe')

        assert recipe1 in response1.context['search_result']
        assert recipe2 not in response1.context['search_result']

        assert recipe2 in response2.context['search_result']
        assert recipe1 not in response2.context['search_result']

        assert (recipe1 and recipe2) in response_both.context['search_result']
