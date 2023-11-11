from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from typing import Annotated
from fastapi import Depends


SQLALCHEMY_DB_URL = "sqlite:///./opp.db"

engine = create_engine(SQLALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
