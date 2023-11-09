from pydantic import BaseModel
from typing import Optional


class UserCreateModel(BaseModel):
    username: str
    password: str
    type: str


class UserReturnModel(BaseModel):
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class OrderModel(BaseModel):
    amount_paid: int
    detail: str


class OrderUpdateModel(BaseModel):
    amount_paid: Optional[int] = None
    detail: Optional[str] = None
