from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import cv2
import easyocr
import io
import re

app = FastAPI()

# Autoriser CORS si test frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

reader = easyocr.Reader(["fr"], gpu=False)

def extract_fields(text):
    fields = {}
    lines = [line.strip() for line in text.split('\n') if line.strip()]

    # CIN
    cin_match = re.search(r"\b[A-Z]{1,2}\d{4,6}\b", text)
    if cin_match:
        fields["cin"] = cin_match.group()

    # Dates
    dates = re.findall(r"\b\d{2}[./-]\d{2}[./-]\d{4}\b", text)
    if len(dates) >= 1:
        fields["date_of_birth"] = dates[0]
    if len(dates) >= 2:
        fields["expiry_date"] = dates[1]

    # Full name (before NÉ)
    for line in lines:
        if re.search(r"\bN[Ééèe]\b", line, re.IGNORECASE):
            before_ne = re.split(r"\bN[Ééèe]\b", line, flags=re.IGNORECASE)[0]
            words = re.findall(r"\b[A-Z]{2,}\b", before_ne)
            if len(words) >= 2:
                fields["full_name"] = " ".join(words[-2:])
            break

    return fields

@app.post("/verify-card-info")
async def verify_card_info(
    file: UploadFile = File(...),
    cin: str = Form(...),
    full_name: str = Form(...),
    date_of_birth: str = Form(...),
    expiry_date: str = Form(...),
):
    content = await file.read()
    np_arr = np.frombuffer(content, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = reader.readtext(img, detail=0, paragraph=True)
    raw_text = " ".join(results)
    fields = extract_fields(raw_text)

    user_input = {
        "cin": cin.strip().upper(),
        "full_name": full_name.strip().upper(),
        "date_of_birth": date_of_birth.strip(),
        "expiry_date": expiry_date.strip()
    }

    comparisons = {}
    for field in user_input:
        expected = user_input[field]
        found = fields.get(field, "").strip().upper()
        comparisons[field] = {
            "status": "MATCH" if expected == found else "MISMATCH",
            "expected": expected,
            "found": found
        }

    return JSONResponse({
        "comparisons": comparisons,
        "raw_text": raw_text,
        "fields": fields
    })