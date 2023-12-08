from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from starlette import status

from schemas import CardModel, CardResponseModel
from database import db_dependency
from models.models import Cards
from routers.auth import get_current_user, check_user_authentication
from passlib.context import CryptContext

router = APIRouter(prefix="/card", tags=["card"])

user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_card(request: CardModel, db: db_dependency, user: user_dependency):
    check_user_authentication(user)

    # match the last 4 digits of the card (to check if this card exists in db)
    last_four = request.card_number[-4:]
    found_card = db.query(Cards).filter(last_four == Cards.last_four_digits).first()
    if found_card:
        raise HTTPException(status_code=302, detail="existing card found.")
    new_card = Cards(card_number=bcrypt_context.hash(request.card_number),
                     type=request.type,
                     user_id=user.get("id"),
                     last_four_digits=last_four)
    db.add(new_card)
    db.commit()


@router.get("/id/{id}/", status_code=status.HTTP_200_OK, response_model=CardResponseModel)
async def get_card_by_id(id: int, db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    found_card = db.query(Cards).filter(Cards.id == id).filter(Cards.user_id == id) .first()
    if not found_card:
        raise HTTPException(status_code=404, detail=f"Card {id} does not exist.")
    # return {"last_four_digits": found_card.last_four_digits,
    #         "type": found_card.type,
    #         "id": found_card.id
    #         }
    return found_card


@router.get("/", status_code=status.HTTP_200_OK)
async def get_cards(db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    cards = db.query(Cards).filter(Cards.user_id == user.get("id")).all()
    if not cards:
        raise HTTPException(status_code=404, detail="there are no saved cards.")
    return cards


# Commented this put method b/c, when we normally update an existing card,
# we update expiration number, name on the card or address.
# If a new card number is needed, create one.

# @router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
# async def update_card(
#     id: int, request: CardModel, db: db_dependency, user: user_dependency
# ):
#     check_user_authentication(user)
#     found_card = db.query(Cards).filter(Cards.id == id).first()
#     if not found_card:
#         raise HTTPException(status_code=404, detail=f"Card {id} does not exist.")
#
#     # make the update
#     found_card.card_number = request.card_number or found_card.card_number # rehash for the new card number
#     found_card.type = request.type or found_card.type
#
#     db.add(found_card)
#     db.commit()


@router.get("/card-number/{four_digits}/",
            status_code=status.HTTP_200_OK,
            response_model=CardResponseModel)
async def get_card_by_four_digits_number(
    four_digits: str, db: db_dependency, user: user_dependency
):
    check_user_authentication(user)
    found_card = db.query(Cards).filter(Cards.last_four_digits == four_digits).first()
    if not found_card:
        raise HTTPException(
            status_code=404, detail=f"Card with the last four digits {four_digits} does not exist."
        )
    # return {"last_four_digits": found_card.last_four_digits,
    #         "type": found_card.type,
    #         "id": found_card.id
    #         }
    return found_card


@router.delete("/id/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_card_by_id(id: int, db: db_dependency, user: user_dependency):
    check_user_authentication(user)
    found_card = db.query(Cards).filter(Cards.id == id).filter(Cards.user_id == id).delete()
    if not found_card:
        raise HTTPException(status_code=404, detail=f"Card {id} does not exist.")

    db.commit()


@router.delete("/card-number/{four_digits}/", status_code=status.HTTP_200_OK)
async def delete_card_by_number(
    four_digits: str, db: db_dependency, user: user_dependency
):
    check_user_authentication(user)
    found_card = db.query(Cards).filter(Cards.last_four_digits == four_digits).delete()
    if not found_card:
        raise HTTPException(
            status_code=404, detail=f"Card with the last four digits {four_digits} does not exist."
        )

    db.commit()
