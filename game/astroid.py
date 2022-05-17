# functions 
# - words and get/setter

from game.actor import Actor
from game.physics import Physics

class Astroid(Actor):

    def __init__(self):
        super().__init__()
        self.set_image("images\spaceship.png")
        self.set_position(640, 360)



