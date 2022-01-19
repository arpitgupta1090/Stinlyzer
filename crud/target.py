from DataBase import models
from sqlalchemy.sql import func
from custom_exceptions import TargetLimitExceeded


def create_sector(request, db):
    new_sector = models.Sector(sector=request.sector, target=request.target, user_id=request.user_id)
    total = get_total_sector_target(db)
    if total + request.target > 100:
        raise TargetLimitExceeded()
    db.add(new_sector)
    db.commit()
    db.refresh(new_sector)
    return new_sector


def list_sector(db):
    sector = db.query(models.Sector).all()
    return sector


def details_sector(sector, db):
    sector = db.query(models.Sector).filter(models.Sector.sector == sector)
    return sector


def create_segment(request, db):
    new_segment = models.Segment(segment=request.segment, target=request.target, user_id=request.user_id)
    total = get_total_segment_target(db)
    if total + request.target > 100:
        raise TargetLimitExceeded()
    db.add(new_segment)
    db.commit()
    db.refresh(new_segment)
    return new_segment


def list_segment(db):
    segments = db.query(models.Segment).all()
    return segments


def details_segment(segment, db):
    segment = db.query(models.Segment).filter(models.Segment.segment == segment)
    return segment


def get_total_segment_target(db):
    totals = db.query(func.sum(models.Segment.target).label("total_target"))
    if not totals[0][0]:
        return 0
    return totals[0][0]


def get_total_sector_target(db):
    totals = db.query(func.sum(models.Sector.target).label("total_target"))
    if not totals[0][0]:
        return 0
    return totals[0][0]
