import sqlalchemy.orm as _orm
import passlib.hash as _hash

import database as _db
import models as _models
import schemas as _schemas


def create_database():
    return _db.Base.metadata.create_all(bind=_db.engine)


def get_database():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_use_by_email(email: str, db: _orm.Session) -> _models.User:
    return db.query(_models.User).filter(_models.User.email == email).first()


async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    user_obj = _models.User(
        email=user.email, hashed_password=_hash.bcrypt.hash(user.hashed_password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj
