from django.core.exceptions import ValidationError
from pytest import mark
from pytest import raises as assertRaises


@mark.django_db
class TestCategoryModel:
    def test_category_model_string_representation_is_correct(self, category):
        assert str(category) == category.name

    def test_category_model_name_max_length_is_65_chars(self, category):
        category.name = 'A' * 66

        with assertRaises(ValidationError):
            category.full_clean()  # type: ignore
