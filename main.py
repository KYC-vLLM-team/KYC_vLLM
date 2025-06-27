from fastapi import FastAPI, UploadFile, File
from utils.model_utils import load_model
from PIL import Image
import numpy as np
import io

app = FastAPI()
model = load_model()

# Seuil empirique trouvé dans le notebook
THRESHOLD = 0.0505

def preprocess_image(file: UploadFile) -> np.ndarray:
    image = Image.open(io.BytesIO(file.file.read())).convert("RGB")
    image = image.resize((128, 128))
    arr = np.array(image) / 255.0
    return np.expand_dims(arr, axis=0)  # (1, 128, 128, 3)

@app.post("/predict")
async def predict_id(file: UploadFile = File(...)):
    image = preprocess_image(file)
    recon = model.predict(image)
    mse = np.mean(np.square(image - recon))
   
    verdict = "Fake" if mse > THRESHOLD else "Real"

    return {
        "filename": file.filename,
        "anomaly_score": round(float(mse), 6),
        "verdict": verdict
    }