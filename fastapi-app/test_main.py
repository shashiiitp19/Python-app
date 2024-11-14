from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add():
    response = client.get("/add?a=1&b=2")
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_multiply():
    response = client.get("/multiply?a=4&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 20}

