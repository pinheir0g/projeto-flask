from flask import Flask

from natal_delivery.ext import site
from natal_delivery.ext import config
from natal_delivery.ext import toolbar
from natal_delivery.ext import db
from natal_delivery.ext import migrate
from natal_delivery.ext import cli
from natal_delivery.ext import hooks
from natal_delivery.ext import auth
from natal_delivery.ext import admin


# Application Factory

def create_app():
    """Factory principal"""

    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    hooks.init_app(app)
    return app
    
