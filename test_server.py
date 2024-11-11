import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from main import app
from shared.database import get_db

@pytest.fixture
def mock_db():
    db = MagicMock()
    yield db

@pytest.fixture
def client(mock_db):
    app.dependency_overrides[get_db] = lambda: mock_db
    with TestClient(app) as c:
        yield c

def test_api_working(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "API está rodando."

def test_api_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == "Saúde da API em dia"
