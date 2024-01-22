from django.test import TestCase
from django.urls import reverse


class StatusCodeTest(TestCase):
    def test_home_response_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_category_response_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_detail_response_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)
