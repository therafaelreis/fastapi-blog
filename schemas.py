from typing import List
from pydantic import BaseModel

# Article inside UserResponse
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config():
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    # this converts database type automatically to the format that we want in this case UserResponse.
    class Config():
        orm_mode = True


# User inside article Display
class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode=True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleResponse(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config():
        orm_mode = True