from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from DataBase import schemas
from sqlalchemy.orm import Session
from DataBase.database import get_db
from custom_exceptions import DuplicateUserException
from sqlalchemy.exc import IntegrityError
from crud import target


router = APIRouter(
    tags=["Targets"],
    prefix="/target"
)


@router.post("/sectors", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowSector)
def create_sector(request: schemas.Sector, db: Session = Depends(get_db)):
    try:
        new_user = target.create_sector(request, db)
        return new_user
    except IntegrityError:
        raise DuplicateUserException(request.sector)


@router.get("/sectors", response_model=List[schemas.ShowSector])
def list_sectors(db: Session = Depends(get_db)):
    sectors = target.list_sector(db)
    return sectors


@router.put("/sectors/{sector}", status_code=status.HTTP_202_ACCEPTED)
def update_sector(sector, request: schemas.Sector, db: Session = Depends(get_db)):
    sectors = target.details_sector(sector, db)
    if not sectors.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    total = target.get_total_sector_target(db)
    if total + request.target - sectors.first().target > 100:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Total target cannot be more than 100")
    sectors.update(request.__dict__, synchronize_session=False)
    db.commit()
    return sectors.first()


@router.delete("/sectors/{sector}", status_code=status.HTTP_202_ACCEPTED)
def delete_sector(sector, db: Session = Depends(get_db)):
    sectors = target.details_sector(sector, db)
    if not sectors.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    sectors.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Deleted"}


@router.post("/segments", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowSegment)
def create_segment(request: schemas.Segment, db: Session = Depends(get_db)):
    try:
        new_segment = target.create_segment(request, db)
        return new_segment
    except IntegrityError:
        raise DuplicateUserException(request.segment)


@router.get("/segments", response_model=List[schemas.ShowSegment])
def list_segments(db: Session = Depends(get_db)):
    segments = target.list_segment(db)
    print(target.get_total_segment_target(db))
    print(target.get_total_sector_target(db))
    return segments


@router.put("/segments/{segment}", status_code=status.HTTP_202_ACCEPTED)
def update_segment(segment, request: schemas.Segment, db: Session = Depends(get_db)):
    segments = target.details_segment(segment, db)
    if not segments.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    total = target.get_total_segment_target(db)
    if total + request.target - segments.first().target > 100:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Total target cannot be more than 100")
    segments.update(request.__dict__, synchronize_session=False)
    db.commit()
    return segments.first()


@router.delete("/segments/{segment}", status_code=status.HTTP_202_ACCEPTED)
def delete_segment(segment, db: Session = Depends(get_db)):
    segments = target.details_segment(segment, db)
    if not segments.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    segments.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Deleted"}
