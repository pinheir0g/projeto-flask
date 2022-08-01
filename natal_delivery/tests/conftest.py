import pytest
from natal_delivery.app import create_app 

@pytest.fixture(scope='module')
def app():
    """Instance of Main flask app"""
    app = create_app()
    return app
