# functions 
# - words and get/setter
from os import O_TEXT
from game.constants import (
    CENTER_X,
    CENTER_Y,
    SHIP_SCALE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)
from game.actor import Actor
from game.physics import Physics
from game.data import Data
import arcade

class Astroid(arcade.Sprite):
    def __init__(self, x, y, deltaX, deltaY): 
        super().__init__("game/images/meteor1.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 3
        self.center_y = SCREEN_HEIGHT / 3
        self.physics = Physics(x, y, deltaX, deltaY, 0)
        self.getLetter()
        self.draw()

    # to get letter to print in terminal
    def getLetter(self):
        data = Data() 
        letter_asteroid = data.random_word()
        self.text = letter_asteroid
        print(letter_asteroid)

    def draw(self):
        arcade.draw_text(
            "fish sticks",
            SCREEN_WIDTH / 4,
            SCREEN_HEIGHT / 4,
            arcade.csscolor.RED,
            25
            )
        arcade.draw_circle_filled(
            self.physics.get_pos()[0],
            self.physics.get_pos()[1],
            10,
            arcade.color.RED
            )
    
    def update(self):
        self.physics.tick_update()