from pydantic import BaseModel, StringConstraints, Field
from typing import Annotated, Optional, List
from datetime import datetime

from enum import Enum
from decimal import Decimal


class UserCreateModel(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class OrderModel(BaseModel):
    amount_paid: int
    detail: str


class OrderUpdateModel(BaseModel):
    amount_paid: Optional[int] = None
    detail: Optional[str] = None


class CardType(str, Enum):
    credit = "credit"
    debit = "debit"


class CardModel(BaseModel):
    card_number: Annotated[str, StringConstraints(min_length=16, max_length=16)]
    type: CardType = CardType.credit


class CardUpdateModel(BaseModel):
    card_number: Optional[
        Annotated[str, StringConstraints(min_length=16, max_length=16)] | None
    ] = None
    type: Optional[CardType | None] = None


class TransationStatus(str, Enum):
    pre_auth = "pre-authantication"
    failed = "failed"
    pending = "pending"
    completed = "completed"


class TransactionCreateModel(BaseModel):
    user_id: int
    amount: Decimal = Field(max_digits=9, decimal_places=2)
    card_id: int
    status: TransationStatus = TransationStatus.pre_auth
    time_created: datetime = datetime.now()


class TransactionModel(BaseModel):
    id: int
    user_id: int
    amount: Decimal = Field(max_digits=9, decimal_places=2)
    card_id: int
    status: TransationStatus


class TransactionCollection(BaseModel):
    transactions: List[TransactionModel]
