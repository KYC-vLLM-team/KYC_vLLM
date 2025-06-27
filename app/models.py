from pydantic import BaseModel

class ImageInput(BaseModel):
    id_card_image: str   # image en base64
    selfie_image: str    # image en base64

class MatchResult(BaseModel):
    verified: bool
    distance: float
    model: str