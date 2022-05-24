#from LiterateAstroids.game.constants import CENTER_X, CENTER_Y
from ast import In
import arcade
import math
import random

from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    CENTER_X,
    CENTER_Y,
    WORKING_DIRECTORY,
)
from game.astroid import Astroid
from game.ship import Ship
from game.inputs import Inputs

class Director(arcade.View):

    def __init__(self):
        super().__init__()
        self.spritelist = None
        self.ship = None
        self.astroid = None
        self.inputs = None

    def setup(self):
        self.background = arcade.load_texture(WORKING_DIRECTORY+"\LiterateAstroids\game\images\stars.png")
        self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\LiterateAstroids\game\images\shipshell.png")
        self.spritelist = arcade.SpriteList() # creates a sprite list under name spritelist
        self.ship = Ship()
        # TESTING SPAWN ASTEROID CODE
        self.astroid = self.spawn_asteroid(2)
        # TESTING KEYBOARD INPUT
        self.inputs = Inputs()

        self.spritelist.append(self.ship) # adds actor(all sprites) to sprite list
        self.spritelist.append(self.astroid)
        self.spritelist.append(self.inputs) # adds the keyboard inputs as a sprite
        
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        #self.spritelist.draw() # adds all actors to screen
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.foreground)

        # Updates graphics for all actors // THIS IS ADDED IN AS A FIX TO self.spritelist.draw()
        for sprite in self.spritelist: sprite.draw()
        #place score and word box

    # Check for key press and call the inputs object
    def on_key_press(self, symbol, modifer):
        self.inputs.pressed(symbol, modifer)
    
    def on_update(self, delta_time):
        self.spritelist.update() # updates all sprites
        #call check collisions
        #update health & score

        # COMMENT THIS IN TO TEST MULTIPLE ASTEROIDS
        # self.spritelist.append(self.spawn_asteroid(20))

    # \\\ SPAWN ASTEROID ///
    # Gets a random angle and spawns the asteroid at that angle and sets its veclocity towards
    # the center of the screen
    def spawn_asteroid(self, speed):
        # Randomly select the side the spawing will happen
        side = random.randint(1,2)

        # Set a random spawn angle based on the side selected
        if (side == 1): theta = random.uniform(math.atan2(-SCREEN_WIDTH,-SCREEN_HEIGHT), math.atan2(-SCREEN_WIDTH,SCREEN_HEIGHT))
        else:           theta = random.uniform(math.atan2(SCREEN_WIDTH,-SCREEN_HEIGHT), math.atan2(SCREEN_WIDTH,SCREEN_HEIGHT))

        # Set the spawn coordinates based on the spawn angle
        x = CENTER_X - (CENTER_X * math.sin(theta))
        y = CENTER_Y + (100 + CENTER_X) * math.cos(theta)

        # Set the velocity vector based on the spawn angle + 180 degrees
        deltaX = speed * math.cos(theta - (math.pi/2))
        deltaY = speed * math.sin(theta - (math.pi/2))

        # Return a new asteroid object
        return Astroid(x, y, deltaX, deltaY)

    # \\\ SPAWN LASER ///
    # Spawns a laser from the direction the ship is currently pointing
    def spawn_laser(self, rotation):
        pass
    
#MOrgan 