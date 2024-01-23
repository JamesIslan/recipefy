from django.test import TestCase
from django.urls import reverse


class TemplateLoadedTest(TestCase):
    def test_home_response_loads_home_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_search_uses_search_template(self):
        url = reverse('recipes:search') + '?q=teste'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
