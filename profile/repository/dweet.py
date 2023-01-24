from typing import List
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status, HTTPException


def get_all(db: Session) -> List[models.Dweet]:
  dweets = db.query(models.Dweet).all()
  return dweets


def create(request: schemas.Dweet, db: Session):
  new_dweet = models.Dweet(user=request.user, body=request.body, user_id=1)
  db.add(new_dweet)
  db.commit()
  db.refresh(new_dweet)
  return new_dweet


def destroy(id: int, db: Session):
  dweet = db.query(models.Dweet).filter(models.Dweet.id == id)
  if not dweet:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Dweet with id {id} not found")
  dweet.delete(synchronize_session=False)
  db.commit()
  return 'done'


def update(id: int, request: schemas.Dweet, db: Session):
  dweet = db.query(models.Dweet).filter(models.Dweet.id == id)
  if not dweet.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Dweet with id {id} not found")
  else:
    db.query(models.Dweet).filter(models.Dweet.id == id).update(request.dict())
  db.commit()
  db.refresh(dweet)
  return 'updated'


def show(id: int, db: Session):
  single = db.query(models.Dweet).filter(models.Dweet.id == id).first()
  if not single:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    detail=f"dweet with id {id} not available")
  return single