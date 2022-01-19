from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from DataBase import schemas
from sqlalchemy.orm import Session
from DataBase.database import get_db
from custom_exceptions import DuplicateSegmentException, DuplicateSectorException, TargetLimitExceeded
from sqlalchemy.exc import IntegrityError
from crud import target

router = APIRouter(
    tags=["Segments"],
    prefix="/segments"
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowSegment)
def create_segment(request: schemas.Segment, db: Session = Depends(get_db)):
    try:
        new_segment = target.create_segment(request, db)
        return new_segment
    except IntegrityError:
        raise DuplicateSegmentException(request.segment)


@router.get("/", response_model=List[schemas.ShowSegment])
def list_segments(db: Session = Depends(get_db)):
    segments = target.list_segment(db)
    return segments


@router.put("/{segment}", status_code=status.HTTP_202_ACCEPTED)
def update_segment(segment, request: schemas.Segment, db: Session = Depends(get_db)):
    segments = target.details_segment(segment, db)
    if not segments.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    total = target.get_total_segment_target(db)
    if total + request.target - segments.first().target > 100:
        raise TargetLimitExceeded()
    segments.update(request.__dict__, synchronize_session=False)
    db.commit()
    return segments.first()


@router.delete("/{segment}", status_code=status.HTTP_202_ACCEPTED)
def delete_segment(segment, db: Session = Depends(get_db)):
    segments = target.details_segment(segment, db)
    if not segments.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    segments.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Deleted"}
