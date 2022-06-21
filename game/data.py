import random
from game.constants import WORKING_DIRECTORY

# // have to be this way


class Data():

    def __init__(self):
        self.list_of_words = []

    # to read in txt file into list_of_words
    def read_words(self):
        file = open(WORKING_DIRECTORY+"/game/words.txt", "r")
        for words in file:
            self.list_of_words.append(words)

# to get random number to get random word
    def random_word(self, score):
        # adding levels
        # 197 - word with tree letters and under
        # 26 - single letters
        # 227 - four letter words 
        if score > 45:
            high_word = 227
            low_word = 26
        elif score > 30:
            high_word = 197
            low_word = 26
        elif score > 15:
            high_word = 197
            low_word = 0
        else:
            low_word = 0
            high_word = 26
        self.read_words()
        # low_word is the lowest number to read in file 
        # high _ word is the highest number to read in file 
        random_numer_word = random.randrange(low_word,high_word)
        letter = self.list_of_words[random_numer_word]
        return letter
