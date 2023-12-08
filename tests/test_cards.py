from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def login_user():
    res = client.post("/auth/login", data={"username": "hyojin", "password": "12345"})
    return res.json().get("access_token")


# test create a new card that does not exist
# this test passed and create a card in bd


def test_create_card():
    token = login_user()
    response = client.post(
        "/card",
        json={"card_number": "4111112014267661", "type": "credit"},
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 201


# test create a card that already exists
def test_create_card_exists():
    token = login_user()
    response = client.post(
        "/card",
        json={"card_number": "4111112014267661", "type": "debit"},
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 302


# test get cards
def test_get_cards():
    token = login_user()
    response = client.get("/card", headers={"Authorization": "Bearer " + token})
    assert response.status_code == 200


# test get card by id
def test_get_card_by_id():
    token = login_user()
    response = client.get(
        "/card/id/5/",
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 200
    assert response.json() == {"last_four_digits": "2729", "type": "debit", "id": 5}


# test get card by four digits
def test_get_card_by_four_digits_number():
    token = login_user()
    response = client.get(
        "/card/card-number/2729",
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 200
    assert response.json() == {"last_four_digits": "2729", "type": "debit", "id": 5}


def test_delete_card_by_id():
    token = login_user()
    res = client.post(
        "/card",
        json={"card_number": "4111112014267661", "type": "credit"},
        headers={"Authorization": "Bearer " + token},
    )
    id_res = client.get(
        "/card/card-number/7661",
        headers={"Authorization": "Bearer " + token},
    )
    id = id_res.json()["id"]
    response = client.delete(
        f"/card/id/{id}", headers={"Authorization": "Bearer " + token}
    )
    assert response.status_code == 204


# test delete card by number -- last four digits
def test_delete_card_by_number():
    token = login_user()
    res = client.post(
        "/card",
        json={"card_number": "4111112014267661", "type": "credit"},
        headers={"Authorization": "Bearer " + token},
    )
    response = client.delete(
        "/card/card-number/7661", headers={"Authorization": "Bearer " + token}
    )
    assert response.status_code == 200
