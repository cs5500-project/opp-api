from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database.database import SessionLocal
from models.models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

router = APIRouter(prefix="/auth", tags=["auth"])

""" this is the key and algo I used. They are in .env file - not sure if you also need this so left here
 Later we should remove this
# SECRET_KEY = "c69c30b9ea4597dd4f5b3824ed4f26bf07b84ea6de79bfa245be395d965d878b"
# ALGORITHM = "HS256"
"""

load_dotenv()  # take environment variables from .env.
os.environ.get("SECRET_KEY")
os.environ.get("ALGORITHM")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


class CreateUserRequest(BaseModel):
    username: str
    first_name: str
    surname: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

