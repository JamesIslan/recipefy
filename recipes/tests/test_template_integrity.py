from django.urls import reverse


def test_search_template_escapes_code_injection(db, client):
    url = reverse('recipes:search') + '?q=<Teste>'
    escaped_query_string = '&quot;&lt;Teste&gt;&quot;'
    content = client.get(url).content.decode('utf-8')
    assert escaped_query_string in content
