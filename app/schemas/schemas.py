from pydantic import BaseModel, EmailStr
from typing import List


class UserBase(BaseModel):
    email: EmailStr


class User(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: EmailStr
    password: str
    user_base: List[UserBase]


class SignIn(UserBase):
    password: str


class SignUp(UserBase):
    first_name: str
    last_name: str
    password: str


class UserUpdate(UserBase):
    first_name: str
    last_name: str


class UsersList(UserBase):
    email: str
    pagination: list
    users: List[User]


class Config:
    orm_mode = True
