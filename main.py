from fastapi import FastAPI
from routers import blog_get
from routers import blog_post
from routers import user
from routers import article
from db import models
from db.database import engine

app = FastAPI()

app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)

@app.get("/")
def index():
    return {"message": "Hello World"}


models.Base.metadata.create_all(engine)
