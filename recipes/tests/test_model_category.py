from django.core.exceptions import ValidationError
from django.test import TestCase
from pytest import raises as assertRaises

from .conftest import CategoryFactory


class CategoryModelTest(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory()
        return super().setUp()

    def test_category_model_string_representation_is_correct(self):
        assert str(self.category) == self.category.name

    def test_category_model_name_max_length_is_65_chars(self):
        self.category.name = 'A' * 66

        with assertRaises(ValidationError):
            self.category.full_clean()  # type: ignore
