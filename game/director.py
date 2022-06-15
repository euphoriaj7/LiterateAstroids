#from LiterateAstroids.game.constants import CENTER_X, CENTER_Y
from pickle import NONE
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
from game.data import Data
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
        self.data = Data()
        self.inputs = Inputs()
        self.tracker = Tracker()
        self.gameover = GameOver()
        self.text = None
        self.spawning = False   # DO NOT CHANGE
        self.spawn_counter = 1  # DO NOT CHANGE

        # ASTEROID SPAWN PARAMETERS
        self.spawn_amount = 3
        self.spawn_interval = 100

    def setup(self):
        self.background = arcade.load_texture(
            WORKING_DIRECTORY+"/game/images/stars.png")

        # creates a sprite list under name spritelist
        self.spritelist = arcade.SpriteList()
        self.asteroidlist = arcade.SpriteList()
        self.laserlist = arcade.SpriteList()

        self.ship = Ship()
        self.inputs = Inputs()
        # adds ship to sprite list /// THIS NEEDS TO BE THE FIRST ITEM ///
        self.spritelist.append(self.ship)

    def on_draw(self):
        arcade.start_render()
        # Draw background
        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Updates graphics for all sprites
        self.laserlist.draw()
        self.spritelist.draw()
        self.asteroidlist.draw()
        # Makes the first text in the list red, and the rest green
        for i in range(len(self.asteroidlist)):
            if i == 0:
                self.asteroidlist[i].draw_letter(arcade.color.RED)
            else:
                self.asteroidlist[i].draw_letter(arcade.color.GREEN)

        # Draw foreground
        if self.tracker.gethp() == 6:
            self.foreground = arcade.load_texture(
                WORKING_DIRECTORY+"/game/images/shipshellH6.png")
        elif self.tracker.gethp() == 5:
            self.foreground = arcade.load_texture(
                WORKING_DIRECTORY+"/game/images/shipshellH5.png")
        elif self.tracker.gethp() == 4:
            self.foreground = arcade.load_texture(
                WORKING_DIRECTORY+"/game/images/shipshellH4.png")
        elif self.tracker.gethp() == 3:
            self.foreground = arcade.load_texture(
                WORKING_DIRECTORY+"/game/images/shipshellH3.png")
        elif self.tracker.gethp() == 2:
            self.foreground = arcade.load_texture(
                WORKING_DIRECTORY+"/game/images/shipshellH2.png")
        elif self.tracker.gethp() == 1:
            self.foreground = arcade.load_texture(
                WORKING_DIRECTORY+"/game/images/shipshellH1.png")
        elif self.tracker.gethp() < 1:
            self.foreground = arcade.load_texture(
                WORKING_DIRECTORY+"/game/images/shipshellH0.png")

        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.foreground)

        # Update text on screen
        self.inputs.draw(str(self.tracker.getscore()))

    # Check for key press and for is_match signal
    # Spawns new asteroid with new word if there is a match
    # Spawns a new laser pointed at the first asteroid in the list
    def on_key_press(self, symbol, modifer):
        # Waches for the "word matched" signal from the inputs object
        if len(self.asteroidlist) > 0:
            word = self.asteroidlist[0].get_word()
        else:
            word = ""
        if self.inputs.pressed(symbol, modifer, word) and len(self.asteroidlist) > 0:
            self.spritelist[0].point_to(self.asteroidlist[0].get_pos())

    # Check for key release

    def on_key_release(self, symbol, modifier): self.inputs.released(
        symbol, modifier)

    def on_update(self, delta_time):
        for sprite in self.spritelist:
            if sprite.update() == True:
                self.laserlist.append(
                    Laser(40, self.spritelist[0].get_target_angle()))

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

        # spawn_counter is used to spawn multiple asteroids with a 30 tick gap
        if len(self.asteroidlist) <= 0 and self.spawning == False:
            self.spawning = True
            self.spawn_counter = self.spawn_interval * self.spawn_amount
        if self.spawn_counter % self.spawn_interval == 0:
            self.asteroidlist.append(Astroid(2, self.data.random_word()))
        if self.spawn_counter >= 2:
            self.spawn_counter -= 1
        if self.spawn_counter < 2:
            self.spawning = False

        # This came from morgan's branch

        # if arcade.check_for_collision(self.asteroidlist[0], self.spritelist[0]):
        #     self.asteroidlist.pop(0)
        #     if self.tracker.gethp() > 1:
        #         self.tracker.minushp()
        #     else:
        #         # Wait 2 seconds
            # self.gameover.gather(str(self.tracker.getscore()))
        #         self.window.show_view(self.gameover)

        if len(self.asteroidlist) > 0 and len(self.asteroidlist) > 0:
            if arcade.check_for_collision(self.asteroidlist[0], self.spritelist[0]):
                self.asteroidlist.pop(0)
                if self.tracker.gethp() > 1:
                    self.tracker.minushp()
                else:
                    # Wait 2 seconds
                    self.gameover.gather(
                        str(self.tracker.getscore()), self.inputs)
                    self.window.show_view(self.gameover)

        for laser in self.laserlist:
            if laser.get_pos()[0] > SCREEN_WIDTH or laser.get_pos()[0] < 0:
                laser.remove_from_sprite_lists()
            if laser.get_pos()[1] > SCREEN_HEIGHT or laser.get_pos()[1] < 0:
                laser.remove_from_sprite_lists()
