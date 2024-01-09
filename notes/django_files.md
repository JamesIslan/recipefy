# Django Main Files

## `manage.py`
O arquivo `manage.py` executa de forma similiar ao comando `django-admin`, com a diferença de que o primeiro carrega também as configurações estabelecidas no arquivo `settings.py`.
>Isso é feito através da variável de ambiente "DJANGO_SETTINGS_MODULE", que é carregada dentro do arquivo `manage.py`
- - - 
## `settings.py`
É o principal arquivo de configurações do Django.
- - - 
## `__init__.py`
Esse arquivo indica ao Python que o conjunto de arquivos em questão trata-se de um pacote Python
- - - 
## `wsgi.py` e `asgi.py`
São utilizados em produção para fazer a ligação entre o django e um webserver
- - - 
## `urls.py`
Estabelece as configurações de rota e endereço para acesso do site pelo navegador.