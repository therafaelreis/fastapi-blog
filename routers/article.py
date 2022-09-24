from typing import List
from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleResponse
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article

router = APIRouter(
    prefix='/article',
    tags=['article']
)

@router.post('/', response_model=ArticleResponse)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(request, db)


@router.get('/{id}', response_model=ArticleResponse)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(id, db)