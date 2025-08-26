import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_soma(client):
    response = client.get("/soma?a=2&b=3")
    json_data = response.get_json()
    assert json_data["resultado"] == 5

def test_subtracao(client):
    response = client.get("/subtracao?a=10&b=4")
    json_data = response.get_json()
    assert json_data["resultado"] == 6

def test_multiplicacao(client):
    response = client.get("/multiplicacao?a=3&b=4")
    json_data = response.get_json()
    assert json_data["resultado"] == 12

def test_divisao(client):
    response = client.get("/divisao?a=20&b=5")
    json_data = response.get_json()
    assert json_data["resultado"] == 4
