## card todo Yuhan
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from starlette import status

from schemas import CardModel, CardUpdateModel
from database import db_dependency
from models.models import Cards
from routers.auth import get_current_user, check_user_authentication

router = APIRouter(prefix="/card", tags=["card"])

user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_card(request: CardModel, db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    found_card = (
        db.query(Cards).filter(Cards.card_number == request.card_number).first()
    )
    if found_card:
        raise HTTPException(status_code=400, detail="Card number is already exists.")

    new_card = Cards(
        card_number=request.card_number,
        type=request.type,
    )
    db.add(new_card)
    db.commit()


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_card(
    id: int, request: CardUpdateModel, db: db_dependency, user: user_dependency
):
    check_user_authentication(user)
    found_card = db.query(Cards).filter(Cards.id == id).first()
    if not found_card:
        raise HTTPException(status_code=404, detail=f"Card {id} does not exist.")

    found_card.card_number = request.card_number or found_card.card_number
    found_card.type = request.type or found_card.type

    db.commit()


@router.get("/id/{id}", status_code=status.HTTP_200_OK, response_model=CardModel)
async def get_by_id(id: int, db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    found_card = db.query(Cards).filter(Cards.id == id).first()
    if not found_card:
        raise HTTPException(status_code=404, detail=f"Card {id} does not exist.")
    return found_card


@router.get(
    "/card-number/{card_number}",
    status_code=status.HTTP_200_OK,
    response_model=CardModel,
)
async def get_by_number(card_number: str, db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    found_card = db.query(Cards).filter(Cards.card_number == card_number).first()
    if not found_card:
        raise HTTPException(
            status_code=404, detail=f"Card {card_number} does not exist."
        )
    return found_card


@router.delete("/id/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(id: int, db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    found_card = db.query(Cards).filter(Cards.id == id).delete()
    if not found_card:
        raise HTTPException(status_code=404, detail=f"Card {id} does not exist.")


@router.delete(
    "/card-number/{card_number}",
    status_code=status.HTTP_200_OK,
)
async def get_by_number(card_number: str, db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    found_card = db.query(Cards).filter(Cards.card_number == card_number).delete()
    if not found_card:
        raise HTTPException(
            status_code=404, detail=f"Card {card_number} does not exist."
        )
