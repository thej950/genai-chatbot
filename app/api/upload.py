from fastapi import APIRouter, UploadFile, File
from app.services.s3 import upload_to_s3

router = APIRouter()


@router.post("/upload")
def upload(file: UploadFile = File(...)):

    return upload_to_s3(file)