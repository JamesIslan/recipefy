from django.core.exceptions import ValidationError
from pytest import raises as assertRaises

from .conftest import CategoryFactory


def test_category_model_string_representation_is_correct(db):
    category = CategoryFactory()
    assert str(category) == category.name


def test_category_model_name_max_length_is_65_chars(db):
    category = CategoryFactory(name='A' * 66)

    with assertRaises(ValidationError):
        category.full_clean()  # type: ignore
