from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "Sqlite:///./posts.db"

engine = create_engine(DATABASE_URL, connect_arg={"check_same_threads": False})
SessionlLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base(bind=engine, AutoCommit = False, AutoFlush = False)