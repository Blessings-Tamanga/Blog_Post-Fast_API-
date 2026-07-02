from sqlalchemy.orm import Session
from ..models.user import UserModel
from ..schemas.user import UserCreateSchema,UserUpdateSchema
from ..core.security import get_hashed_password,verify_password

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def get_username(db:Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()

def create_user(db:Session, user: UserCreateSchema):
    hashed = get_hashed_password(user.password)
    db_user = UserModel(
        email = user.email,
        surname = user.surname,
        hashed_password = hashed,
        bio = user.bio,
        profile_pic = user.profile_pic,
    )
    db.add(db_user)
    db.commit()
    db.refresh("db_user")

def update_user(db: Session, user_id: int, user_update: UserUpdateSchema):
    db_user = get_user(db, user_id)
    if not db_user: 
        return None
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user,key,value)
    db.commit()
    db.refresh(db_user)
    return db_user