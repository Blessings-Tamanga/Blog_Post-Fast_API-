from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from ..database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key =True, index = True)
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    passowrd = Column(String, nullable=False)
    bio = Column(String, default="")
    profile_pic = Column(String, default="")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    posts = relationship("PostModel", back_populates="author", cascade="all, delete-orphan")