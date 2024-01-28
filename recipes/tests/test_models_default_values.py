def test_recipe_model_test_values_are_correct(db, recipe):
    assert recipe.title == 'Uma receita genérica'
    assert recipe.description == 'Uma receita deliciosa e muito fácil de fazer'
    assert recipe.slug == 'uma-receita-generica'
    assert recipe.preparation_time == 30
    assert recipe.preparation_time_unit == 'minutos'
    assert recipe.servings == 5
    assert recipe.servings_unit == 'pessoas'
    assert recipe.preparation_steps == 'Aqui virá o passo a passo de preparo'
    assert not recipe.preparation_steps_is_html
    assert not recipe.is_published


def test_user_model_test_values_are_correct(db, user):
    assert user.username == 'fulanodetal'
    assert user.first_name == 'Fulano'
    assert user.last_name == 'de Tal'
    assert user.email == 'fulano@gmail.com'
    assert user.password == 'fulano123'


def test_category_model_test_values_are_correct(db, category):
    assert category.name == 'Categoria'
