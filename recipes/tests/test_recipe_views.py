from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse("recipes:home"))
        assert view.func is views.home
        self.assertIs(view.func, views.home)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response_content = self.client.get(
            reverse("recipes:home")
            ).content.decode("utf-8")
        self.assertIn(
            "Não há receitas cadastradas!",
            response_content,
        )

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={"category_id": 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id": 1}))
        self.assertIs(view.func, views.recipe)
