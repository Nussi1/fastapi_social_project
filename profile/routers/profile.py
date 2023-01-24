from typing import List, Any
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database
from ..schemas import ShowProfile
from ..auth import oauth2
from sqlalchemy.orm import Session
from ..repository import profile


router = APIRouter(
  prefix="/profile",
  tags=['Profiles']
)
get_db = database.get_db


@router.get('/', response_model=List[ShowProfile])
def all(db: Session = Depends(get_db)):
    profiles = profile.get_all(db)
    return profiles


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(p: schemas.Profile, db: Session = Depends(get_db)):
    return profile.create(p, db)


@router.get('/{id}', status_code=200, response_model=ShowProfile)
def show(id: int, db: Session = Depends(get_db)):
    return profile.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Profile, db: Session = Depends(get_db)):
    return profile.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return profile.destroy(id, db)
