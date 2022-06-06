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
    WORKING_DIRECTORY,
)
from game.astroid import Astroid
from game.laser import Laser
from game.ship import Ship
from game.inputs import Inputs
from game.tracker import Tracker
from game.gameover import GameOver

class Director(arcade.View):

    def __init__(self):
        super().__init__()
        self.spritelist = None
        self.asteroidlist = None
        self.laserlist = None
        self.ship = None
        self.astroid = None
        self.inputs = Inputs()
        self.tracker = Tracker()
        self.gameover = GameOver()
        self.text = None
        
    def setup(self):
        self.background = arcade.load_texture(WORKING_DIRECTORY+"\game\images\stars.png")
        
        self.spritelist = arcade.SpriteList() # creates a sprite list under name spritelist
        self.asteroidlist = arcade.SpriteList()
        self.laserlist = arcade.SpriteList()
        
        self.ship = Ship()
        self.inputs = Inputs()
        self.spritelist.append(self.ship) # adds ship to sprite list /// THIS NEEDS TO BE THE FIRST ITEM ///
        
    def on_draw(self):
        arcade.start_render()
        # Draw background
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Updates graphics for all sprites
        self.laserlist.draw()
        self.spritelist.draw()
        self.asteroidlist.draw()
        for astroid in self.asteroidlist:
            astroid.draw_letter()

        # Draw foreground
        if self.tracker.gethp() == 6:
            self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\game\images\shipshellH6.png")
        elif self.tracker.gethp() == 5:
            self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\game\images\shipshellH5.png")
        elif self.tracker.gethp() == 4:
            self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\game\images\shipshellH4.png")
        elif self.tracker.gethp() == 3:
            self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\game\images\shipshellH3.png")
        elif self.tracker.gethp() == 2:
            self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\game\images\shipshellH2.png")
        elif self.tracker.gethp() == 1:
            self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\game\images\shipshellH1.png")
        elif self.tracker.gethp() < 1:
            self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\game\images\shipshellH0.png")
        
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.foreground)

        # Update text on screen
        self.inputs.draw(str(self.tracker.getscore()))

    # Check for key press and for is_match signal
    # Spawns new asteroid with new word if there is a match
    # Spawns a new laser pointed at the first asteroid in the list
    def on_key_press(self, symbol, modifer):
        # Waches for the "word matched" signal from the inputs object
        if self.inputs.pressed(symbol, modifer) and len(self.asteroidlist) > 0: self.spritelist[0].point_to(self.asteroidlist[0].get_pos())
            
            
    # Check for key release
    def on_key_release(self, symbol, modifier): self.inputs.released(symbol, modifier)
    
    def on_update(self, delta_time):
        for sprite in self.spritelist:
            if sprite.update() == True: self.laserlist.append(Laser(40, self.spritelist[0].get_target_angle())) 

        self.asteroidlist.update()
        self.laserlist.update()

        # Update keyboard inputs
        self.inputs.update()

        # Check for collisions with the laser and the asteroids
        # Delete both if there is contact
        if (len(self.laserlist) > 0 and len(self.asteroidlist) > 0):
            if arcade.check_for_collision(self.asteroidlist[0], self.laserlist[0]):
                self.laserlist.pop(0)
                self.asteroidlist.pop(0)
                self.tracker.addscore()
        
        if len(self.asteroidlist) <= 0:
            self.asteroidlist.append(Astroid(2, self.inputs))

        if arcade.check_for_collision(self.asteroidlist[0], self.spritelist[0]):
            self.asteroidlist.pop(0)
            if self.tracker.gethp() > 1:
                self.tracker.minushp()
            else:
                # Wait 2 seconds
                self.window.show_view(self.gameover)

        for laser in self.laserlist:
            if laser.get_pos()[0] > SCREEN_WIDTH or laser.get_pos()[0] < 0:     laser.remove_from_sprite_lists()
            if laser.get_pos()[1] > SCREEN_HEIGHT or laser.get_pos()[1] < 0:    laser.remove_from_sprite_lists()