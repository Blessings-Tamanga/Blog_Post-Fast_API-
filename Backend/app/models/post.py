from sqlalchemy import Column, String, Integer, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class PostModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(String, default=datetime.utcnow)
    updated_at = Column(String, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    author_id = Column(Integer, ForeignKey("user_id", ondelete="CASCADE"), nullable=False)
    author = relationship("UserModel", back_populates="posts")