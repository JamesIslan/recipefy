# Renders
Renders em Django são funções responsáveis pela renderização de páginas HTML. <br>
A função `render()` propriamente dita é um atalho, e seu papel é de converter um template HTML para uma string, que será carregada e enviada como resposta ao cliente através de uma HTTPResponse.
- - - 

# Parâmetros
## `status=`
É o parâmetro referente ao status code da resposta. Ou seja, ao renderizar uma certa página, quando esse processo for completo, poderá ser enviado junto da resposta o código HTTP referente a essa requisição.
## `context=`
O parâmetro `context` serve para se passar variáveis para um certo template HTML. Ou seja, um template genérico que cubra dois casos pode ser criado utilizando essas variáveis, e ao passar na render de cada um desses casos um context diferente, a página resultante será diferente.
