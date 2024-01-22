from django.test import TestCase
from django.urls import reverse


class RecipeTemplateLoadedTest(TestCase):
    def test_recipe_home_response_loads_home_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
