import fastapi as _fastapi
from typing import List
import fastapi.security as _security
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services
from fastapi import Header
import jwt
import asyncio

_JWT_SECRET = "thisisnotverysafe"


app = _fastapi.FastAPI()

# Create a background task to consume messages from Kafka
asyncio.create_task(_services.consume())


@app.post("/api/v1/createPost", response_model=_schemas.Post)
async def create_post(post : _schemas.PostCreate, authorization: str = Header(), db: _orm.Session  = _fastapi.Depends(_services.get_db)):
    # Extract the JWT token from the Authorization header
    jwt_token = authorization.split("Bearer ")[1]
    
    try:
        # Decode the JWT token using the secret key
        decoded_token = jwt.decode(jwt_token, _JWT_SECRET, algorithms=["HS256"])
        
        # Extract the user ID from the decoded token
        user_id = decoded_token["id"]

    except jwt.exceptions.DecodeError:
        raise _fastapi.HTTPException(
            status_code=401,
            detail="Invalid JWT token"
        )
    
    return await _services.create_post(user_id=user_id, db=db, post=post)




@app.get("/api/v1/getUserPosts", response_model=List[_schemas.Post])
async def get_user_posts(authorization: str = Header(), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    # Extract the JWT token from the Authorization header
    jwt_token = authorization.split("Bearer ")[1]
    
    try:
        # Decode the JWT token using the secret key
        decoded_token = jwt.decode(jwt_token, _JWT_SECRET, algorithms=["HS256"])
        
        # Extract the user ID from the decoded token
        user_id = decoded_token["id"]
    except jwt.exceptions.DecodeError:
        raise _fastapi.HTTPException(
            status_code=401,
            detail="Invalid JWT token"
        )
    
    return await _services.get_user_posts(user_id=user_id, db=db)       



@app.get("/api/v1/getAllPosts")
async def get_all_posts(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_posts(db=db)


