from typing import Optional, List
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    number_of_comments: int


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, comment_title: int = Query(None,
                                                                     title='Title of the comment',
                                                                     description='Some description for comment title',
                                                                     alias='commentTitle',
                                                                     deprecated=True),
                                                                     content: str = Body(...),
                                                                     v: Optional[List[str]] = Query(None),
                                                                     comment_id: int = Path(None, gt=5, le=10)):
    return {
        'id': id,
        'data': blog,
        'comment_title': comment_title,
        'content': content,
        'comment_id': comment_id,
        'version': v
    }
