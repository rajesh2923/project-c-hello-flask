import pytest
from app import app  # assumes your Flask app is created in app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_status_code(client):
    """Basic test: GET / should return 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_index_content(client):
    """Ensure the homepage contains expected text."""
    response = client.get('/')
    assert b"Hello, World" in response.data  # adjust to your response

