from fastapi import APIRouter, Depends, status, HTTPException
from DataBase import schemas
from sqlalchemy.orm import Session
from DataBase.database import get_db
from repository import transaction


router = APIRouter(
    tags=["Transactions"],
    prefix="/transactions"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_transaction(request: schemas.Transaction, db: Session = Depends(get_db)):
    new_tnx = transaction.create(request, db)
    return new_tnx


@router.get("/")
def list_transaction(db: Session = Depends(get_db)):
    transactions = transaction.list(db)
    return transactions


@router.get("/{id}", response_model=schemas.TransactionShow)
def details_transaction(id, db: Session = Depends(get_db)):
    transactions = transaction.detail(id, db)
    if not transactions.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return transactions.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    transactions = transaction.detail(id, db)
    if not transactions.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    transactions.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Deleted"}


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Transaction, db: Session = Depends(get_db)):
    transactions = transaction.detail(id, db)
    if not transactions.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    transactions.update(request.__dict__, synchronize_session=False)
    db.commit()
    return transactions.first()
