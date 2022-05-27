# points/score and will need key board 
from game.constants import (
    CENTER_X,
    CENTER_Y,
    SHIP_SCALE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WORKING_DIRECTORY,
)
import arcade
import math

class Laser(arcade.Sprite):
    def __init__(self, speed, ship_rotation): 
        super().__init__(WORKING_DIRECTORY+"\game\images\laser.png", SHIP_SCALE/20)
        self.center_x = SCREEN_WIDTH / 3
        self.center_y = SCREEN_HEIGHT / 3
        self.draw()
        self.spawn_laser(speed, ship_rotation)

    # \\\ GET POS ///
    # Returns the current (x, y) coordinates
    def get_pos(self): return self.center_x, self.center_y

    # \\\ SPAWN LASER ///
    # Spawns a laser from the direction the ship is currently pointing
    def spawn_laser(self, speed, theta):
        theta = math.radians(theta)
        spawn_radius = 20

        # Set the spawn coordinates based on the spawn angle
        x = CENTER_X - spawn_radius * math.sin(theta)
        y = CENTER_Y + spawn_radius * math.cos(theta)

        # Set the veclocity vector pointing the same direction as the spawn angle
        deltaX = speed * math.cos(theta + (math.pi/2))
        deltaY = speed * math.sin(theta + (math.pi/2))

        # Set positional updates to calculated values
        self.center_x = x
        self.center_y = y
        self.change_x = deltaX
        self.change_y = deltaY
        self.angle = theta * 180 /math.pi