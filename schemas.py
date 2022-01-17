from pydantic import BaseModel
from datetime import datetime


class Transaction(BaseModel):
    stockId: int
    amount: float
    value: float


class TransactionShow(Transaction):

    class Config:
        orm_mode = True


class User(BaseModel):
    userName: str
    email: str
    password: str


class ShowUser(BaseModel):
    userName: str
    email: str

    class Config:
        orm_mode = True
