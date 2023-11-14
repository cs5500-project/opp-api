from pydantic import BaseModel
from typing import Union
from datetime import datetime

from enum import Enum


class UserCreateModel(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# class OrderModel(BaseModel):
#     amount_paid: int
#     detail: str
#
#
# class OrderUpdateModel(BaseModel):
#     amount_paid: Union[int, None] = None
#     detail: Union[str, None] = None


class CardType(str, Enum):
    credit = "credit"
    debit = "debit"


class CardModel(BaseModel):
    card_number: str
    type: CardType


class CardResponseModel(BaseModel):
    last_four_digits: str
    type: CardType
    id: int

# class CardUpdateModel(BaseModel):
#     # Union[type1, type2] : python 3.9 doesn't allow X | Y
#     card_number: Union[str, None] = None  # hashed - not irreversible for security purpose
#     type: Union[CardType, None] = None


class TransactionStatus(str, Enum):
    in_processing = "in-processing"
    processed = "processed"


class TransactionCreateModel(BaseModel):
    """ authenticated user is sending money to his/her account.
     db needs to save user_id to send money, but user doesn't have to enter it in a request body"""
    # card_id: int
    card_number: str
    amt: float
    card_type: CardType


class TransactionResponseModel(BaseModel):
    id: int
    user_id: int
    amount: float
    # card_id: int
    status: TransactionStatus
    time_created: datetime
    time_updated: datetime
