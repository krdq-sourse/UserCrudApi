from datetime import date
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    password: str
    register_date: date


class UserSchemaCreate(BaseModel):
    username: str
    email: str
    password: str


class UserSchemaUpdate(BaseModel):
    username: str
    email: str
    password: str


class UserSchemaDelete(BaseModel):
    id: int
