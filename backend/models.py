from sqlalchemy import Column, Integer, String
from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)


# class Consumers(Users):
#     __tablename__ = "consumers"

#     id = Column(Integer, primary_key=True)
#     username = Mapped
