import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_stock(client):
    response = client.get('/stock/AAPL')
    assert response.status_code == 200
    assert 'company_name' in response.json

def test_post_stock(client):
    response = client.post('/stock/AAPL', json={"amount": 5})
    assert response.status_code == 201
    assert 'message' in response.json