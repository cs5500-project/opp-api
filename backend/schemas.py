from pydantic import BaseModel, Field  # StringConstraints: will be deprecated in Pydantic 3.0
from typing import Annotated, Optional


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


class CardModel(BaseModel):
    card_number: Annotated[str, Field(min_length=16, max_length=16)]
    type: str


class CardUpdateModel(BaseModel):
    card_number: Annotated[str, Field(min_length=16, max_length=16)] = None
    type: str = None
