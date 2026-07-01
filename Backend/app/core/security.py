from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from ..config import settings

pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")

def get_hashed_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#act as temporary vip pass
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode, settings.SECRETE_KEY, algorithm=settings.ALGORITHM)

    return encode_jwt

#token validation
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRETE_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")
        if user_id in None:
            return None
        return int(user_id)
    except JWTError:
        return None