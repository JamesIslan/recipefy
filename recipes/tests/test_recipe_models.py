from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
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
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        self.assertFalse(self.recipe.preparation_steps_is_html)

    def test_recipe_is_published_is_false_by_default(self):
        self.assertFalse(self.recipe.is_published)
