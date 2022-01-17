from fastapi import Depends
from DataBase import schemas, models
from sqlalchemy.orm import Session
from DataBase.database import get_db
from encryption import encrypt


def create(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(userName=request.userName, email=request.email, password=encrypt.hashed(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(username, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.userName == username).first()
    return user
