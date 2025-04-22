import pytest
from flask import Flask

@pytest.fixture
def app():
    """Create a test Flask application instance."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    
    @app.route('/test')
    def test_route():
        return {'status': 'ok'}
    
    return app

@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()

def test_app_creation(client):
    """Test if the app is created correctly."""
    response = client.get('/test')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

