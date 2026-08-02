from fastapi import APIRouter, UploadFile, File
from PIL import Image

from app.services.product_service import predict_product

router = APIRouter()

@router.post("/classify-product")
async def classify_product(file: UploadFile = File(...)):
    image = Image.open(file.file)

    result = predict_product(image)

    return result