import click
from natal_delivery.ext.db import db
from natal_delivery.ext.auth.models import User
from natal_delivery.ext.db import models
import os

def init_app(app):

    @app.cli.command()
    def create_db():

        """Create a database"""
        arquivo = "~/dev/project-flask/natal_delivery/natal_delivery/delivery.db"
        if not os.path.exists(arquivo):
            db.create_all()


    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):

        """Add a new user"""
        user = User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f"Usuário {email} criado com sucesso!")
     
    @app.cli.command()
    def order_list():

        """Show the order list"""
        order = models.Order.query.all()
        return order

    @app.cli.command()
    def users_list():
        
        """Show the users list"""
        users = User.query.all()
        click.echo(f"""== Lista de Usuários ==
        {users}""")
        

    @app.cli.command()
    @click.option("--name", "-n")
    @click.option("--on_menu", "-o", default=False)
    def add_category(name, on_menu):
        """Add a new category"""
        category = models.Category(
            name=name,
            on_menu=on_menu
        )
        db.session.add(category)
        db.session.commit()


    @app.cli.command()
    @click.option("--name", "-n")
    @click.option("--image", "-i")
    @click.option("--price", "-p")
    @click.option("--available", "-a", default=False)
    def add_items(name, image, price, available):
        """Add a new item"""
        items = models.Items(
            name=name,
            image=image,
            price=price,
            available=available
        )
        db.session.add(items)
        db.session.commit()
          

    @app.cli.command()
    @click.option("--zipcode", "-z")
    @click.option("--country", "-c")
    @click.option("--address", "-a")
    @click.option("--user_id", "-ui")
    @click.option("--user", "-u")
    def add_address(zipcode, country, address, user_id, user):
        """Add a new address"""
        address = models.Address(
            zipcode=zipcode,
            country=country,
            address=address,
            user_id=user_id,
            user=user
        )

        db.session.add(address)
        db.session.commit()