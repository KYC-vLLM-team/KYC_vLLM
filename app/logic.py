import base64
import numpy as np
from PIL import Image
from io import BytesIO
from deepface import DeepFace

def decode_image(base64_str):
    decoded = base64.b64decode(base64_str)
    image = Image.open(BytesIO(decoded)).convert("RGB")
    return np.array(image)

def compare_faces_arcface(id_image_b64, selfie_image_b64):
    img1 = decode_image(id_image_b64)
    img2 = decode_image(selfie_image_b64)

    result = DeepFace.verify(
        img1_path=img1,
        img2_path=img2,
        model_name="ArcFace",
        enforce_detection=False
    )

    return {
        "verified": result.get("verified", False),
        "distance": result.get("distance", 1.0),
        "model": result.get("model", "unknown")
    }