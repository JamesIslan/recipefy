from pytest import mark


@mark.parametrize(
    'field,max_length',
    [
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ],
)
def test_recipe_fields_max_length(db, field: str, max_length: int, recipe):
    recipe.preparation_steps_is_html = True
    assert recipe._meta.get_field(field).max_length == max_length


def test_recipe_preparation_steps_is_html_is_false_by_default(db, recipe):
    assert not recipe.preparation_steps_is_html


def test_recipe_is_published_is_false_by_default(db, recipe):
    assert not recipe.is_published


def test_recipe_string_representation_is_correct(db, recipe):
    desired_title = 'Testing representation'
    recipe.title = desired_title
    assert str(recipe) == desired_title
