import streamlit as st
from google.cloud import firestore
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
import time

global num
num = 0

# qui ci stiamo autenticando a Firestore con la chiave json scaricata e inserita nel progetto
db = firestore.Client.from_service_account_json("firestore-key.json")

# definiamo il riferimento al db
db_ref = db.collection("tws")


df = pd.read_csv(f'data/data.csv', index_col=[0])
df = df.head(12)



def aggiungiTweetOgniNSecondi():
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
    num += 1




# Create a scheduler
scheduler = BackgroundScheduler()


# Schedule the job to run every WAIT_SECONDS
scheduler.add_job(aggiungiTweetOgniNSecondi, 'interval', seconds=15)

# Start the scheduler
scheduler.start()




# stampiamo tutto il db con un ciclo
print_db_ref = db.collection("tws").order_by("id")

for doc in print_db_ref.stream():
    st.write("aggiornamento numero: ", num)
    st.write("the id is: ", doc.id)
    st.write("contents of db: ", doc.to_dict())