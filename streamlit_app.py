import streamlit as st
from google.cloud import firestore


# qui ci stiamo autenticando a Firestore con la chiave json scaricata e inserita nel progetto
db = firestore.Client.from_service_account_json("firestore-key.json")


posts_ref = db.collection("tweets")

# stampiamo tutto il db con un ciclo
for doc in posts_ref.stream():
    st.write("the text is: ", doc.to_dict())