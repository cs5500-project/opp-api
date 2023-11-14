from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from starlette import status
from datetime import datetime, timedelta

from ..schemas import (
    TransactionCreateModel,
    TransactionResponseModel,
    TransactionStatus
)
from ..database import db_dependency
from ..models.models import Transactions
from ..routers.auth import get_current_user, check_user_authentication
from ..routers.validations import check_validations

router = APIRouter(prefix="/transaction", tags=["transaction"])

user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_transaction(request: TransactionCreateModel,
                             user: user_dependency,
                             db: db_dependency):
    check_user_authentication(user)

    card_number = request.card_number
    amt = request.amt

    # raises error if validation not successful- needed for an immediate rejection
    await check_validations(card_number, amt, user)

    # create transaction
    user_id = user.get("id")
    card_type = request.card_type
    time_created = datetime.now()
    transaction_status = TransactionStatus.in_processing

    if card_type == "credit":  # note: for testing change timedelta value to "minutes=1"
        time_completed = time_created + timedelta(days=3)  # at least 2 days so on day 3 we can update to 'processed'
    else:
        time_completed = time_created
        transaction_status = TransactionStatus.processed

    new_transaction = Transactions(user_id=user_id, amount=amt,
                                   time_created=time_created,
                                   time_updated=time_completed,
                                   status=transaction_status)
    db.add(new_transaction)
    db.commit()


@router.put('/', status_code=status.HTTP_202_ACCEPTED)
async def check_status_and_update_for_credit(db: db_dependency, user: user_dependency):
    check_user_authentication(user)

    time_now = datetime.now()
    transactions_to_update_status = db.query(Transactions).filter(
        Transactions.status == "in-processing"). \
        filter(Transactions.user_id == user.get("id")). \
        filter(time_now >= Transactions.time_updated).all()

    # loop transactions, update status to processed
    if (not transactions_to_update_status or len(transactions_to_update_status)) == 0:
        return
    if len(transactions_to_update_status) == 1:
        transactions_to_update_status[0].status = "processed"
        db.add(transactions_to_update_status[0])
        return
    for i in range(len(transactions_to_update_status)):
        transactions_to_update_status[i].status = "processed"
        db.add(transactions_to_update_status[i])

    db.commit()


@router.get("/processed/balance/", status_code=status.HTTP_200_OK)
async def get_current_balance_processed_transactions(db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    # before getting all processed transactions,
    # run this method to update status (for credit) first
    await check_status_and_update_for_credit(db, user)

    # then query for all processed transactions
    processed_transactions = db.query(Transactions).\
        filter(Transactions.status == "processed").\
        filter(Transactions.user_id == user.get("id"))

    # loop transactions and add amount
    current_balance = 0
    for transaction in processed_transactions:
        current_balance += transaction.amount
    current_balance = "%.2f" % current_balance
    return current_balance


@router.get("/processed/balance/{start}/{end}/", status_code=status.HTTP_200_OK)
async def get_current_balance_processed_transactions_with_time(db: db_dependency,
                                                            user: user_dependency,
                                                            start: datetime,
                                                            end: datetime):
    # start format: 2023-11-13 00:00:00 end format: 2023-11-13 23:59:59
    # TODO: currently accepting only the format like above. I think we can handle how we get
    #  the type of datetime in the front-end or figure out how we can handle start & date
    #  more flexible
    check_user_authentication(user)
    # before getting all processed transactions,
    # run this method to update status (for credit) first
    await check_status_and_update_for_credit(db, user)

    # then query for all processed transactions between start and end dates
    processed_transactions = db.query(Transactions).\
        filter(Transactions.status == "processed").\
        filter(Transactions.user_id == user.get("id")).\
        filter(Transactions.time_updated.between(start, end))

    # loop transactions and add amount
    current_balance = 0
    for transaction in processed_transactions:
        current_balance += transaction.amount
    current_balance = "%.2f" % current_balance
    return current_balance


@router.get("/transaction-list/all/", status_code=status.HTTP_200_OK)
async def get_by_user_id(db: db_dependency, user: user_dependency):
    """ getting all transactions of this user """
    check_user_authentication(user)
    transactions = db.query(Transactions).filter(Transactions.user_id == user.get("id")).all()
    if not transactions:
        raise HTTPException(
            status_code=404,
            detail=f"Transaction with user ID: {user.get('id')} does not exist."
        )
    return transactions


@router.get("/transaction-list/processed/", status_code=status.HTTP_200_OK)
async def get_all_processed_transactions(db: db_dependency, user: user_dependency):
    check_user_authentication(user)

    transactions = db.query(Transactions).\
        filter(Transactions.user_id == user.get("id")).\
        filter(Transactions.status == "processed").all()
    if not transactions:
        raise HTTPException(
            status_code=404,
            detail=f"Transaction with user ID: {user.get('id')} does not exist."
        )

    return transactions


@router.get("/transaction-list/pending/", status_code=status.HTTP_200_OK)
async def get_all_pending_transactions(db: db_dependency, user: user_dependency):
    """ getting all pending/in-processing transactions of this usr """
    check_user_authentication(user)

    transactions = db.query(Transactions).\
        filter(Transactions.user_id == user.get("id")).\
        filter(Transactions.status == "in-processing").all()
    if not transactions:
        raise HTTPException(
            status_code=404,
            detail=f"Transaction with user ID: {user.get('id')} does not exist."
        )

    return transactions


@router.get("/{id}/", status_code=status.HTTP_200_OK, response_model=TransactionResponseModel)
async def get_by_id(db: db_dependency, user: user_dependency, id: int):
    check_user_authentication(user)
    transaction = (db.query(Transactions).
                   filter(Transactions.id == id).
                   filter(Transactions.user_id == user.get("id")).first())
    if not transaction:
        raise HTTPException(status_code=404, detail=f"Transaction {id} does not exist.")

    return transaction


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_transaction(id: int, db: db_dependency, user: user_dependency):
    check_user_authentication(user)

    transaction = (db.query(Transactions).
                   filter(Transactions.id == id).
                   filter(Transactions.user_id == user.get("id")).first())
    if not transaction:
        raise HTTPException(status_code=404, detail=f"Transaction {id} does not exist.")

    db.query(Transactions).filter(Transactions.id == id).\
        filter(Transactions.user_id == user.get("id")).delete()

    db.commit()

# I commented this put method because once a transaction is made,
# it shouldn't be allowed for users to change detail of a created transaction
# (updating credit card status is done in "check_status_and_update_for_credit")
# @router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
# async def update_transaction(
#     db: db_dependency,
#     user: user_dependency,
#     id: int,
#     status: TransationStatus | None = None,
#     amount: int | None = None,
# ):
#     check_user_authentication()
#     transaction = db.query(Transactions).filter(Transactions.id == id).first()
#     if not transaction:
#         raise HTTPException(status_code=404, detail=f"Transaction {id} does not exist.")
#     transaction.status = status or transaction.status
#     transaction.amount = amount or transaction.amount
#     transaction.time_updated = datetime.now()
#     db.commit()
