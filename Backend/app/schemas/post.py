from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from .user import UserResponseSchema

#Base Post layout
class PostBaseSchema(BaseModel):
    title: Optional[str] = None
    content: str

#question schema for questions
class QuestionCreateSchema(PostBaseSchema):
    title: str

#required for question being answered
class AnswerCreateSchema(PostBaseSchema):
    parent_id: int

class PostUpdateSchema(PostBaseSchema):
    title: Optional[str] = None
    content: Optional[str] = None

#output schema for sending data back to frontend
class PostResponseSchema(BaseModel):
    id: int
    title: Optional[str]
    content: str
    created_at: datetime
    updated_at: Optional[datetime]
    author: UserResponseSchema
    answer_count: Optional[int] = 0
    answers: Optional[List["PostResponseSchema"]] = []
    class Config:
        from_attributes = True