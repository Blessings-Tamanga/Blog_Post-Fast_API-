from typing import Generator
from ..database.database import SessionlLocal 

"""
create a new database session for a single network request
and auto close it once the request is done
"""
def get_db() -> Generator:
    db = SessionlLocal
    try:
        yield db
    finally:
        db.close()