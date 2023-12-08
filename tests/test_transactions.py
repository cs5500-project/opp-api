from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def login_user():
    res = client.post("/auth/login", data={"username": "hyojin", "password": "12345"})
    return res.json().get("access_token")


def test_create_transaction_good():
    token = login_user()
    response = client.post(
        "/transaction",
        json={"card_number": "4111112014267661", "amt": 123, "card_type": "debit"},
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 200


def test_create_transaction_bad():
    token = login_user()
    response = client.post(
        "/transaction",
        json={"card_number": "4111112014267660", "amt": 123, "card_type": "debit"},
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 400


def test_create_transaction_overdraft():
    token = login_user()
    response = client.post(
        "/transaction",
        json={"card_number": "4111112014267661", "amt": 10001, "card_type": "debit"},
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 400


def test_create_transaction_overdraft_and_bad_number():
    token = login_user()
    response = client.post(
        "/transaction",
        json={"card_number": "4111112014267660", "amt": 10001, "card_type": "debit"},
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 400


def test_check_and_update_status_credit():
    token = login_user()
    response = client.put("/transaction/", headers={"Authorization": "Bearer " + token})
    assert response.status_code == 202


def test_get_current_balance():
    token = login_user()
    response = client.get(
        "/transaction/processed/balance", headers={"Authorization": "Bearer " + token}
    )
    assert response.status_code == 200


def test_get_current_balance_with_start_end_dates():
    token = login_user()
    response = client.get(
        "/transaction/processed/balance/2023-11-11%2000%3A00%3A00/2023-11-14%2023%3A59%3A00/",
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 200


def test_get_all_transactions():
    token = login_user()
    response = client.get(
        "/transaction/transaction-list/all/",
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 200


def test_get_all_processed_transactions():
    token = login_user()
    response = client.get(
        "/transaction/transaction-list/processed/",
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 200


def test_get_all_pending_transactions():
    token = login_user()
    response = client.get(
        "/transaction/transaction-list/pending/",
        headers={"Authorization": "Bearer " + token},
    )
    assert (
        response.status_code == 404
    )  # becasue there is no pending transaction in the database so it should return code 404


def test_get_transaction_by_id():
    token = login_user()
    response = client.get(
        "/transaction/1/", headers={"Authorization": "Bearer " + token}
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "user_id": 7,
        "amount": 123,
        "status": "processed",
        "time_created": "2023-12-07T21:01:35.220012",
        "time_updated": "2023-12-07T21:01:35.220012",
    }


def test_delete_transaction_by_id():
    token = login_user()
    my_transactions = client.get(
        "/transaction/transaction-list/all/",
        headers={"Authorization": "Bearer " + token},
    )
    response = client.delete(
        f"/transaction/{my_transactions.json()[-1].get('id')}/",
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code == 200
