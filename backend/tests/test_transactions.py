from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def login_user():
    res = client.post("/auth/login", data={"username": "hyojin", "password": "12345"})
    return res.json().get("access_token")


def test_create_transaction():
    token = login_user()
    response = client.post("/transaction", data={
                                                 "card_number": "4111112014267661",
                                                 "amt": 123,
                                                 "card_type": "debit"},
                           headers={"Authorization": "Bearer" + token})
    assert response.status_code == 201




