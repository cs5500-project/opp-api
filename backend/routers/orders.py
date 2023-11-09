from fastapi import Path, Query, HTTPException, APIRouter
from pydantic import BaseModel, Field
from starlette import status
from fastapi import Depends, FastAPI, HTTPException
from typing import Annotated


# from datetime import timedelta, datetime

from models.models import Orders
from database import db_dependency
from schemas import *
from routers.auth import get_current_user

# this system faces merchants only! So all order actions are based on merchant side!

router = APIRouter(prefix="/orders", tags=["orders"])

user_dependency = Annotated[dict, Depends(get_current_user)]


# # validate user with returning a token -- for future action after validation
# def validate_user(db: db_dependency, token: str = Query(..., description="JWT token")):
#     decoded_token = auth.get_current_user(token)
#     print(decoded_token)
#     if not decoded_token:
#         raise HTTPException(status_code=401, detail="Invalid token")

#     # check whether the user is in db
#     # print(decoded_token)
#     user = db.query(Users).filter(Users.id == decoded_token["id"]).first()
#     if not user:
#         return False
#     else:
#         return user


@router.get("/{id}")
async def get_order(db: db_dependency, id: int, user: user_dependency):
    order = (
        db.query(Orders)
        .filter(Orders.id == id)
        .filter(Orders.user_id == user.get("id"))
        .first()
    )
    return order


#  from fastapi import Depends, HTTPException
@router.post("/create_order", status_code=status.HTTP_201_CREATED)
async def create_order(
    db: db_dependency,
    create_order_request: OrderCreateModel,
    user: user_dependency,  # Assuming oauth2_bearer is your dependency to get the JWT token
):
    """Create a new order"""
    # Check if the order already exists
    existing_order = (
        db.query(Orders)
        .filter(
            Orders.amount_paid == create_order_request.amount_paid,
            Orders.user_id == user.get("id"),
            Orders.order_detail == create_order_request.order_detail,
            Orders.order_time == create_order_request.order_time,
        )
        .first()
    )

    if existing_order:
        raise HTTPException(status_code=400, detail="Order already exists")

    # Create a new order
    create_order_model = Orders(
        **create_order_request.model_dump(),
        user_id=user.get("id"),  # Associate the order with the user ID from the token
    )

    db.add(create_order_model)
    db.commit()
    # db.refresh(create_order_model)
    # return create_order_model


@router.put("/update_order/{id}", status_code=status.HTTP_201_CREATED)
async def update_order(
    db: db_dependency,
    update_order_request: OrderUpdateModel,
    id: int,
    user: user_dependency,  # Assuming oauth2_bearer is your dependency to get the JWT token
):
    # Check if the desired order exists
    existing_order = (
        db.query(Orders)
        .filter(
            Orders.id == id,
        )
        .first()
    )

    if not existing_order:
        raise HTTPException(status_code=400, detail="Order does not exists")

    # Create a new order
    update_order_model = Orders(
        amount_paid=update_order_request.amount_paid,
        order_detail=update_order_request.order_detail,
        order_time=update_order_request.order_time,
        # all users are not allowed to update the user id
    )

    db.query(Orders).filter(Orders.id == id).update(
        {
            "amount_paid": update_order_request.amount_paid,
            "order_detail": update_order_request.order_detail,
            "order_time": update_order_request.order_time,
        }
    )

    db.commit()
    return update_order_model


# merchant delete order
@router.delete("/delete_order/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_orders(db: db_dependency, id: int, user: user_dependency):
    # Check if the desired order exists
    existing_order = (
        db.query(Orders)
        .filter(
            Orders.id == id,
        )
        .first()
    )
    if not existing_order:
        raise HTTPException(status_code=400, detail="Order does not exists")
    if existing_order.user_id != user.get("id"):
        raise HTTPException(status_code=401, detail="Unauthorized user")

    db.query(Orders).filter(Orders.id == id).delete()
    db.commit()
