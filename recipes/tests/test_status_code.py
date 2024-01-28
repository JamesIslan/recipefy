from django.test import TestCase
from django.urls import reverse
from pytest import mark


class TestStatusCode(TestCase):
    def test_home_response_raises_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        assert response.status_code == 200

    def test_category_response_raises_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        assert response.status_code == 404

    def test_detail_response_raises_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
        assert response.status_code == 404

    def test_search_response_raises_404_if_no_search_terms(self):
        response = self.client.get(reverse('recipes:search'))
        assert response.status_code == 404
