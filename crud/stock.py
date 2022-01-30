from DataBase import models


def create(request, db):
    new_stock = models.Stock(name=request.name, symbol=request.symbol, exchange=request.exchange, price=request.price,
                             sector=request.sector, segment=request.segment, tags=request.tags)
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock


def get(symbol, db):
    stock = db.query(models.Stock).filter(models.Stock.symbol == symbol)
    return stock


def list_stocks(db):
    stocks = db.query(models.Stock).all()
    return stocks
