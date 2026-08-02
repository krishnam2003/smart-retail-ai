from fastapi import APIRouter, UploadFile, File
from PIL import Image

from app.services.face_service import recognize_face

router = APIRouter()

@router.post("/recognize-face")
async def recognize(file: UploadFile = File(...)):
    image = Image.open(file.file)

    return recognize_face(image)