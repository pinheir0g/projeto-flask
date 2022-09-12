from flask import Flask

from natal_delivery.ext import site
from natal_delivery.ext import config
from natal_delivery.ext import toolbar
from natal_delivery.ext import db
from natal_delivery.ext import cli

# Application Factory

def create_app():
    """Factory principal"""

    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
    
