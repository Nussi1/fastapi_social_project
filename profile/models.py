from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .database import Base
from sqlalchemy.orm import relationship
import datetime


class Profile(Base):
  __tablename__ = 'profiles'

  id = Column(Integer, primary_key=True, index=True)
  user = Column(String)
  follows = Column(String)
  user_id = Column(Integer, ForeignKey('users.id'))

  owner = relationship('User', back_populates='profiles')


class Dweet(Base):
  __tablename__ = 'dweets'

  id = Column(Integer, primary_key=True, index=True)
  user = Column(String)
  body = Column(String)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  user_id = Column(Integer, ForeignKey('users.id'))

  creator = relationship('User', back_populates='dweets')


class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  email = Column(String)
  password = Column(String)

  profiles = relationship('Profile', back_populates='owner')
  dweets = relationship('Dweet', back_populates='creator')


