from django.urls import reverse


def test_home_response_raises_200_OK(db, client):
    response = client.get(reverse('recipes:home'))
    assert response.status_code == 200


def test_category_response_raises_404_if_no_recipes_found(db, client):
    response = client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
    assert response.status_code == 404


def test_detail_response_raises_404_if_no_recipe_found(db, client):
    response = client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
    assert response.status_code == 404


def test_search_response_raises_404_if_no_search_terms(db, client):
    response = client.get(reverse('recipes:search'))
    assert response.status_code == 404
