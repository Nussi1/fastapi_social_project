from typing import List
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status, HTTPException


def get_all(db: Session) -> List[models.Profile]:
	profiles = db.query(models.Profile).all()
	return profiles


def create(user: schemas.Profile, db: Session):
	new_profile = models.Profile(user=user.user, follows=user.follows, user_id=1)
	db.add(new_profile)
	db.commit()
	db.refresh(new_profile)
	return new_profile


def destroy(id: int, db: Session):
	profile = db.query(models.Profile).filter(models.Profile.id == id)
	if not profile:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
		                    detail=f"Profile with id {id} not found")
	profile.delete(synchronize_session=False)
	db.commit()
	return 'done'


def update(id: int, request: schemas.Profile, db: Session):
	profile = db.query(models.Profile).filter(models.Profile.id == id)
	if not profile.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
		                    detail=f"Profile with id {id} not found")
	else:
		db.query(models.Profile).filter(models.Profile.id == id).update(request.dict())
	db.commit()
	db.refresh(profile)
	return 'updated'


def show(id: int, db: Session):
	single = db.query(models.Profile).filter(models.Profile.id == id).first()
	if not single:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
		                    detail=f"profile with id {id} not available")
	return single
