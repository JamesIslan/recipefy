from typing import assert_never

from django.test import TestCase
from parameterized import parameterized

from .conftest import RecipeFactory


class RecipeModelTest(TestCase):
    def setUp(self) -> None:
        self.recipe = RecipeFactory()
        return super().setUp()

    @parameterized.expand(
        [
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ]
    )
    def test_recipe_fields_max_length(self, field: str, max_length: int):
        self.recipe.preparation_steps_is_html = True
        assert self.recipe._meta.get_field(field).max_length == max_length  # type: ignore

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        assert not self.recipe.preparation_steps_is_html

    def test_recipe_is_published_is_false_by_default(self):
        assert not self.recipe.is_published

    def test_recipe_string_representation_is_correct(self):
        desired_title = 'Testing representation'
        self.recipe.title = desired_title
        assert str(self.recipe) == desired_title
