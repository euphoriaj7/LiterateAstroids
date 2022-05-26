# functions 
# - words and get/setter
from os import O_TEXT
from game.constants import (
    CENTER_X,
    CENTER_Y,
    SHIP_SCALE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WORKING_DIRECTORY,
    
)
from game.actor import Actor
from game.physics import Physics
from game.data import Data
from game.inputs import Inputs
import arcade

class Astroid(arcade.Sprite):
    def __init__(self, x, y, deltaX, deltaY, inputs): 
        super().__init__(WORKING_DIRECTORY+"\game\images\meteor1.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 3
        self.center_y = SCREEN_HEIGHT / 3
        self.physics = Physics(x, y, deltaX, deltaY, 0)
        self.inputs = inputs
        self.getLetter()
        self.draw()
        
    
    # \\\ GET POS ///
    # Returns the current (x, y) coordinates of the ship
    def get_pos(self): return self.physics.get_pos()

    # to get letter to print in terminal
    def getLetter(self):
        data = Data() 
        letter_asteroid = data.random_word()
        self.text = letter_asteroid
        print(letter_asteroid)

    def draw(self):
        
        arcade.draw_circle_filled(
            self.physics.get_pos()[0],
            self.physics.get_pos()[1],
            10,
            arcade.color.RED
            )
        arcade.draw_text(
            self.inputs.get_active_word(),
            self.physics.get_pos()[0],
            self.physics.get_pos()[1],
            arcade.csscolor.WHITE,
            25
        )
    
    def update(self):
        self.center_x = self.physics.get_pos()[0]
        self.center_y = self.physics.get_pos()[1]
        self.physics.tick_update()