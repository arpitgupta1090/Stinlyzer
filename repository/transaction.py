from DataBase import models


def detail(id, db):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id)
    return transaction


def list(db):
    transactions = db.query(models.Transaction).all()
    return transactions


def create(request, db):
    new_tnx = models.Transaction(stockId=request.stockId, amount=request.amount, value=request.value, user_id=request.user_id)
    db.add(new_tnx)
    db.commit()
    db.refresh(new_tnx)
    return new_tnx
