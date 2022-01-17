from fastapi import FastAPI, Depends, status, HTTPException
import schemas
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
import encrypt
# import custom_exceptions

app = FastAPI()
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/transactions", status_code=status.HTTP_201_CREATED, tags=["Transactions"])
def create_transaction(request: schemas.Transaction, db: Session = Depends(get_db)):
    new_tnx = models.Transaction(stockId=request.stockId, amount=request.amount, value=request.value, user_id=request.user_id)
    db.add(new_tnx)
    db.commit()
    db.refresh(new_tnx)
    return new_tnx


@app.get("/transactions", tags=["Transactions"], response_model=List[schemas.TransactionShow])
def list_transaction(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()
    return transactions


@app.get("/transactions/{id}", tags=["Transactions"], response_model=schemas.TransactionShow)
def details_transaction(id, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id==id).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return transaction


@app.delete("/transactions/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Transactions"])
def destroy(id, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id==id)
    if not transaction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    transaction.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Deleted"}


@app.put("/transactions/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Transactions"])
def update(id, request: schemas.Transaction, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id)
    if not transaction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    transaction.update(request.__dict__, synchronize_session=False)
    db.commit()
    return transaction.first()


@app.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=["Users"])
def create(request: schemas.User, db: Session = Depends(get_db)):

    new_user = models.User(userName=request.userName, email=request.email, password=encrypt.hashed(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/user/{username}", response_model=schemas.ShowUser, tags=["Users"])
def detail(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.userName == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Not Found")
    return user


