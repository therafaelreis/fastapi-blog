from typing import List
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
@router.get('/', response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# read user by id
@router.get('/{id}', response_model=UserResponse)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db_user.find_user_by_id(id, db)

# update user
@router.put('/{id}')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(id, request, db)


# delete user
@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(id, db)