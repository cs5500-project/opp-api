from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

from schemas import *
from database import SessionLocal
from database import db_dependency
from models.models import Users

router = APIRouter(prefix="/auth", tags=["auth"])

""" this is the key and algo I used. They are in .env file - not sure if you also need this so left here
 Later we should remove this
# SECRET_KEY = "c69c30b9ea4597dd4f5b3824ed4f26bf07b84ea6de79bfa245be395d965d878b"
# ALGORITHM = "HS256"
"""

load_dotenv()  # take environment variables from .env.
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: UserCreateModel):
    found_user = (
        db.query(Users).filter(Users.username == create_user_request.username).first()
    )
    if found_user:
        raise HTTPException(
            status_code=400, detail="Username already exists"
        )  # 400: bad request
    """registering user"""
    new_user = Users(
        username=create_user_request.username,
        hashed_password=bcrypt_context.hash(create_user_request.password),
    )
    db.add(new_user)
    db.commit()


@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    """logging in user"""
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user"
        )
    # Create token from the authenticated user
    token = access_token = create_access_token(
        user.id, user.username, timedelta(minutes=30)
    )

    return {"access_token": token, "token_type": "bearer"}


def authenticate_user(username: str, password: str, db: db_dependency):
    """checking match of username and password"""
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False

    return user


def create_access_token(user_id: int, username: str, expires_delta: timedelta):
    """creating a token for an authenticated user"""
    claims = {"id": user_id, "username": username}
    expires = datetime.utcnow() + expires_delta
    claims.update({"exp": expires})
    token = jwt.encode(claims, SECRET_KEY, algorithm=ALGORITHM)
    return token


# async
def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    """get the logged-in user"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("id")
        username: str = payload.get("username")

        if username is None or id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Can't authenticate the user",
            )
        return {"username": username, "id": id, "type": type}
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Fail to authenticate the user.",
        )


def check_user_authentication(user):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
