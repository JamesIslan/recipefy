from django.test import TestCase
from django.urls import reverse


class RecipeStatusCodeTest(TestCase):
    def test_recipe_home_response_returns_http_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        assert response.status_code == 200
