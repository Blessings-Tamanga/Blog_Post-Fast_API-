from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

#Base configuration shared by all user representation
class UserBaseSchema(BaseModel):
    username: str
    email: str

#schema for receiving data during registration
class UserCreateSchema(UserBaseSchema):
    password: str

#schema for sending data back to frontend
class UserResponseSchema(UserBaseSchema):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True