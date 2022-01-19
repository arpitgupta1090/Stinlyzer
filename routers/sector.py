from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from DataBase import schemas
from sqlalchemy.orm import Session
from DataBase.database import get_db
from custom_exceptions import DuplicateSectorException, TargetLimitExceeded
from sqlalchemy.exc import IntegrityError
from crud import target


router = APIRouter(
    tags=["Sectors"],
    prefix="/sectors"
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowSector)
def create_sector(request: schemas.Sector, db: Session = Depends(get_db)):
    try:
        new_user = target.create_sector(request, db)
        return new_user
    except IntegrityError:
        raise DuplicateSectorException(request.sector)


@router.get("/", response_model=List[schemas.ShowSector])
def list_sectors(db: Session = Depends(get_db)):
    sectors = target.list_sector(db)
    return sectors


@router.put("/{sector}", status_code=status.HTTP_202_ACCEPTED)
def update_sector(sector, request: schemas.Sector, db: Session = Depends(get_db)):
    sectors = target.details_sector(sector, db)
    if not sectors.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    total = target.get_total_sector_target(db)
    if total + request.target - sectors.first().target > 100:
        raise TargetLimitExceeded()
    sectors.update(request.__dict__, synchronize_session=False)
    db.commit()
    return sectors.first()


@router.delete("/{sector}", status_code=status.HTTP_202_ACCEPTED)
def delete_sector(sector, db: Session = Depends(get_db)):
    sectors = target.details_sector(sector, db)
    if not sectors.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    sectors.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Deleted"}


