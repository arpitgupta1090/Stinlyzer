from DataBase import models


def detail(id, db):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id)
    return transaction


def list(db):
    transactions = db.query(models.Transaction).all()
    return transactions


def create(request, db):
    new_tnx = models.Transaction(stockId=request.stockId, price=request.price, quantity=request.quantity,
                                 purchased_date=request.purchased_date, user_id=request.user_id)
    db.add(new_tnx)
    db.commit()
    db.refresh(new_tnx)
    return new_tnx
