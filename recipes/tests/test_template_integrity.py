from django.test import TestCase
from django.urls import reverse


class TemplateIntegrityTest(TestCase):
    def test_search_template_escapes_code_injection(self):
        url = reverse('recipes:search') + '?q=<Teste>'
        escaped_query_string = '&quot;&lt;Teste&gt;&quot;'
        content = self.client.get(url).content.decode('utf-8')
        assert escaped_query_string in content
