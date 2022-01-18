from fastapi import APIRouter, Depends, status, HTTPException
from DataBase import schemas
from sqlalchemy.orm import Session
from DataBase.database import get_db
from custom_exceptions.exception import DuplicateUserException, SymbolNotFoundException
from sqlalchemy.exc import IntegrityError
from repository import stock
from yahoo.api import get_symbol, get_quote


router = APIRouter(
    tags=["Stocks"],
    prefix="/stock"
)


@router.get("/symbol/{company}")
def get(company: str):
    symbols = get_symbol(company)
    if not symbols:
        raise HTTPException(status_code=404, detail="Not Found")
    return symbols


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


@router.put("/{symbol}", response_model=schemas.ShowStock)
def update_current_price(symbol: str, db: Session = Depends(get_db)):
    stocks = stock.get(symbol, db)
    if not stocks.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    quote = get_quote(symbol)
    if not quote:
        raise SymbolNotFoundException(symbol)
    stocks.update(quote, synchronize_session=False)
    db.commit()
    return stocks.first()


