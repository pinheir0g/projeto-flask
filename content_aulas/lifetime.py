# Contextos

from flask import Flask

def create_app():
    """Dentro dessa função vão as configurações do aplicativo."""
    app = Flask(__name__)

    ## 1 Configuração

    ### Add configuração

    app.config["DEBUG"] = True
    app.config["SQLModel"] = "sqlite:///app.db" 

    ### Registrar Rotas

    """Forma de adicionar uma rota"""
    @app.route("/path")
    def função():
        ...

"""Outra forma de adicionar uma rota"""
    @app.add_url_rule("/path", callable)

    ### Inicializar extensões

    from flask_admin import Admin
    Admin.init_app(app)

    ### Registrar Blueprints

    app.register_blueprints(...)

    ### add hooks

    """São coisas que vão acontecer em determinado
    momento, e você pode injetar dependências.
    é uma injeção de métodos de dependências"""

    @app.before_request(...)
    @app.error_handler(...)

    ### Chamar outras factories

    views.init_app(app)

    ## 2 App Context
    """Entra em application context, quando o programa é rodado 
    e ainda não aconteceu nada, não teve nenhum request"""
    ### App está pronto! ´app´

    ### Testar

    app.test_client
    debug
    objetos globais do Flask
    (importar request, session, g)
    - hooks

    ## 3 Request Context
    usar globais do flask

    from flask import request, session
    
    request.args
    request.form
    