from django.test import TestCase
from django.urls import reverse


class TemplateLoadedTest(TestCase):
    def test_home_response_loads_home_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
