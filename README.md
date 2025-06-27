# KYC_vLLM


**KYC_vLLM** (Know Your Customer via Vision and Large Language Models) is a full-stack project designed to perform secure, AI-powered identity verification. It combines facial recognition, document authenticity checks, and OCR-based data matching to help detect fraud and ensure regulatory compliance.

This project was developed in collaboration with **Mr Zakariyya (Effyis)** and contributed by:


- **Naoual El Omri**
- **Aya Rabeh**



## Project Overview

KYC_vLLM offers a modular and scalable pipeline for user verification, including:

### 1. Face Match Verification
- **Goal:** Confirm that the user’s selfie matches the ID card photo.
- **Tech:** `DeepFace` (ArcFace model), OpenCV
- **Frontend:** Streamlit interface (`ui-01`)
- **Backend API:** FastAPI endpoint (`fastapi-01`)

### 2. Fake ID Detection
- **Goal:** Detect counterfeit ID cards using anomaly detection.
- **Tech:** Convolutional Autoencoder trained on real IDs
- **Frontend:** Streamlit (`ui-02`)
- **Backend API:** FastAPI (`fastapi-02`)

### 3. Data Consistency Verification
- **Goal:** Ensure that the information entered by the user (name, CIN, birth date...) matches what is extracted from the ID using OCR.
- **Tech:** EasyOCR + Regex parsing
- **Frontend:** Streamlit (`ui-03`)
- **Backend API:** FastAPI (`fastapi-03`)

## Collaboration

This project includes licensed code under the MIT License by **Mr Zakariyya (Effyis)**.

All development, testing, and documentation have been co-authored by:

- **Zakariyya (Effyis)** – Lead contributor (original license owner)
- **Naoual El Omri**
- **Aya Rabeh**

---

## License

This project contains parts that are under the MIT License, originally written by Zakariyya:
MIT License

Copyright (c) 2025 zakaria-effyis

#  UI-01 — Streamlit Frontend for Identity Verification

This branch (`UI-01`) contains the Streamlit web interface that interacts with the FastAPI backend defined in `fastapi-01`.

The goal is to provide a **user-friendly web interface** where users can upload:
- An image of an identity card
- A selfie image

Then, it will call the FastAPI `/verify_identity` endpoint and display:
- Whether the person in the selfie matches the ID card
-  Confidence score

---

##  How to Run the UI

### 1. Make sure the FastAPI server is running

Go to the `fastapi-01` directory and start the server:


cd ../fastapi-01
uvicorn app.main:app --reload
You should see:
Uvicorn running on http://127.0.0.1:8000
This exposes the /verify_identity route used by the UI.

### 2. Run the Streamlit app
From the UI-01 directory:

cd ../UI-01
streamlit run app.py
### 3. Interact via the Web UI
Once the Streamlit app is running, your browser should open to:

http://localhost:8501
There, you can:

Upload an ID card image  


Upload a selfie image  


Click  to launch verification  


View the result (match or not + similarity score)
