from pytest import mark


@mark.django_db
class TestRecipeModel:
    @mark.parametrize(
        'field,max_length',
        [
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ],
    )
    def test_recipe_fields_max_length(self, field: str, max_length: int, recipe):
        recipe.preparation_steps_is_html = True
        assert recipe._meta.get_field(field).max_length == max_length  # type: ignore

    def test_recipe_preparation_steps_is_html_is_false_by_default(self, recipe):
        assert not recipe.preparation_steps_is_html

    def test_recipe_is_published_is_false_by_default(self, recipe, client):
        assert not recipe.is_published

    def test_recipe_string_representation_is_correct(self, recipe):
        desired_title = 'Testing representation'
        recipe.title = desired_title
        assert str(recipe) == desired_title
