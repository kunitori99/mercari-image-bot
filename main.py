import os
from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

@app.post("/generate")
async def generate_image(file: UploadFile = File(...)):
    api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

    image_bytes = await file.read()

    # Hugging Face にファイル形式で送信（これが重要）
    files = {"file": ("input.png", image_bytes, file.content_type)}

    response = requests.post(api_url, headers=headers, files=files)

    return {"result": response.json()}
