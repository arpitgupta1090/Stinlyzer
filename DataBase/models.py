from sqlalchemy.sql import func
from DataBase.database import Base
from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    stockId = Column(Integer)
    amount = Column(Float)
    value = Column(Float)
    purchased = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="transactions")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String, unique=True)
    email = Column(String)
    password = Column(String)
    transactions = relationship("Transaction", back_populates="user")


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    symbol = Column(String, unique=True)
    exchange = Column(String)
    price = Column(float, default=0)

