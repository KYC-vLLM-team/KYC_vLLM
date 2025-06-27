import streamlit as st
import requests

st.set_page_config(page_title="Vérification des informations de la carte", layout="centered")

st.title("Vérification des informations de la carte d'identité")
st.markdown("Veuillez saisir vos informations et télécharger une image de votre carte d'identité.")

with st.form("formulaire_id"):
    full_name = st.text_input("Nom complet (ex: ESSOUSSI MUSTAPHA)")
    cin = st.text_input("Numéro de CIN (ex: EA441462)")
    date_of_birth = st.text_input("Date de naissance (ex: 26/09/1972)")
    expiry_date = st.text_input("Date d'expiration (ex: 27/09/2027)")
    image_file = st.file_uploader("Image de la carte d'identité", type=["jpg", "jpeg", "png"])
    submitted = st.form_submit_button("Vérifier")

if submitted and image_file:
    with st.spinner("Analyse en cours..."):
        files = {"file": image_file.getvalue()}
        data = {
            "cin": cin,
            "full_name": full_name,
            "date_of_birth": date_of_birth,
            "expiry_date": expiry_date,
        }
        try:
            res = requests.post("http://localhost:8000/verify-card-info", data=data, files={"file": image_file})
            if res.status_code == 200:
                result = res.json()
                st.success("Résultat de la comparaison :")

                for field, details in result["comparisons"].items():
                    color = "" if details["status"] == "MATCH" else "❌"
                    st.markdown(f"**{field}** : {color} {details['status']}")
                    st.markdown(f"- Attendu : `{details['expected']}`")
                    st.markdown(f"- Trouvé : `{details['found']}`")

                with st.expander("📜 Texte brut extrait de la carte"):
                    st.code(result["raw_text"])

            else:
                st.error("Erreur lors de la requête à l’API.")
        except Exception as e:
            st.error(f"Erreur : {e}")
elif submitted:
    st.warning("Veuillez fournir une image de la carte.")