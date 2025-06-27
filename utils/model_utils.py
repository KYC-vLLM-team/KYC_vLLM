import os
import gdown
import tensorflow as tf

MODEL_URL = "https://drive.google.com/uc?id=1eVDLSSNFmbMIt0fs3Ntpqq4bnTqkpXxg"
MODEL_PATH = "models/autoencoder_id.h5"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Téléchargement du modèle...")
        os.makedirs("models", exist_ok=True)
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

def load_model():
    download_model()
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    return model