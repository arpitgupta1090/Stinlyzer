from DataBase import models


def create_sector(request, db):
    new_sector = models.Sector(sector=request.sector, target=request.target)
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
    new_segment = models.Segment(segment=request.segment, target=request.target)
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
