# functions
# - words and get/setter
from game.constants import (
    CENTER_X,
    CENTER_Y,
    SHIP_SCALE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WORKING_DIRECTORY,
    FONT
)
import arcade
import math
import random

class Astroid(arcade.Sprite):
    
    def __init__(self, speed, new_word):
        super().__init__(WORKING_DIRECTORY+"/game/images/meteor1.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 3
        self.center_y = SCREEN_HEIGHT / 3
        self.spawn_asteroid(speed)

        # gets active word/letter from inputs
        self.word = new_word
        # It currently reads an extra space. This deletes that space
        self.word = self.word[:-1]
        # A uniquie id to make sure the correct asteroid is shot
        self.id = random.randint(0,10000)

    # returns the uniquie id for the asteroid
    def get_id(self): return self.id

    def get_word(self): return self.word

    def draw_letter(self, color):
        # printing it in the screen
        arcade.draw_text(self.word, self.center_x, self.center_y, color, 30, font_name=(FONT,))
        # print(FONT)

    # \\\ GET POS ///
    # Returns the current (x, y) coordinates
    def get_pos(self): return self.center_x, self.center_y

    # \\\ SPAWN ASTEROID ///
    # Gets a random angle and spawns the asteroid at that angle and sets its veclocity towards
    # the center of the screen
    def spawn_asteroid(self, speed):
        # Randomly select the side the spawing will happen
        side = random.randint(1, 2)
        spawn_radius = math.sqrt(CENTER_X**2 + CENTER_Y**2) + 30

        # Set a random spawn angle based on the side selected
        if (side == 1):
            theta = random.uniform(
                math.atan2(-SCREEN_WIDTH, -SCREEN_HEIGHT), math.atan2(-SCREEN_WIDTH, SCREEN_HEIGHT))
        else:
            theta = random.uniform(math.atan2(
                SCREEN_WIDTH, -SCREEN_HEIGHT), math.atan2(SCREEN_WIDTH, SCREEN_HEIGHT))

        # Set the spawn coordinates based on the spawn angle
        self.center_x = CENTER_X - spawn_radius * math.sin(theta)
        self.center_y = CENTER_Y + spawn_radius * math.cos(theta)

        # Set the velocity vector based on the spawn angle + 180 degrees
        self.change_x = speed * math.cos(theta - (math.pi/2))
        self.change_y = speed * math.sin(theta - (math.pi/2))

        # Set rotation to a random spin one way or the other
        self.angle = random.randint(-180, 180)
        self.change_angle = random.uniform(-1, 1)