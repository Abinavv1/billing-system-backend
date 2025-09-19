from typing import Optional

from pydantic import EmailStr

from .base import Schema

class UserRegister(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    is_admin: bool = False
    
class UserLogin(Schema):
    email: EmailStr
    password: str
    
class UserResponse(Schema):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    is_admin: bool

class UserUpdate(Schema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_admin: Optional[bool] = None
