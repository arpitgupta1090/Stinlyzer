from pydantic import BaseModel
from datetime import datetime


class Transaction(BaseModel):
    stock_id: int
    amount: float
    value: float
    purchased: datetime
