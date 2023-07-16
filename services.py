
#SERVICES STILL NOT ORGINIZED

import database as _database
import fastapi as _fastapi
import models as _models
import schemas as _schemas
import fastapi.security as _security
from typing import TYPE_CHECKING, List
import sqlalchemy.orm as _orm
# It is used for validating email addresses.
import email_validator as _email_val
#  It is used for encoding and decoding JSON Web Tokens 
import jwt 
# It provides password hashing and verification utilities.
import passlib.hash as _hash

_JWT_SECRET = "thisisnotverysafe"




if TYPE_CHECKING:
    from sqlalchemy.orm import Session


# >>>import services
# >>> services._add_tables()
# it is a helper function responsible for creating the database tables based on the SQLAlchemy models defined in the database module.
def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


# It is a FastAPI dependency that provides a database session (db) to other routes and functions.
def get_db():
    db = _database.SessionLocal()

    try:
        yield db
    finally:
        db.close()



 


async def create_post(user_id : str, db: _orm.Session, post: _schemas.PostCreate):
    post = _models.Post(**post.dict(), owner_id = user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return _schemas.Post.from_orm(post)


async def get_user_posts(user_id: str, db: _orm.Session):
    posts = db.query(_models.Post).filter_by(owner_id=user_id)

    return list(map(_schemas.Post.from_orm, posts))


async def get_all_posts(db: _orm.Session):
    posts = db.query(_models.Post)
    return list(map(_schemas.Post.from_orm, posts))