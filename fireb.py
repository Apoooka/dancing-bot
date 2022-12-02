import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("dance-f1a3b-firebase-adminsdk-qbw2c-a1c46c2f0a.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://dance-f1a3b-default-rtdb.firebaseio.com/'
})