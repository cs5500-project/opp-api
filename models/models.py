from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Float

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)


class Cards(Base):
    __tablename__ = "cards"
    user_id = Column(Integer, ForeignKey("users.id")) 
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String, unique=True)  # hashed card number
    type = Column(String)
    last_four_digits = Column(String, unique=True)  # to check if this card exists in db


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id")) 
    # card_id = Column(Integer, ForeignKey("cards.id"))
    time_created = Column(DateTime)
    time_updated = Column(DateTime)
    amount = Column(Float)
    status = Column(String)
