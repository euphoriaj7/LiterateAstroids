# functions 
# - words and get/setter
from game.constants import (
    SHIP_SCALE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)
from game.actor import Actor
from game.physics import Physics
from game.data import Data
import arcade

class Astroid(arcade.Sprite):
    def __init__(self): 
        super().__init__("game/images/spaceship.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 3
        self.center_y = SCREEN_HEIGHT / 3
        self.text = ""
        # data = Data() 
        # letter_asteroid = data.random_word()
        # print(letter_asteroid)
        self.getLetter(self)

# to get letter to print in terminal
    def getLetter(self):
        data = Data() 
        letter_asteroid = data.random_word()
        self.text = letter_asteroid
        print(letter_asteroid)
        
        



