from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import shutil


router = APIRouter(
    prefix='/file',
    tags=['file']
)


@router.post('/uploadfile')
def get_uploadfile(upload_file: UploadFile = File(...)):
    path = f"files/{upload_file.filename}"
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return {
        'filename': path,
        'type': upload_file.content_type
    }


@router.get("/download/{name}", response_class=FileResponse)
def get_file(name: str):
    path = f'files/{name}'
    return path