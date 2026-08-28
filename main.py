import os
from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

@app.post("/generate")
async def generate_image(file: UploadFile = File(...)):
    # ★画像→画像ができるモデル（SD3.5は不可）
    api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

    # ユーザーがアップした画像を読み込む
    image_bytes = await file.read()

    # Hugging Face に画像を送信（img2img対応モデルならOK）
    response = requests.post(api_url, headers=headers, data=image_bytes)

    return {"result": response.json()}
