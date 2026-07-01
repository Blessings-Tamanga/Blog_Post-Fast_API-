from sqlalchemy import create_engine
from sqlalchemy.ext import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


engine = create_engine(settings.DATABASE_URL, connect_arg={"check_same_threads": False} if "sqlite" in settings.DATABASE_URL else{})
SessionlLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()