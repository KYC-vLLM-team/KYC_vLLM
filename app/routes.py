from fastapi import APIRouter
from .models import ImageInput, MatchResult
from .logic import compare_faces_arcface

router = APIRouter()

@router.post("/verify_identity", response_model=MatchResult)
def verify_identity(data: ImageInput):
    return compare_faces_arcface(data.id_card_image, data.selfie_image)