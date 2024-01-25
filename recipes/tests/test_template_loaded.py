from django.template.loader import get_template
from django.test import TestCase
from django.urls import reverse


class TemplateLoadedTest(TestCase):
    def test_home_response_loads_home_template(self):
        response = self.client.get(reverse('recipes:home'))
        expected_template = get_template('recipes/pages/home.html').template  # type: ignore
        assert expected_template in response.templates

    def test_search_uses_search_template(self):
        url = reverse('recipes:search') + '?q=teste'
        response = self.client.get(url)
        expected_template = get_template('recipes/pages/search.html').template  # type: ignore
        assert expected_template in response.templates
