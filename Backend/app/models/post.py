from sqlalchemy import Column, String, Integer, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class PostModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("user_id", ondelete="CASCADE"), nullable=False)
    parent_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    view_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    #relationships
    author = relationship("UserModel", back_populates="posts")
    answers = relationship("PostModel", back_populates="question", remote_id=[id]) #self refernces