

class data():

    def __init__(self):
        self.list_of_words = []

    #to read in txt file into list_of_words
    def read_words(self):
        file = open("words.txt", "r")
        for words in file:
            self.list_of_words.append(words)

    