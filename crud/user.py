from DataBase import models
from encryption import hashed


def create(request, db):
    new_user = models.User(userName=request.userName, email=request.email, password=hashed(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(username, db):
    user = db.query(models.User).filter(models.User.userName == username).first()
    return user
