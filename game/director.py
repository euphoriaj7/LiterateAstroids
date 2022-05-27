#from LiterateAstroids.game.constants import CENTER_X, CENTER_Y
from ast import In
from distutils.spawn import spawn
import arcade
import math
import random
import time

from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    CENTER_X,
    CENTER_Y,
    WORKING_DIRECTORY,
)
from game.astroid import Astroid
from game.laser import Laser
from game.ship import Ship
from game.inputs import Inputs

class Director(arcade.View):

    def __init__(self):
        super().__init__()
        self.spritelist = None
        self.asteroidlist = None
        self.laserlist = None
        self.ship = None
        self.astroid = None
        self.inputs = None
        
        # THIS IS PURELY A TEST VALUE (delete later)
        self.test_counter = 0

    def setup(self):
        self.background = arcade.load_texture(WORKING_DIRECTORY+"\game\images\stars.png")
        self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\game\images\shipshell.png")
        
        self.spritelist = arcade.SpriteList() # creates a sprite list under name spritelist
        self.asteroidlist = arcade.SpriteList()
        self.laserlist = arcade.SpriteList()
        
        self.ship = Ship()
        self.inputs = Inputs()
        self.spritelist.append(self.ship) # adds actor(all sprites) to sprite list /// THIS NEEDS TO BE THE FIRST ITEM ///
        self.spritelist.append(self.inputs) # adds the keyboard inputs as a sprite
        self.asteroidlist.append(Astroid(2)) # spawn in the first asteroid
        
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.foreground)

        # Updates graphics for all sprites
        self.spritelist.draw()
        ##for sprite in self.spritelist:      sprite.draw()
        for sprite in self.asteroidlist:    sprite.draw()
        for sprite in self.laserlist:       sprite.draw()
        #place score and word box

    # Check for key press and for is_match signal
    # Spawns new asteroid with new word if there is a match
    # Spawns a new laser pointed at the first asteroid in the list
    def on_key_press(self, symbol, modifer):
        if self.inputs.pressed(symbol, modifer):
            self.asteroidlist.append(Astroid(2))
            self.spritelist[0].point_to(self.asteroidlist[0].get_pos())
            self.laserlist.append(Laser(40, self.spritelist[0].get_rotation()))
            
    # Check for key release
    def on_key_release(self, symbol, modifier): self.inputs.released(symbol, modifier)
    
    def on_update(self, delta_time):
        self.spritelist.update() # updates all sprites
        self.asteroidlist.update()
        self.laserlist.update()

        # Check for collisions with the laser and the asteroids
        # Delete both if there is contact
        if (len(self.laserlist) > 0):
            if arcade.check_for_collision(self.asteroidlist[0], self.laserlist[0]):
                self.laserlist.pop(0)
                self.asteroidlist.pop(0)
        
        # # ASTEROID/LASER SPAWNING/DESTRUCTION BENCHMARK
        # self.test_counter += 1
        # spawn_freq = 25
        # if (self.test_counter%spawn_freq>=spawn_freq-1):
        #     self.asteroidlist.append(Astroid(2))
        #     self.spritelist[0].point_to(self.asteroidlist[0].get_pos())
        #     self.laserlist.append(Laser(40, self.spritelist[0].get_rotation()))

    