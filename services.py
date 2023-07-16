
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

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=_database.engine)


from config import loop, KAFKA_BOOTSTRAP_SERVERS,  KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import json
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



async def consume():
    # Obtain the database session or transaction object from the dependency injection system
    
    db_session = _database.SessionLocal()
     # Create a Kafka consumer instance
    consumer = AIOKafkaConsumer(KAFKA_TOPIC,loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id= KAFKA_CONSUMER_GROUP)
    await consumer.start()
    try:
        # Consume messages from the Kafka topic
        async for userProduced in consumer:
            # Decode the message value from bytes to a JSON strin
            value_json = userProduced.value.decode('utf-8')
            
            # Convert the JSON string to a dictionary
            user_dict = json.loads(value_json)
            user = _models.userInformationPost(owner_id= user_dict['id'], first_name= user_dict['first_name'], last_name=user_dict['last_name'])
            
            db_session.add(user)
            db_session.commit()
            db_session.refresh(user)
            
    finally:
        db_session.close()
        await consumer.stop()


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