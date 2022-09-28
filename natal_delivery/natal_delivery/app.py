from flask import Flask
from natal_delivery.ext import config


# Application Factory

def create_app():
    """Factory principal"""

    app = Flask(__name__)
    config.init_app(app)
    return app
    
