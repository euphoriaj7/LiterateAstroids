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
<<<<<<< HEAD
    def point_to(self, pos): self.physics.point_to(pos[0], pos[1])

    def draw(self):
        # DRAWS THE SHIP AS A LINE POINTING TOWARDS THE CURRENT ANGLE OF ROTATION
        arcade.draw_line(
            CENTER_X, 
            CENTER_Y, 
            CENTER_X - 30 * math.sin(self.physics.get_rotation()),
            CENTER_Y + 30 * math.cos(self.physics.get_rotation()),
            arcade.color.RED,12)

    def update(self):
        """"""
=======
    def point_to(self, pos): self.angle = ((math.atan2(pos[1] - CENTER_Y, pos[0] - CENTER_X) - math.pi/2) * 180/math.pi)
>>>>>>> 01b2f8a72f4cf6ec30fe9a46eb4cb3a68cad017c
