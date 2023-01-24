from datetime import datetime
from fastapi import Body
from pydantic import BaseModel
from typing import List
from typing import Union


class Profile(BaseModel):
  user: str
  follows: str


class User(BaseModel):
  name: str
  email: str
  password: str


class ShowUser(BaseModel):
  name: str
  email: str
  profiles: List
  dweets: List

  class Config():
    orm_mode = True


class Dweet(BaseModel):
  user: str
  body: str
  created_at: datetime | None = Body(default=None)


class ShowDweet(BaseModel):
  user: str
  body: str
  created_at: datetime | None = Body(default=None)
  creator: ShowUser


class ShowProfile(BaseModel):
  id: int
  user: str
  follows: str
  user_id: int

  class Config:
    orm_mode = True


class Login(BaseModel):
  username: str
  password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
