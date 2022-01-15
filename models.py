from database import  Base
from sqlalchemy import Column, Integer, Float, DateTime


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    stockId = Column(Integer)
    amount = Column(Float)
    value = Column(Float)
    purchased = Column(DateTime)
