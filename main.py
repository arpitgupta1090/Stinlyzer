from fastapi import FastAPI, Depends, status, HTTPException
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return "home"


@app.post("/transactions", status_code=status.HTTP_201_CREATED)
def create_transaction(request: schemas.Transaction, db: Session = Depends(get_db)):
    new_tnx = models.Transaction(stockId=request.stockId, amount=request.amount, value=request.value)
    db.add(new_tnx)
    db.commit()
    db.refresh(new_tnx)
    return new_tnx


@app.get("/transactions")
def list_transaction(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()
    return transactions


@app.get("/transactions/{id}")
def details_transaction(id, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id==id).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return transaction


@app.delete("/transactions/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id==id)
    if not transaction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    transaction.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Deleted"}


@app.put("/transactions/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Transaction, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id)
    if not transaction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    transaction.update(request.__dict__, synchronize_session=False)
    db.commit()
    return transaction.first()


@app.post("/user", status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(userName=request.userName, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
