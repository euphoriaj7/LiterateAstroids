import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class DB_Connect():
    def __init__(self):
        self.db = None

    def initialize_firestore(self):
        # Setup Google Cloud Key - The json file is obtained by going to 
        # Project Settings, Service Accounts, Create Service Account, and then
        # Generate New Private Key

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "game/literateastroids-firebase-adminsdk-2y0ix-ed3689b496.json"
        # Use the application default credentials.  The projectID is obtianed 
        # by going to Project Settings and then General.
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
            'projectId': 'literateastroids',
        })
        # Get reference to database
        db = firestore.client()
        self.db = db


    def add_new_score(self, name, score):
        '''
        Prompt the user for a new item to add to the inventory database.  The
        item name must be unique (firestore document id).  
        '''

        # Check for an already existing item by the same name.
        # The document ID must be unique in Firestore.
        result = self.db.collection("literateAstroids").document(name).get()
        if result.exists:
             # Convert data read from the firestore document to a dictionary
            data = result.to_dict()

            # Update the dictionary with the new quanity and then save the 
            # updated dictionary to Firestore.
            if data['score'] < str(score):
                print('new high score!')
                data["score"] = str(score)
                self.db.collection("literateAstroids").document(name).set(data)
            else:
                print('Eh...not your best score...')
            return

        # Build a dictionary to hold the contents of the firestore document.
        data = {"name" : name, 
                "score" : str(score)}
        self.db.collection("literateAstroids").document(name).set(data)
