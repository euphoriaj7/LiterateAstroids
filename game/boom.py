import arcade
from game.constants import (
    SHIP_SCALE, 
    WORKING_DIRECTORY
    )

class Boom(arcade.Sprite):

    def __init__(self):
        super().__init__(WORKING_DIRECTORY+'/game/images/explosion.png', SHIP_SCALE)

