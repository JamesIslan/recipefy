from django.urls import reverse


def test_home_url_is_correct(db):
    url = reverse('recipes:home')
    assert url == '/'


def test_category_url_is_correct(db):
    url = reverse('recipes:category', kwargs={'category_id': 1})
    assert url == '/recipes/category/1/'


def test_detail_url_is_correct(db):
    url = reverse('recipes:recipe', kwargs={'id': 1})
    assert url == '/recipes/1/'


def test_search_url_is_correct(db):
    url = reverse('recipes:search')
    assert url == '/recipes/search/'
