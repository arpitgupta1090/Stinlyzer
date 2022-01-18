from pydantic import BaseModel
from typing import List


class Transaction(BaseModel):
    stockId: int
    amount: float
    value: float
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


class TransactionShow(BaseModel):
    stockId: int
    amount: float
    value: float
    user_id: int
    user: UserTransaction

    class Config:
        orm_mode = True


class Stock(BaseModel):
    name: str
    symbol: str
    exchange: str
    price: float


class ShowStock(Stock):
    class Config:
        orm_mode = True
