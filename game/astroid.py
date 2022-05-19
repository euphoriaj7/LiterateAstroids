# functions 
# - words and get/setter

from game.actor import Actor
from game.physics import Physics
from game.data import Data

class Astroid(Actor):

    def __init__(self):
        words = None

# to get letter to print in terminal
    def getLetter(self):
        words = Data() 
        letter_asteroid = words.random_word()
        print(letter_asteroid)
        



