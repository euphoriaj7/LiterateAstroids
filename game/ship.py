# fucnitons 
# - score/points
import arcade
import math
from game.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    CENTER_X,
    CENTER_Y,
    SHIP_SCALE,
    WORKING_DIRECTORY,
    )

class Ship(arcade.Sprite):
    def __init__(self): 
        super().__init__(WORKING_DIRECTORY+"\game\images\spaceship.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2

    # \\\ POINT TO ///
    # Points the ship towards the passed coordinates
    def point_to(self, pos): self.angle = ((math.atan2(pos[1] - CENTER_Y, pos[0] - CENTER_X) - math.pi/2) * 180/math.pi)
