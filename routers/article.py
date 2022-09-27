from typing import List
from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleCreateResponse, ArticleResponse, User, UserBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/article',
    tags=['article']
)

@router.post('/', response_model=ArticleResponse)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(request, db)


@router.get('/{id}', response_model=ArticleCreateResponse)
def get_article(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return {
        'data': db_article.get_article(id, db),
        'currentUser': current_user
    }