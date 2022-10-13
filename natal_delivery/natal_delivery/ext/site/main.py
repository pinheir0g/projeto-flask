from flask import Blueprint, render_template, request, redirect
from natal_delivery.ext.auth.form import UserForm
from natal_delivery.ext.auth.controller import create_user


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

@bp.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        create_user(
            email=form.email.data,
            passwd=form.passwd.data
        )
        # forçar login
        return redirect("/")

    return render_template("userform.html", form=form)


@bp.route('/login')
def login():
    return "<form><input type='text'></input></form>"


@bp.route("/cardapio")
def menu():
    return render_template("menu.html")