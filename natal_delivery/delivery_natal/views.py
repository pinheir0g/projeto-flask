"""Extensão Flask"""

def init_app(app):
    """Inicialização de Extensões"""

    @app.route('/')
    def index():
        return '<h1 style="text-align: center;">Restaurante da Natal</h1><button>Login</button>'


    @app.route("/sobre")
    def sobre():
        return "<h1>Esse é o melhor restaurante de SJM</h1><button>SIM</button><button>NÃO</button>"


    @app.route('/login')
    def login():
        return "<form><input type='text'></input></form>"

        