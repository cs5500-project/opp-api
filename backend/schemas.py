from pydantic import BaseModel


class UserCreateModel(BaseModel):
    username: str
    password: str

class UserReturnModel(BaseModel):
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

  
class OrderCreateModel(BaseModel):
    amount_paid : int
    order_detail : str
    order_time : int


class OrderReturnModel(BaseModel):
    order_id: int
    

class OrderUpdateModel(BaseModel):
    amount_paid : int
    order_detail : str
    order_time : int
    

