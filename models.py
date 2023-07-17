import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import database as _database
from database import Base


class Post(_database.Base):
    # Model for the Post table
    __tablename__ = "posts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(_sql.Integer, index=True)
    post_text = _sql.Column(_sql.String, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)


class userInformationPost(_database.Base):
    # Model for the userInformationPost table
    __tablename__ = "userInformationPost"
    owner_id = _sql.Column(_sql.Integer,primary_key=True, index=True)
    first_name = _sql.Column(_sql.String,index=True)
    last_name = _sql.Column(_sql.String,index=True)