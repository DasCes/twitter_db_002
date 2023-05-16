import datetime

import streamlit as st
from google.cloud import firestore
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
import time


num = 0

# qui ci stiamo autenticando a Firestore con la chiave json scaricata e inserita nel progetto
db = firestore.Client.from_service_account_json("firestore-key.json")

# definiamo il riferimento al db
db_ref = db.collection("tws1")


# df = pd.read_csv(f'data/data.csv', index_col=[0])
# df = df.head(12)
#
#
#
# def aggiungiTweetOgniNSecondi():
#
#     collection_name = "tws1"
#
#     element = {
#         "datetime": datetime.datetime.now()
#     }
#
#     # Update the database if element is absent
#     update_database_if_element_absent(collection_name, element)
#
#
#
#
# def update_database_if_element_absent(collection_name, element):
#     parameter_name = "datetime"  # Replace with the name of your parameter field
#
#     # Check if the element is already present
#     if is_element_present(collection_name, parameter_name, element[parameter_name]):
#         print("Element already exists:", element)
#     else:
#         # Update the Firestore collection with the new element
#         doc_ref = db.collection(collection_name).document()
#         doc_ref.set(element)
#         print("Element added to the database:", element)
#
#
# def is_element_present(collection_name, parameter_name, parameter_value):
#     # Check if the element is present in the collection
#     query = db.collection(collection_name).where(parameter_name, "==", parameter_value).limit(1).get()
#     return len(query) > 0
#
#
#     # for index, row in df.iterrows():
#     #     doc_ref = db_ref.document("i" + str(index))
#     #     doc = doc_ref.get()
#     #
#     #     if not doc.exists:
#     #         doc_ref.set({
#     #             'id': index,
#     #             'text': row['text'],
#     #             'date': date
#     #         })
#
#
#
# # Create a scheduler
# scheduler = BackgroundScheduler()
#
#
# # Schedule the job to run every WAIT_SECONDS
# scheduler.add_job(aggiungiTweetOgniNSecondi, 'interval', seconds=30)
#
# # Start the scheduler
# scheduler.start()

# stampiamo tutto il db con un ciclo
print_db_ref = db.collection("tws1").order_by("id")

for doc in print_db_ref.stream():
    st.write("aggiornamento numero: ", datetime.datetime.now())
    st.write("the id is: ", doc.id)
    st.write("contents of db: ", doc.to_dict())


