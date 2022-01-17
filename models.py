from sqlalchemy.sql import func
from database import Base
from sqlalchemy import Column, Integer, Float, DateTime, String


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    stockId = Column(Integer)
    amount = Column(Float)
    value = Column(Float)
    purchased = Column(DateTime, default=func.now())


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String, unique=True)
    email = Column(String)
    password = Column(String)