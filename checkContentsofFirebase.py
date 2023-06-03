# pip install firebase-admin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# use the json file you downloaded from firebase
cred = credentials.Certificate(r"C:\Users\core i5\Documents\GitHub\DataScience\PD_2\FireBaseDataBase\Firebase_Upload_RawData\credentials\copper-oven-382608-ea1f4baca1f3.json") 
app = firebase_admin.initialize_app(cred)
db = firestore.client()
# doc_ref = db.collection("users").document("xnSSNwkYrEduqQoEY0H0")
users_ref = db.collection("users")
docs = users_ref.stream()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

'''
prints:
xnSSNwkYrEduqQoEY0H0 => {'AirFlow': [32, 5, 6, 6], 'Snore': [32, 5, 6, 6], 'SpO2': [32, 5, 6, 6], 'Therm': [32, 5, 6, 6], 'ECG': [32, 5], 'HR': [32, 5, 6, 6]}
'''
