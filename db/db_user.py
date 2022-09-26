from sqlalchemy.orm.session import Session
from db.hash import Hash
from schemas import UserBase
from db.models import DbUser
from fastapi import HTTPException, status


def create_user(request: UserBase, db: Session):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    # we need to refresh so once the database creates the new user, we need the id that was auto generated by the db.
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def find_user_by_id(id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    return user


def update_user(id: int, request: UserBase, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'


def delete_user(id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    db.delete(user)
    db.commit()
    return 'ok'
