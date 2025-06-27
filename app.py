import streamlit as st
import requests

st.set_page_config(page_title="Vérification d'authenticité ID", layout="centered")
st.title("Vérification d’une Carte d’Identité")
st.markdown("Téléversez une image de votre carte pour vérifier son authenticité.")

uploaded_file = st.file_uploader("Uploader votre carte d'identité", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Afficher l’image
    st.image(uploaded_file, caption="Carte téléversée", use_column_width=True)

    # Envoyer vers l’API FastAPI-02
    if st.button("Analyser la carte"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/predict", files=files)

        if response.status_code == 200:
            result = response.json()
            st.subheader("Résultat de l’analyse :")
            st.write(f"**Score d'anomalie** : {result['anomaly_score']:.4f}")
            st.success(f"Verdict : **{result['verdict']}**")
        else:
            st.error("Erreur lors de l’appel à l’API.")
