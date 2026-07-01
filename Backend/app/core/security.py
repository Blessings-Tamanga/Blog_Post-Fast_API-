from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from ..schemas.user import UserResponseSchema
from dotenv import load_dotenv

load_dotenv()

pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")

def get_hashed_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()