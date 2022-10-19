from pydantic import BaseModel, EmailStr


class User(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: EmailStr
    password: str


class UserBase(BaseModel):
    email: EmailStr


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


class Config:
    orm_mode = True
