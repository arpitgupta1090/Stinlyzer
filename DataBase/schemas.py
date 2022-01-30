from pydantic import BaseModel
from typing import List, Optional
import enums


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
    sector: enums.Sector
    segment: enums.Segment
    tags: str


class StockUpdate(BaseModel):
    sector: enums.Sector
    segment: enums.Segment
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


class Sector(BaseModel):
    sector: enums.Sector
    target: float
    user_id: int


class ShowSector(Sector):
    class Config:
        orm_mode = True


class Segment(BaseModel):
    segment: enums.Segment
    target: float
    user_id: int


class ShowSegment(Segment):
    class Config:
        orm_mode = True


class Plot(BaseModel):
    flag: enums.Flag
    data: enums.Data

