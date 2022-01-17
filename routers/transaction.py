from fastapi import APIRouter, Depends, status, HTTPException
from DataBase import schemas, models
from sqlalchemy.orm import Session
from DataBase.database import get_db
from typing import List


router = APIRouter(
    tags=["Transactions"],
    prefix="/transactions"
)


@router.get("/{id}", response_model=schemas.TransactionShow)
def details_transaction(id, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id==id).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return transaction


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_transaction(request: schemas.Transaction, db: Session = Depends(get_db)):
    new_tnx = models.Transaction(stockId=request.stockId, amount=request.amount, value=request.value, user_id=request.user_id)
    db.add(new_tnx)
    db.commit()
    db.refresh(new_tnx)
    return new_tnx


@router.get("/", response_model=List[schemas.TransactionShow])
def list_transaction(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()
    return transactions


@router.get("/{id}", response_model=schemas.TransactionShow)
def details_transaction(id, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id==id).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return transaction


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id==id)
    if not transaction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    transaction.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Deleted"}


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Transaction, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id)
    if not transaction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    transaction.update(request.__dict__, synchronize_session=False)
    db.commit()
    return transaction.first()