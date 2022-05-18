# fucnitons 
# - score/points

from game.actor import Actor
from game.physics import Physics

class Ship(Actor):
    def __init__(self): 
        super().__init__()
        self.set_image("images\spaceship.png")
        self.set_position(640, 360)



