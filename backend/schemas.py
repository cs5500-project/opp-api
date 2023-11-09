from pydantic import BaseModel


class UserCreateModel(BaseModel):
    username: str
    password: str


class UserReturnModel(BaseModel):
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
