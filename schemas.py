
# It defines the Pydantic schemas used for data validation and serialization.
import datetime as _dt
import pydantic as _pydantic

class _PostBase(_pydantic.BaseModel):
    post_text: str

class PostCreate(_PostBase):
    pass

class Post(_PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True