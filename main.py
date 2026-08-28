import os
from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

@app.post("/generate")
async def generate_image(file: UploadFile = File(...)):
    api_url = "https://api-inference.huggingface.co/models/your-model-name"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}
    image_bytes = await file.read()
    response = requests.post(api_url, headers=headers, data=image_bytes)
    return {"result": response.json()}

