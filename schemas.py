from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    username: str
    email: str
    # this converts database type automatically to the format that we want in this case UserResponse.
    class Config():
        orm_mode = True 