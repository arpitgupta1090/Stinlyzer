from fastapi import APIRouter, Depends, status, HTTPException
from DataBase import schemas
from sqlalchemy.orm import Session
from DataBase.database import get_db
from custom_exceptions.exception import DuplicateUserException
from sqlalchemy.exc import IntegrityError
from repository import stock


router = APIRouter(
    tags=["Stocks"],
    prefix="/stock"
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowStock)
def create(request: schemas.Stock, db: Session = Depends(get_db)):
    try:
        new_stock = stock.create(request, db)
        return new_stock
    except IntegrityError:
        raise DuplicateUserException(request.symbol)


@router.get("/{symbol}", response_model=schemas.ShowStock)
def detail(symbol: str, db: Session = Depends(get_db)):
    stocks = stock.get(symbol, db)
    if not stocks:
        raise HTTPException(status_code=404, detail="Not Found")
    return stocks
