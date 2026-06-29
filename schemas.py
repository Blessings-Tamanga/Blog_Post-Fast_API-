from pydantic import BaseModel
from typing import Optional


class PostSchema(BaseModel):
    title : str
    content : str
    date : str


class PostsUpdateSchema(BaseModel):
    title : Optional[str]
    content : Optional[str]
    date : Optional[str]