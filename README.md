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

# Notebook - Identity Card Information Matching

This notebook implements a method to verify if the **user-entered identity information** matches the information **automatically extracted from an uploaded Moroccan ID card image**.

## Functionality

The notebook:
- Uses **EasyOCR** to extract text from the uploaded ID card image.
- Applies **regex rules** to detect and extract:
  - **CIN** (National ID number)
  - **Full name**
  - **Date of birth**
  - **Expiry date**
- Compares these extracted fields with the **user-entered values**.
- Outputs a **comparison table** indicating:
  - `MATCH`  if the field matches.
  - `MISMATCH` if there's a discrepancy.



## Notes

- Accuracy depends on image quality and OCR precision.
