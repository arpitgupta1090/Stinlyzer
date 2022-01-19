from pydantic import BaseModel
from typing import List
from enums import Sector, Segment


class Transaction(BaseModel):
    stockId: int
    price: float
    quantity: int
    purchased_date: str
    user_id: int


class User(BaseModel):
    userName: str
    email: str
    password: str


class UserTransaction(BaseModel):
    userName: str
    email: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    userName: str
    email: str
    transactions: List

    class Config:
        orm_mode = True


class Stock(BaseModel):
    name: str
    symbol: str
    exchange: str
    price: float
    sector: Sector
    segment: Segment
    tags: str


class StockUpdate(BaseModel):
    sector: Sector
    segment: Segment
    tags: str

    class Config:
        orm_mode = True


class ShowStock(Stock):
    transactions: List

    class Config:
        orm_mode = True


class ShowStockTransaction(Stock):

    class Config:
        orm_mode = True


class TransactionShow(BaseModel):
    user_id: int
    user: UserTransaction
    stockId: int
    stock: ShowStockTransaction
    price: float
    quantity: int
    purchased_date: str

    class Config:
        orm_mode = True
