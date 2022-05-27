# functions 
# - words and get/setter
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
import random

class Astroid(arcade.Sprite):
    def __init__(self, speed): 
        super().__init__(WORKING_DIRECTORY+"\game\images\meteor1.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 3
        self.center_y = SCREEN_HEIGHT / 3
        self.spawn_asteroid(speed)
    
    # \\\ GET POS ///
    # Returns the current (x, y) coordinates
    def get_pos(self): return self.center_x, self.center_y
    
    # \\\ SPAWN ASTEROID ///
    # Gets a random angle and spawns the asteroid at that angle and sets its veclocity towards
    # the center of the screen
    def spawn_asteroid(self, speed):
        # Randomly select the side the spawing will happen
        side = random.randint(1,2)
        spawn_radius = math.sqrt(CENTER_X**2 + CENTER_Y**2) + 30

        # Set a random spawn angle based on the side selected
        if (side == 1): theta = random.uniform(math.atan2(-SCREEN_WIDTH,-SCREEN_HEIGHT), math.atan2(-SCREEN_WIDTH,SCREEN_HEIGHT))
        else:           theta = random.uniform(math.atan2(SCREEN_WIDTH,-SCREEN_HEIGHT), math.atan2(SCREEN_WIDTH,SCREEN_HEIGHT))

        # Set the spawn coordinates based on the spawn angle
        x = CENTER_X - spawn_radius * math.sin(theta)
        y = CENTER_Y + spawn_radius * math.cos(theta)

        # Set the velocity vector based on the spawn angle + 180 degrees
        deltaX = speed * math.cos(theta - (math.pi/2))
        deltaY = speed * math.sin(theta - (math.pi/2))

        # Set positional updates to calculated values
        self.center_x = x
        self.center_y = y
        self.change_x = deltaX
        self.change_y = deltaY

        # Set rotation to a random spin one way or the other
        self.angle = random.randint(-180, 180) 
        self.change_angle = random.uniform(-1,1)