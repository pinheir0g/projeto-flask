import click
from natal_delivery.ext.db import db
from natal_delivery.ext.site import models

def init_app(app):

    @app.cli.command()
    def create_db():
        """Create a database"""
        db.create_all()


    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """Add a new user"""
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()
     
    @app.cli.command()
    def order_list():
        """Show the order list"""
        order = models.Order.query.all()
        return order

    @app.cli.command()
    def users_list():
        """Show the users list"""
        users = models.User.query.filter(models.User.admin == 1)
        for i in users:
            click.echo(i)
        