#import libraries to access operating system and google firebase
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class DB_Connect():
    #declare variable to hold database
    def __init__(self):
        self.db = None

    def initialize_firestore(self):
        #Get Google Firebase key -- Read in private key from game
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "game/literateastroids-firebase-adminsdk-2y0ix-ed3689b496.json"
        
        #Get the application credentials (project ID name)
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
            'projectId': 'literateastroids',
        })
        
        #Get reference to database
        db = firestore.client()

        #assign database to variable
        self.db = db


    def add_new_score(self, name, score):
        '''
        Add in a new score to the database
        '''

        #Check for an already existing user by the same name.
        result = self.db.collection("literateAstroids").document(name).get()
        if result.exists:

            #Convert data read from the firestore document to a dictionary
            data = result.to_dict()

            # Update the dictionary with the new score if it's higher and then save the 
            # updated dictionary to Firestore. This will allow us to keep track of individual high scores.
            if data['score'] < int(score):
                data["score"] = int(score)
                self.db.collection("literateAstroids").document(name).set(data)
                return 'New High Score!'
            else:
                return 'Eh...not your best score...'

         #If the user isn't already in our database, build a dictionary to insert their name
         #and score to the database.
        else:
            data = {"name" : name, 
                "score" : int(score)}
            self.db.collection("literateAstroids").document(name).set(data)
            return "Great First Score!"



    def get_top_five(self):
        '''
        Gather the top five scores to a dictionary to display at gameover.
        '''
        #Get all users/scores from the database
        results = self.db.collection("literateAstroids").get()

        #Create a list to hold each row in the database
        list_scores = []

        #Loop through results to see individual scores
        for result in results:

            #convert each row to a readable dictionary
            row = result.to_dict()

            #append row to database to keep the scores and names together
            list_scores.append(row)

        #sort list by score to see the highest scores
        newlist = sorted(list_scores, key=lambda d: int(d['score'])) 

        #create a list to hold the top five scores
        topFive = []

        #Only grab the bottom (highest) five scores in the list
        for i in range(5):

            #grab score at the end of the list
            score = newlist.pop()

            #append it to a new list
            topFive.append(score)

        #create a dictionary to hold a formatted list of the top five scores
        topfive = dict()

        #set variable to keep track of place in the top five
        j = 0

        #loop through top five formatting the names and order
        for i in topFive:

            #update placeholder
            j += 1

            #go through each key and score
            for key, value in i.items():

                #determine if it's a name value or score
                if key == 'name':

                    #assign place in scoreboard as key name
                    newKeyName = 'name' + str(j)

                    #assign name to the key for that value
                    topfive[newKeyName] = value
                    
                
                else:

                    #assign place in scoreboard as key score
                    newKeyScore = 'score' + str(j)

                    #assign score to the key for that value
                    topfive[newKeyScore] = value
        
        #return top five scores, ordered and formatted
        return topfive
        
