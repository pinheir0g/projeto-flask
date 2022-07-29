from flask import Flask
from delivery_natal import views

def create_app():
    """Factory principal"""

    app = Flask(__name__)
    views.init_app(app)
    
    return app
