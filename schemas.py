
# It defines the Pydantic schemas used for data validation and serialization.
import datetime as _dt
import pydantic as _pydantic

# Base schema for a post
class _PostBase(_pydantic.BaseModel):
    post_text: str

# Schema for creating a new post
class PostCreate(_PostBase):
    pass

# Schema for a post with additional fields
class Post(_PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime

    class Config:
        # Enable ORM mode to allow working with SQLAlchemy models
        orm_mode = True

# Schema for the user producer
class UserProducer(_pydantic.BaseModel):
    id : int
    first_name: str
    last_name :str

