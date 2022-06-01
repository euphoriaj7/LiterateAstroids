import random
from game.constants import WORKING_DIRECTORY

# // have to be this way
class Data():

    def __init__(self):
        self.list_of_words = []

    #to read in txt file into list_of_words
    def read_words(self):
        file = open(WORKING_DIRECTORY+"\game\words.txt", "r")
        for words in file:
            self.list_of_words.append(words)

# to get random number to get random word
    def random_word(self):
        self.read_words()
        random_numer_word = random.randrange(0,196)
        letter = self.list_of_words[random_numer_word]
        return letter