import arcade
from matplotlib.pyplot import draw
from sympy import false
from game.constants import (
    SHIP_SCALE, 
    WORKING_DIRECTORY
    )

class Boom(arcade.Sprite):

    def __init__(self, x, y, explode_time):
        super().__init__(WORKING_DIRECTORY+'/game/images/explosion.png', SHIP_SCALE)
        self.center_x = x
        self.center_y = y
        self.explode_time = explode_time
        self.count = 0
        self.explode_done = False


    def update(self):
        super().update()

        if self.explode_done == False:
            self.count += 1
        
            if self.count >= self.explode_time:
                self.alpha = 0
                self.explode_done = True
                del self