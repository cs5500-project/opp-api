from fastapi.testclient import TestClient
import string
import random

from main import app

client = TestClient(app)


def login_user():
    res = client.post("/auth/login", data={"username": "hyojin", "password": "12345"})
    return res.json().get("access_token")


def test_create_user():
    username = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    password = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    response = client.post(
        "/auth",
        json={"username": str(username), "password": str(password)},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 201


def test_create_user_duplicate_name():
    response = client.post(
        "/auth",
        json={"username": "xiaolin", "password": "1234"},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 400
