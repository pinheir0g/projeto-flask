from flask import Blueprint, render_template


bp = Blueprint("site", __name__)

"""Extensão Flask"""


"""Inicialização de Extensões"""
@bp.route('/')
def index():
    return render_template(
        "index.html", 
        site_name="Natal Delivery", 
        site_subtitle="O melhor que nos temos!"
    )

@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route('/login')
def login():
    return "<form><input type='text'></input></form>"


@bp.route("/cardapio")
def menu():
    return render_template("menu.html")