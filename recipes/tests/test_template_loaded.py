from django.template.loader import get_template
from django.urls import reverse


def test_home_response_loads_home_template(db, client):
    response = client.get(reverse('recipes:home'))
    expected_template = get_template('recipes/pages/home.html').template  # type: ignore
    assert expected_template in response.templates


def test_search_uses_search_template(db, client):
    url = reverse('recipes:search') + '?q=teste'
    response = client.get(url)
    expected_template = get_template('recipes/pages/search.html').template  # type: ignore
    assert expected_template in response.templates
