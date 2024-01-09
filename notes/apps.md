# Apps
Os apps são formas de separar o conteudo de páginas específicas de um site. Através dele, pode-se carregar diferentes views no arquivo `urls.py`, mas que estarão sendo criados em outro lugar.
- - - 
# Arquivos App
## `admin.py` e `models.py`
Sâo os arquivos aonde são inseridos os models da aplicação, que poderão ser alterados por um CRUD

## `apps.py`
Contém informações acerca do app em si, como por exemplo o nome que lhe foi dado na hora da criação.

## `tests.py`
É o arquivo onde serão inseridos os testes da aplicação

## `views.py`
É o arquivo onde são inseridas as views, ou seja, aquilo que será mostrado ao cliente quando a página for carregada.