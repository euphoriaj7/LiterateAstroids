# functions 
# - words and get/setter
from os import O_TEXT
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
from game.data import Data
import arcade
import math
import random

class Astroid(arcade.Sprite):
    def __init__(self, speed): 
        super().__init__(WORKING_DIRECTORY+"\game\images\meteor1.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 3
        self.center_y = SCREEN_HEIGHT / 3
        self.physics = Physics(0, 0, 0, 0, 0)
        self.getLetter()
        self.draw()
        self.spawn_asteroid(speed)
    
    # \\\ GET POS ///
    # Returns the current (x, y) coordinates of the ship
    def get_pos(self): return self.physics.get_pos()

    # to get letter to print in terminal
    def getLetter(self):
        data = Data() 
        letter_asteroid = data.random_word()
        self.text = letter_asteroid
        print(letter_asteroid)

    def draw(self):
        arcade.draw_text(
            "fish sticks",
            SCREEN_WIDTH / 4,
            SCREEN_HEIGHT / 4,
            arcade.csscolor.RED,
            25
            )
        arcade.draw_circle_filled(
            self.physics.get_pos()[0],
            self.physics.get_pos()[1],
            10,
            arcade.color.RED
            )
    
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

        # Set physics to calculated values
        self.physics.set_pos(x, y)
        self.physics.set_velocity(deltaX, deltaY)
    
    def update(self):
        self.center_x = self.physics.get_pos()[0]
        self.center_y = self.physics.get_pos()[1]
        self.physics.tick_update()