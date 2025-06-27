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

# ID Card Authenticity Detection (Notebook-02)

This notebook uses a **convolutional autoencoder** to verify the **authenticity of an identity card image** by checking for anomalies. It is part of the **KYC_vLLM** project for secure and automated identity verification.

##  Core Features

- **Autoencoder Model** trained to reconstruct only real ID cards
- **Anomaly Score** is computed as reconstruction error
- Predicts whether an ID card is **real** or **fake**


## Output

- Displays original and reconstructed images side by side.
- Shows anomaly score (MSE between input and reconstruction).
- Highlights mismatches (likely fakes) with higher scores.
  
## Download the model from Google Drive

The `autoencodeur_id.h5` model is hosted on Google Drive to avoid file size limits on GitHub.

**Model Drive Link**:  
[https://drive.google.com/file/d/1eVDLSSNFmbMIt0fs3Ntpqq4bnTqkpXxg/view?usp=sharing](https://drive.google.com/file/d/1eVDLSSNFmbMIt0fs3Ntpqq4bnTqkpXxg/view?usp=sharing)

In the notebook, the following code downloads it automatically:

```python
import gdown
file_id = "1eVDLSSNFmbMIt0fs3Ntpqq4bnTqkpXxg"
gdown.download(f"https://drive.google.com/uc?id={file_id}", "autoencodeur_id.h5", quiet=False)

ae = tf.keras.models.load_model("autoencodeur_id.h5", compile=False)
