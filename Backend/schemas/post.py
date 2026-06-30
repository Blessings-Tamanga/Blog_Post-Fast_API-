from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ..schemas.user import UserResponse

#Base Post layout
class PostBaseSchema(BaseModel):
    title: str
    content: str

#Input schema for creating a new post(Vanilla)
class PostCreateSchema(PostBaseSchema):
    pass

class PostUpdateSchema(PostBaseSchema):
    title: Optional[str]
    content: Optional[str]

#output schema for sending data back to frontend
class PostResponseSchema(PostBaseSchema):
    id: int
    date: datetime
    user: UserResponse

    class Config:
        from_attributes = True