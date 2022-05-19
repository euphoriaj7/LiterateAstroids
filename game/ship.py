# fucnitons 
# - score/points
import arcade
from game.actor import Actor
from game.physics import Physics
from game.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHIP_SCALE
    )

class Ship(arcade.Sprite):
    def __init__(self): 
        super().__init__("game/images/spaceship.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        #self.set_image("images\spaceship.png")
        #self.set_position(640, 360)
    
    def draw(self):
        pass

    def update(self):
        """"""


