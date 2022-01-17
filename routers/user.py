from fastapi import APIRouter, Depends, status, HTTPException
from DataBase import schemas, models
from sqlalchemy.orm import Session
from DataBase.database import get_db
from encryption import encrypt
from custom_exceptions.exception import DuplicateUserException
from sqlalchemy.exc import IntegrityError


router = APIRouter()


@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=["Users"])
def create(request: schemas.User, db: Session = Depends(get_db)):
    try:
        new_user = models.User(userName=request.userName, email=request.email, password=encrypt.hashed(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        raise DuplicateUserException(request.userName)


@router.get("/user/{username}", response_model=schemas.ShowUser, tags=["Users"])
def detail(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.userName == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Not Found")
    return user