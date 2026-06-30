from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime
from fastapi import HTTPException, status
from ..schemas.user import UserResponseSchema
from dotenv import load_dotenv

load_dotenv()

pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")