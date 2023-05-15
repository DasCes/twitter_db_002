import streamlit as st
from google.cloud import firestore
import pandas as pd

# qui ci stiamo autenticando a Firestore con la chiave json scaricata e inserita nel progetto
db = firestore.Client.from_service_account_json("firestore-key.json")

# definiamo il riferimento al db
db_ref = db.collection("tweets")


df = pd.read_csv(f'data/data.csv', index_col=[0])
df = df.head(10)

for index, row in df.iterrows():
    doc_ref = db_ref.document("i" + str(index))
    doc = doc_ref.get()

    if not doc.exists:
        doc_ref.set({
            'id': index,
            'text': row['text'],
            'created_at': row['created_at'],
            'text_clean_IT': row['text_clean_IT']
        })



# stampiamo tutto il db con un ciclo
for doc in db_ref.stream():
    st.write("the id is: ", doc.id)
    st.write("contents of db: ", doc.to_dict())
