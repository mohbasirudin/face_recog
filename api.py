from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel
from deepface import DeepFace
import base64
import os
from io import BytesIO
import time

app = FastAPI()

@app.post("/faces_base64/")
async def faces_base64(
    image1: str = Form(...),
    image2: str = Form(...),
):
    try:
        if(len(image1) == 0 or len(image2) == 0):
            return {
                "message": "Verifikasi Gagal: Coba Lagi",
                "image1": "",
                "image2": "",
                "distance": "",
                "threshold": 0,
                "match": False,
                }
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        contents1 = base64.b64decode(image1)
        contents2 = base64.b64decode(image2)
        
        epoch_time = int(time.time())
        filename1 = str(epoch_time+1)+".jpg"
        filename2 = str(epoch_time+2)+".jpg"
        
        img_path1 = os.path.join(current_dir, filename1)
        with open(img_path1, "wb") as img_file:
            img_file.write(contents1)
        img_path2 = os.path.join(current_dir, filename2)
        with open(img_path2, "wb") as img_file:
            img_file.write(contents2)
        
        result = DeepFace.verify(
            img1_path = filename1,
            img2_path = filename2,
            model_name = "Facenet",
            distance_metric = "cosine",
        )
        distance = result['distance']
        threshold = result['threshold']
        
        os.remove(img_path1)
        os.remove(img_path2)
        
        message = "Verifikasi Gagal"
        if distance <= threshold:
            message = "Verifikasi Berhasil"
        elif distance > threshold and distance <= 0.5:
            message = "Verifikasi Gagal: Kurang Jelas"
        else:
            message = "Verifikasi Gagal"

        return {
            "message": message,
            "image1": filename1,
            "image2": filename2,
            "distance": distance,
            "threshold": threshold,
            "match": distance <= threshold,
            }
    except Exception as e:
        return {
            "message": "Verifikasi Gagal: Coba Lagi",
            "image1": "",
            "image2": "",
            "distance": "",
            "threshold": 0,
            "match": False,
            }
