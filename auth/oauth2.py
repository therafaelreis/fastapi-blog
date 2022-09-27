from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from fastapi import Depends, HTTPException, status
from db.database import get_db
from sqlalchemy.orm.session import Session
from db import db_user


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = '9f147c43c3f894caa9a69928a01dadccd837facbc434c37e6910f1ab84ceda0b'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    credentials_exception  = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db_user.get_user_by_username(username=username, db=db)

    if user is None:
        raise credentials_exception
    
    return user