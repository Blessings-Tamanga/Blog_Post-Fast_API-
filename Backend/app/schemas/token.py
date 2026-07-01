from pydantic import BaseModel
from typing import Optional

class TokenSchema(BaseModel):
    token: str
    token_type: str

class TokenDataSchema(BaseModel):
    user_id: Optional[int] = None