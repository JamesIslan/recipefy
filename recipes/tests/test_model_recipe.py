from pytest import mark

from .conftest import RecipeFactory


@mark.parametrize(
    'field,max_length',
    [
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ],
)
def test_recipe_fields_max_length(db, field: str, max_length: int):
    recipe = RecipeFactory(preparation_steps_is_html=True)
    assert recipe._meta.get_field(field).max_length == max_length  # type: ignore


def test_recipe_string_representation_is_correct(db, recipe):
    desired_title = 'Testing representation'
    recipe.title = desired_title
    assert str(recipe) == desired_title
