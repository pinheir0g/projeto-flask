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


## Tests com Pytest

Pytest é uma biblioteca python feita para todo o tipo de testes que o dev precisará fazer, tanto tests unitário quanto tests funcionais e etc.

O papel de um test é assegurar que alguma função que o programa precisa executar seja executada corretamente sem nenhum erro.

No pytest todo test nada mais é do que uma função que por convenção começa com test_ e dentro dessa função usa a palavra assert, que é do próprio python, e o assert vai verificar se a coisa é verdadeira, caso o que for passado depois do assert seja falso, significa que o test quebrou/falhou.

EX:
```Python
def test_exemplo():
    assert 1 + 1 == 2

def test_exemplo1():
    assert 1 + 1 == 3
```

Para executar esse test não precisa importar o pytest normalmente, basta chamar ele pelo terminal e passar o nome do arquivo.

    $ pytest test_ex.py

 Depois de executado, o pytest vai procurar dentro da pasta escolhida um arquivo chamado conftest.py e executar o que tiver lá dentro.

 Lá dentro pode-se fazer qualquer coisa que o dev quiser para preparar o ambiente de teste dele, mas o mais importante é colocar fixtures.

 Fixtures são dados que vão ser usados apenas para testes e depois podem ser excluídos sem problemas, coisas que vão ser reaproveitadas e repetidas no ambiente de teste.

 Para registrar uma fixuture, usa o seguinte codigo dentro do conftest.py:

 ```Python
 import pytest

 @pytest.fixture()
 def exemplo():
    return "testando"
 ```

 Esse codigo significa que toda vez que for rodado u8m test novo, o dev pode contar que vai ser criado um objeto chamado "exemplo", nesse caso, e toda vez que for acessado vai ser retornado uma string contendo "testando".

 Então ai dentro o dev vai criando varias fixtures para tudo que for reutilizar, pode ser uma pasta, um banco de dados, etc.

 Outra coisa para escolher na fixture é o scope dessa fixture.
 
 ```Python
 import pytest

 @pytest.fixture(scope='function')
 def exemplo():
    return "testando"
 ```

 se for passado o scope com o nome de "function", para cada função de test, vai ser criado e deletado um app novo, para cada uma das funções.

 se for passado o scope com o nome de "module" todo o modulo de test vai ter apenas um app, vai ser testado somente um.

 Depois basta chamar no terminal:

    $ pytest test/ --fixtures

Que vai ser retornado uma lista com as fixtures existentes. 


## Blueprints

São a mesma coisa que plug-in no flask