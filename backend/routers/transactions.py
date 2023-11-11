## card todo Yuhan
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from starlette import status
from datetime import datetime

from schemas import (
    TransactionCreateModel,
    TransactionModel,
    TransationStatus,
    TransactionCollection,
)
from database import db_dependency
from models.models import Transactions
from routers.auth import get_current_user, check_user_authentication


router = APIRouter(prefix="/transaction", tags=["transaction"])

user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_transaction(
    request: TransactionCreateModel, db: db_dependency, user: user_dependency
):
    check_user_authentication(user)

    new_transaction = Transactions(**request.model_dump())
    db.add(new_transaction)
    db.commit()


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_transaction(
    db: db_dependency,
    user: user_dependency,
    id: int,
    status: TransationStatus | None = None,
    amount: int | None = None,
):
    check_user_authentication
    transaction = db.query(Transactions).filter(Transactions.id == id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail=f"Transaction {id} does not exist.")
    transaction.status = status or transaction.status
    transaction.amount = amount or transaction.amount
    transaction.time_updated = datetime.now()
    db.commit()


@router.get(
    "/by-id/{id}", status_code=status.HTTP_200_OK, response_model=TransactionModel
)
async def get_by_id(db: db_dependency, user: user_dependency, id: int):
    check_user_authentication(user)
    transaction = (
        db.query(Transactions)
        .filter(Transactions.id == id)
        .first()
    )
    if not transaction:
        raise HTTPException(status_code=404, detail=f"Transaction {id} does not exist.")
    if transaction.user_id != user.get("id"):
        raise HTTPException(status_code=400, detail="Unauthorized.")
    return transaction


@router.get(
    "/by-user-id",
    status_code=status.HTTP_200_OK,
)
async def get_by_user_id(db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    transactions = db.query(Transactions).filter(Transactions.user_id == user.get("id")).all()
    print(transactions.__class__)
    if not transactions:
        raise HTTPException(
            status_code=404,
            detail=f"Transaction with user ID: {user.get("id")} does not exist.",
        )
    return transactions


@router.delete("/{id}", status_code=status.HTTP_200_OK
)
async def delete_transaction(id: int, db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    db.query(Transactions).filter(Transactions.id == id).delete()
    db.commit()
