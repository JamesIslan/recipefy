from django.core.exceptions import ValidationError
from django.test import TestCase

from .conftest import CategoryFactory


class CategoryModelTest(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory()
        return super().setUp()

    def test_category_model_string_representation_is_correct(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_category_model_name_max_length_is_65_chars(self):
        self.category.name = 'A' * 66

        with self.assertRaises(ValidationError):
            self.category.full_clean()  # type: ignore
