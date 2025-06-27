import streamlit as st
import requests
import base64

st.title("Vérification d'identité avec DeepFace (ArcFace)")

st.write("Téléversez une **image de carte d'identité** et un **selfie** pour vérifier si c'est la même personne.")

# Uploads
id_image = st.file_uploader("Image de la carte d'identité", type=["png", "jpg", "jpeg"])
selfie_image = st.file_uploader("Image du selfie", type=["png", "jpg", "jpeg"])

# Fonction pour encoder en base64
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode("utf-8")

# Bouton vérifier
if st.button("Vérifier"):
    if id_image and selfie_image:
        encoded_id = encode_image(id_image)
        encoded_selfie = encode_image(selfie_image)

        # Appel API FastAPI
        response = requests.post("http://localhost:8000/verify_identity", json={
            "id_card_image": encoded_id,
            "selfie_image": encoded_selfie
        })

        if response.status_code == 200:
            result = response.json()
            st.success(f" Vérifié : {result['verified']}")
            st.write(f"Distance : {result['distance']:.4f}")
            st.write(f"Modèle : {result['model']}")
        else:
            st.error("Erreur lors de l'appel à l'API.")
    else:
        st.warning("Veuillez téléverser les deux images.")