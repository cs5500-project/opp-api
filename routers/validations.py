"""
helper class - validations: amount validations and fraudulent check using luhn's algo.
making a call to aws lambda functions.

"""
import requests
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from routers.auth import get_current_user, check_user_authentication

router = APIRouter(prefix="/validate", tags=["validate"])

user_dependency = Annotated[dict, Depends(get_current_user)]


# @router.post("/fraudulent/", status_code=status.HTTP_201_CREATED)
async def validate_card_number_luhn_algo(card_number: str, user: user_dependency):
    check_user_authentication(user)

    url = "https://c3jkkrjnzlvl5lxof74vldwug40pxsqo.lambda-url.us-west-2.on.aws"
    data = {"card_number": card_number}
    response = requests.post(url, json=data)

    return response.json()


# @router.post("/balance/", status_code=status.HTTP_201_CREATED)  # card_number, amt
async def validate_card_number_with_amount(card_number: str, amt: float, user: user_dependency):
    check_user_authentication(user)

    url = "https://223didiouo3hh4krxhm4n4gv7y0pfzxk.lambda-url.us-west-2.on.aws"
    data = {"card_number": card_number, "amt": amt}
    response = requests.post(url, json=data)

    return response.json()


async def check_validations(card_number, amt, user):
    """ (helper) card number and amount validation of transactions"""
    res1 = await validate_card_number_luhn_algo(card_number, user)

    res2 = await validate_card_number_with_amount(card_number, amt, user)

    if res1.get("success") == "false" or res2.get("success") == "false":
        raise HTTPException(status_code=400, detail="Validations Failed")



