from natal_delivery import __version__

def test_version():
    assert __version__ == '0.1.0'

def test_app_is_created(app):
    assert app.name == 'natal_delivery.app'

def test_config_is_loaded(config):
    assert config['DEBUG'] is True

def test_request_returns_200(client):
    assert client.get('/').status_code == 200

def test_request1_returns_200(client):
    assert client.get('/sobre').status_code == 200

def test_request2_returns_200(client):
    assert client.get('/login').status_code == 200