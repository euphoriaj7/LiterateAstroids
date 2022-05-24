import arcade
import math
import random

from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from game.astroid import Astroid
from game.ship import Ship

class Director(arcade.View):

    def __init__(self):
        super().__init__()
        self.spritelist = None
        self.ship = None
        self.astroid = None
        self.input = None

    def setup(self):
        self.background = arcade.load_texture('game/images/stars.png')
        self.foreground = arcade.load_texture('game/images/shipshell.png')
        self.spritelist = arcade.SpriteList() # creates a sprite list under name spritelist
        self.ship = Ship()
        #self.astroid = Astroid()
        
        # TESTING SPAWN ASTEROID CODE
        self.astroid = self.spawn_asteroid(2)

        self.spritelist.append(self.ship) # adds actor(all sprites) to sprite list
        self.spritelist.append(self.astroid)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.spritelist.draw() # adds all actors to screen
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.foreground)
        #place score and word box
    
    def on_update(self):
        self.spritelist.update() # updates all sprites
        #call check collisions
        #update health & score

    # \\\ SPAWN ASTEROID ///
    # Gets a random angle and spawns the asteroid at that angle and sets its veclocity towards
    # the center of the screen
    def spawn_asteroid(self, speed):
        # Randomly select the side the spawing will happen
        side = random.randint(1,2)

        # Set a random spawn angle based on the side selected
        if (side == 1): theta = random.randrange(-1*math.pi, math.pi)
        else:           theta = random.randrange(-1*math.pi, math.pi)

        # Set the spawn coordinates based on the spawn angle
        x = (SCREEN_WIDTH * math.cos(theta)) - (SCREEN_HEIGHT * math.sin(theta))
        y = (SCREEN_HEIGHT * math.cos(theta)) + (SCREEN_WIDTH * math.sin(theta))

        # Set the velocity vector based on the spawn angle + 180 degrees
        deltaX = speed * math.cos(theta + math.pi)
        deltaY = speed * math.sin(theta + math.pi)

        # Return a new asteroid object
        return Astroid(x, y, deltaX, deltaY)
    
#MOrgan 