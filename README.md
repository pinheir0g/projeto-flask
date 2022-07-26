# Flask

É um framework para desenvolvimento web, conhecido como um micro framework,
isso significa que ele vai tentar entregar tudo o que o desenvolvedor precisa para fazer a base da sua aplicação web, entrega somente o básico, fazer coisas simples como: fazer o roteamento, definir funções, retornos, plugar extensões.

Basicamente ele te da as ferramentas básicas de uma aplicação e deixa você decidir como vai usar.

Código básico para rodar um servidor web usando flask e definir uma função básica hello.

```Python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')                 # decorator pra dizer que a função atende na rota /
def hello():
    return "Hello, World!"      # Objeto response retornado
```

## Views

São as função que colocamos nas rotas, o exemplo acima a função hello() é uma view que atende na rota /.
São chamadas de views por que elas são as funções responsáveis por levar a informação para a camada de visualização


Protocolo do flask é, funções onde o dev vai ligar as funções com URL's e o retorno da função tem que ser um texto.

Cada rota criada é uma função do python, que vai definir quais são os parâmetros de match da rota e vai retornar um objeto response que vai ser um texto.

Utiliza o comando:

    export FLASK_ENV=development

Para iniciar um ambiente de desenvolvimento com o flask e ter umas funções a mais em quando a aplicação esta em desenvolvimento. Com esse ambiente, o flask inicia com o debug dele ativado e vai fazer restart do server automático.


