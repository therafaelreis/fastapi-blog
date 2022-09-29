from fastapi import FastAPI, Request, status
from fastapi.websockets import WebSocket
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.exceptions import HTTPException
from exceptions import StoryException
from routers import blog_get
from routers import blog_post
from routers import user
from routers import article
from routers import product
from routers import file
from auth import authentication
from db import models
from db.database import engine
from fastapi.staticfiles import StaticFiles
import time
from client import html

app = FastAPI()

app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(file.router)


@app.middleware("http")
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    return response


@app.get("/hello")
def index():
    return {"message": "Hello World"}


clients = []


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={'detail': exc.name}
    )


models.Base.metadata.create_all(engine)
app.mount('/files', StaticFiles(directory="files"), name='file')
