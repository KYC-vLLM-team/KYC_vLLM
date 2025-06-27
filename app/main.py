from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="ID Verification API",
    description="Compare ID card and selfie using ArcFace (DeepFace)",
    version="1.0.0"
)

app.include_router(router)