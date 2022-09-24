from fastapi import APIRouter, Depends
from schemas import UserBase, UserResponse
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# create user
@router.post('/', response_model=UserResponse)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)
# read user

# update user

# delete user