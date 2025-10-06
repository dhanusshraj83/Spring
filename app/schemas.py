from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: str
    exp: int

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True

class ReportCreate(BaseModel):
    url: Optional[str] = None
    source: str
    payload: str

class ReportOut(BaseModel):
    id: int
    url: Optional[str]
    source: str
    payload: str
    prediction: Optional[str]
    score: Optional[str]
    created_at: datetime
    owner_id: Optional[int]

    class Config:
        orm_mode = True
