from flask import Blueprint, request, render_template


bp = Blueprint("site", __name__)

"""Extensão Flask"""


"""Inicialização de Extensões"""
@bp.route('/')
def index():
    return render_template(
        "base.html"
    )

@bp.route("/sobre")
def sobre():
    return "<h1>Esse é o melhor restaurante de SJM</h1><button>SIM</button><button>NÃO</button>"


@bp.route('/login')
def login():
    return "<form><input type='text'></input></form>"