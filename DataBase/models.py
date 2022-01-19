from DataBase.database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    stockId = Column(Integer, ForeignKey("stocks.id"))
    price = Column(Float)
    quantity = Column(Integer)
    purchased_date = Column(String, default='YYYYMMDD')
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="transactions")
    stock = relationship("Stock", back_populates="transactions")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String, unique=True)
    email = Column(String)
    password = Column(String)
    transactions = relationship("Transaction", back_populates="user")
    sectors = relationship("Sector", back_populates="user")
    segments = relationship("Segment", back_populates="user")


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    symbol = Column(String, unique=True)
    exchange = Column(String)
    price = Column(Float, default=0)
    sector = Column(String, ForeignKey("sectors.sector"))
    segment = Column(String, ForeignKey("segments.segment"))
    tags = Column(String, nullable=True)

    transactions = relationship("Transaction", back_populates="stock")
    sectors = relationship("Sector", back_populates="stocks")
    segments = relationship("Segment", back_populates="stocks")


class Sector(Base):
    __tablename__ = "sectors"

    sector = Column(String, primary_key=True, index=True)
    target = Column(Float, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="sectors")
    stocks = relationship("Stock", back_populates="sectors")


class Segment(Base):
    __tablename__ = "segments"

    segment = Column(String, primary_key=True, index=True)
    target = Column(Float, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="segments")
    stocks = relationship("Stock", back_populates="segments")


