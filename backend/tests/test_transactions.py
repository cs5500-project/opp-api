from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_create_transaction():
    response = client.post("/transaction")
    assert response.status_code == 201




