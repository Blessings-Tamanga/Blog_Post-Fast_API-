from sqlalchemy import Column,String,Integer,DateTime
from database import Base
from datetime import datetime


class PostsModel(Base):
    __tablename__ = "Posts"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, unique=False, nullable=False, index=True )
    Content =Column(String, Unique=False, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)


    def config(db):
        try:
            yield db
        finally:
            db.close()