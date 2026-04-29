
from pydantic import BaseModel, ConfigDict, Field


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):

    # Can read data from attributes
    # Turns accessing data into Python attributes
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
