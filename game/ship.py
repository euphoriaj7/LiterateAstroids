# fucnitons 
# - score/points
from game.actor import Actor
from game import constants

class Ship(Actor):

    def __init__(self):
        super().__init__()
        self.texture = constants.SHIP_IDLE
        self.center_x = constants.CENTER_X
        self.center_y = constants.CENTER_Y

