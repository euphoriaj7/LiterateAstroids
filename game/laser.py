# points/score and will need key board 
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
import arcade

class Laser(arcade.Sprite):
    def __init__(self, x, y, deltaX, deltaY, rotation): 
        super().__init__(WORKING_DIRECTORY+"\game\images\meteor1.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 3
        self.center_y = SCREEN_HEIGHT / 3
        self.physics = Physics(x, y, deltaX, deltaY, rotation)
        self.getLetter()
        self.draw()