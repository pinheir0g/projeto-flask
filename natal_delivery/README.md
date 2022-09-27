# Flask

É um framework para desenvolvimento web, conhecido como um micro framework,
isso significa que ele vai tentar entregar tudo o que o desenvolvedor precisa para fazer a base da sua aplicação web, entrega somente o básico, faz coisas simples como: fazer o roteamento, definir funções, retornos, plugar extensões.

Resumidamente ele te da as ferramentas básicas de uma aplicação e deixa você decidir como vai usar.

Código básico para rodar um servidor web usando flask e definir uma função de exemplo hello.

```Python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')                 # decorator pra dizer que a função atende na rota /
def hello():
    return "Hello, World!"      # Objeto response retornado
    
```

> Salvar o arquivo que vai iniciar a aplicação com flask, tem por padrão do flask, colocar o nome dele de app.py, que assim o flask consegue identificar o arquivo que deve executar pra iniciar a aplicação com mais facilidade e sem você precisar especificar o nome do arquivo na chamada dele.

Para rodar a aplicação feita acima, basta chamar no terminal o comando: flask run.

Para iniciar um ambiente de desenvolvimento com o flask e ter umas funções a mais quando a aplicação esta em desenvolvimento. Com esse ambiente, o flask inicia com o debug dele ativado e vai fazer restart do server automático.

Utiliza o comando:

    export FLASK_DEBUG=True
---
## Views

São as função que colocamos nas rotas, no exemplo acima, a função hello() é uma view que atende na rota /. 
 São chamadas de views por que elas são as funções responsáveis por levar a informação para a camada de visualização


Protocolo do flask é, funções onde o dev vai ligar as funções com URL's e o retorno da função tem que ser um texto.

Cada rota criada é uma função do python, que vai definir quais são os parâmetros de match da rota e vai retornar um objeto response que vai ser um texto.

---
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

Para executar esse test não precisa importar o pytest normalmente, basta chamar ele pelo terminal e passar o nome do arquivo ou pasta.

    $ pytest test_ex.py

Também pode passar o parametro -v para ver mais detalhes do test

    $ pytest tests/ -v

 Depois de executado, o pytest vai procurar dentro da pasta escolhida um arquivo chamado conftest.py e executar o que tiver lá dentro.

 Lá dentro do conftest.py pode-se fazer qualquer coisa que o dev quiser para preparar o ambiente de teste dele, mas o mais importante é colocar fixtures.

 Fixtures são dados que vão ser usados apenas para testes e depois podem ser excluídos sem problemas, coisas que vão ser reaproveitadas e repetidas no ambiente de teste.

 Para registrar uma fixture, basta adicionar em cima da função app, que é uma instancia do app verdadeiro, um decorator, usa o seguinte código dentro do conftest.py:

 ```Python
 import pytest

 @pytest.fixture()
 def app():
    app = create_app()
    return app
 ```

 Esse código significa que toda vez que for rodado um test novo, o dev pode contar que vai ser criado um objeto chamado "exemplo", nesse caso, e toda vez que for acessado vai ser retornado uma string contendo "testando".

 Então ai dentro o dev vai criando varias fixtures para tudo que for reutilizar, pode ser uma pasta, um banco de dados, etc.

 Outra coisa para escolher na fixture é o scope dessa fixture.
 
 ```Python
 import pytest

 @pytest.fixture(scope='function')
 def app():
    app = create_app()
    return app
 ```

 se for passado o scope com o nome de "function", para cada função de test, vai ser criado e deletado um app novo, para cada uma das funções.

 se for passado o scope com o nome de "module" todo o modulo de test vai ter apenas um app, vai ser testado somente um.

 Depois basta chamar no terminal:

    $ pytest test/ --fixtures

Que vai ser retornado uma lista com as fixtures existentes. 

---
## Blueprints

São a mesma coisa que plug-in no flask, é um esquema onde você divide o projeto em várias camadas, varias pastas diferentes que elas seriam as próprias blueprints e vai trabalhando o que precisa ser trabalhado em cada uma, facilitando se caso der algum erro depois, não precisa editar o projeto todo só a blueprint que deu o problema.

---
## CI
É uma sigla para Continuos integration (Integração contínua).
Isso significa que que cada vez que eu fizer uma alteração no código, localmente, vou precisar integrar ele com o código principal que é a master no github.

E pra isso acontecer, antes de fazer a integração, vai ser preciso fazer umas checagens para que verifique que tudo esta certo e o código principal não vai quebrar.

---
## Templates
Para renderização de templates com flask, vamos usar a função "render_template" do próprio flask, onde ela recebe um parâmetro que é uma string especificando o arquivo html que ele deve renderizar.

Dentro da pasta de [templates](natal_delivery/templates/) vamos criar os templates de cada pagina que vai ser criada dentro do aplicativo.

Na criação dos layouts desse aplicativo, usei o Bulma.css que é um site onde contém diversos layouts para leigos, como eu, em frontend.

