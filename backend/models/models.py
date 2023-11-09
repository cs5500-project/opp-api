from sqlalchemy import Column, Integer, String
from database import Base
# from datetime import datetime

# define the enum list for card type, notice the card type is string now, todo
import enum 
class Card_Type (enum.Enum):
    credit_card = 1
    debit_card = 2
    
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    

# class Consumers(Users):
#     __tablename__ = "consumers"

#     id = Column(Integer, primary_key=True)
#     username = Mapped

# Create database for orders
class Orders(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    amount_paid = Column(Integer)
    order_detail = Column(String)
    id = Column(Integer)
    order_time = Column(String)

# create database for cards
class Cards(Base):
    __tablename__ = "cards"

    card_number = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    expiration_date = Column(String)
    cvv = Column(Integer)
    type = Column(String)
    # user id? 