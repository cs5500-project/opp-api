from fastapi.testclient import TestClient
from models.models import Cards
from database import db_dependency

from ..main import app

client = TestClient(app)


def login_user():
    res = client.post("/auth/login", data={"username": "yuhan", "password": "12345"})
    return res.json().get("access_token")
# test create a new card that does not exist
# this test passed and create a card in bd

# def test_create_card():
#     token = login_user()
#     response = client.post(
#         "/card",
#         json={"card_number": "4147202464191053","type": "debit"},
#         headers={"Authorization": "Bearer " + token},
#     )
#     assert response.status_code == 201
    

# test create a card that already exists
def test_create_card_exists():
    token = login_user()
    response = client.post(
        "/card",
        json={"card_number": "4147202464191053","type": "debit"},
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 302

# test get cards
def test_get_cards():
    token = login_user()
    response = client.get(
        "/card", headers={"Authorization": "Bearer " + token}
    )
    assert response.status_code == 200
    
# test get card by id
def test_get_card_by_id():
    token = login_user()
    response = client.get(
        "/card/id/2",
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 200
    assert response.json() == {
        "last_four_digits": "1053",
        "type": "debit",
        "id" : 2
    }
    
# test get card by four digits
def test_get_card_by_four_digits_number():
    token = login_user()
    response = client.get(
        "/card/card-number/1053",
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 200
    assert response.json() == {
        "last_four_digits": "1053",
        "type": "debit",
        "id" : 2
    }
    

# test delete card by id
# the card is deleted now its 404 
def test_delete_card_by_id():
    token = login_user()
    response = client.delete(
        "/card/id/1", headers={"Authorization": "Bearer " + token}
    )
    assert response.status_code == 204
    
# test delete card by number -- last four digits 
# now its 404 since its deleted, you can resume the card by running create

def test_delete_card_by_number():
    token = login_user()
    response = client.delete(
        "/card/card-number/1053", headers={"Authorization": "Bearer " + token}
    )
    assert response.status_code == 204