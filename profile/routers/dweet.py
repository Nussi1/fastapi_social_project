from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database
from ..schemas import ShowDweet
from ..auth import oauth2
from sqlalchemy.orm import Session
from ..repository import dweet


router = APIRouter(
  prefix="/dweet",
  tags=['Dweets']
)
get_db = database.get_db


@router.get('/', response_model=List[ShowDweet])
def all(db: Session = Depends(get_db)):
    dweets = dweet.get_all(db)
    return dweets


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Dweet, db: Session = Depends(get_db)):
    return dweet.create(request, db)


@router.get('/{id}', status_code=200, response_model=ShowDweet)
def show(id:int, db: Session = Depends(get_db)):
    return dweet.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Dweet, db: Session = Depends(get_db)):
    return dweet.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return dweet.destroy(id, db)