Dentro desses templates to usando as variáveis de templates que é a linguagem jinja do flask.

Ex:

```Html
<!-- exemplo.html-->
<html>
  <head>
    <title>{{ site_name }}</title>
  </head>
  <body>
    {% for item in items %}
    <ul>
        <li>{{item}}</li>
    </ul>
    {% endfor %}
  </body>
```

A linguagem jinja é escrita dentro das chaves { } e contém variações para cada tipo de coisa que for fazer, por exemplo, o simbolo de % ou as duas {{ }} para criar uma variável, entre outras.

O jinja serve para renderizar o template de maneira dinâmica, nesse exemplo os items podem ser qualquer coisa, ele vai ser passado na hora de renderizar.

Então na hora que for fazer a chamada da função render_template, pode ser passado parâmetros especificando as variáveis que foram criadas com o jinja.

Ex:

```Python
from flask import render_template

def index():
    return render_template("index.html", 
        site_name="Natal Delivery",
        items=["caneca", "celular", "pente"]
    )
```

Para entender mais sobre a linguagem, veja a documentação do [jinja](https://jinja.palletsprojects.com/en/3.1.x/).

---

## Databases

O que precisa para um relacionamento dar certo?

chave primária e relacionamento

## SQL

### Consultas estruturais
- CREATE TABLE
- ALTER TABLE
- DROP TABLE

### Consultas de Dados (CRUD)

- INSERT INTO nome VALUE(...);
- SELECT campo FROM nome;
- UPDATE nome SET campo WHERE;
- DELETE from nome WHERE; 

Sempre que usar UPDATE e DELETE usar a clausula WHERE para selecionar o que você deseja alterar ou deletar, porque sem ela corre o risco de alterar ou deletar todo o banco de dados.

é recomendado que toda tabela tenha um ID e que todo ID seja uma primary key.

cada tabela criada no db vai ser uma classe em python e cada atributo dessa classe vai ser um field na tabela.

## ORM - Object Relational Mapper
É uma técnica de mapeamento objeto relacional que permite fazer relação dos objetos com os dados que os mesmos representam.


## Migrations
É para quando é preciso fazer uma alteração no banco de dados, criar, alterar ou remover algo.

Nesse projeto para fazer as migrations ta sendo usando o flask-migrate, que é uma biblioteca do flask que é responsável por automatizar todo esse processo de migrations.

Para fazer isso, basta criar o arquivo de migrate, e dentro dele iniciar uma instancia do flask-migrate.

```Python
# Arquivo migrate.py

from flask_migrate import Migrate

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
```


Depois basta rodar o comando:

    $ flask db init

Vai ser criado uma pasta migrations contendo todo o conteúdo necessário para fazer o migrate.

Depois de fazer a alteração no banco de dados, roda o comando:

    $ flask db migrate -m "Comentário"

Feito isso foi iniciado a migrate e agora precisa ser aplicar as alterações e pra isso roda o comando:

    $ flask db upgrade

Agora todas as alterações feitas no banco de dados, foram realizadas e aplicadas.

Leia a documentação do [flask-migrate]((https://flask-migrate.readthedocs.io/en/latest/)).

---

## Interface Administrativa com Flask-Admin

Flask-admin é uma extensão do flask que cria pra gente uma interface administrativa em cima de um data model existente, deixando o gerenciamento de dados dos serviços de web mais amigável através de uma interface.

O conceito por detrás do flask-admin é que ele deixa você criar interfaces complicadas, agrupando views individuais juntas em classes. Cada pagina web que você ve no frontend, é representada como um método ou uma classe que foi adicionada a interface.

Essas view classes são bastante úteis quando for preciso fazer o famoso CRUD de uma forma mais pratica em cada modelo do seu banco de dados.

O primeiro passo para iniciar uma interface adm vazia:

```Python
from flask_admin import Admin

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin()
# Add administrative views here

def init_app(app):
    admin.name = "Exemplo"
    admin.template_mode = "bootstrap2"
    admin.init_app(app):
```

Depois que inciar a aplicação e você entrar em http://localhost:5000/admin/, vai ter uma pagina vazia com uma barra de navegação no topo. Você pode personalizar ela especificando o tema do bootswatch.

### Adicionando Model Views
Adicionar essas models views, permite que você adicione paginas para manutenção dos modelos do seu banco de dados.
Faça isso criando uma instancia da classe ModelView, que você pode importar das ORM's que estão no backend do Flask-admin, nesse projeto foi usado o SQLAlchemy.

```Python
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin()
# Add administrative views here

def init_app(app):
    admin.name = "Exemplo"
    admin.template_mode = "bootstrap2"
    admin.init_app(app)

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))
```

Pronto, isso lhe da todas as características para fazer um CRUD no seu model.

NOTA: Existe diversas coisas que da pra fazer dentro das views criadas, personalizar de formas diferentes, adicionar novos comandos, etc.

Leia a documentação do [flask-admin](https://flask-admin.readthedocs.io/en/latest/).

// Em desenvolvimento