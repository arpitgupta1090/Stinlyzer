from fastapi import APIRouter, Depends, status, HTTPException
from DataBase import schemas
from sqlalchemy.orm import Session
from DataBase.database import get_db
from custom_exceptions.exception import DuplicateUserException
from sqlalchemy.exc import IntegrityError
from repository import user


router = APIRouter(
    tags=["Users"],
    prefix="/user"
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    try:
        new_user = user.create(request, db)
        return new_user
    except IntegrityError:
        raise DuplicateUserException(request.userName)


@router.get("/{username}", response_model=schemas.ShowUser)
def detail(username: str, db: Session = Depends(get_db)):
    users = user.get(username, db)
    if not users:
        raise HTTPException(status_code=404, detail="Not Found")
    return users
