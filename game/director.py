#from LiterateAstroids.game.constants import CENTER_X, CENTER_Y
import arcade

from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    WORKING_DIRECTORY,
)
from game.astroid import Astroid
from game.db_connect import DB_Connect
from game.laser import Laser
from game.ship import Ship
from game.data import Data
from game.inputs import Inputs
from game.tracker import Tracker
from game.gameover import GameOver
from game.db_connect import DB_Connect
from game.boom import Boom


class Director(arcade.View):

    def __init__(self):
        super().__init__()
        self.spritelist = None
        self.explosionlist = None
        self.asteroidlist = None
        self.laserlist = None
        self.ship = None
        self.astroid = None
        self.data = Data()
        self.inputs = Inputs()
        self.tracker = Tracker()
        self.gameover = GameOver()
        self.db = DB_Connect()
        self.text = None
        self.sig_gameover = False
        self.spawning = False   # DO NOT CHANGE
        self.spawn_counter = 1  # DO NOT CHANGE

        #sounds 
       
        # like this better for laser
        self.laser_sound = arcade.load_sound("game\sounds\laser_gun.wav")
        #sound for end of game explosion
        self.explosion_sound = arcade.load_sound("game\sounds\ship_explode.wav")
        # for asteroid hitting ship sound 
        self.explosion_asteroid_sound = arcade.load_sound("game\sounds\explosion1.wav")
        

        # ASTEROID SPAWN PARAMETERS
        self.spawn_amount = 3
        self.spawn_interval = 100

        # WAIT PARAMETERS
        self.count = 0
        self.target = -1
        self.waiting = False

    def setup(self):
        self.background = arcade.load_texture(
            WORKING_DIRECTORY+"/game/images/stars.png")

        # creates a sprite list under name spritelist
        self.spritelist = arcade.SpriteList()
        self.explosionlist = arcade.SpriteList()
        self.asteroidlist = arcade.SpriteList()
        self.laserlist = arcade.SpriteList()

        self.ship = Ship()
        self.inputs = Inputs()
        # adds ship to sprite list /// THIS NEEDS TO BE THE FIRST ITEM ///
        self.spritelist.append(self.ship)

    # WAIT FUNCTION
    def wait_dur(self, duration):
        if self.waiting:
            if self.count <= 0:
                self.target = duration
                self.count += 1
            elif self.count >= self.target:
                self.waiting = False
                self.count = 0
                self.target = -1
            else: self.count += 1
        else: self.waiting = True

    def on_draw(self):
        arcade.start_render()
        # Draw background
        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Updates graphics for all sprites
        self.laserlist.draw()
        self.spritelist.draw()
        self.explosionlist.draw()
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
            self.spritelist[0].point_to(self.asteroidlist[0].get_pos(), self.asteroidlist[0].get_id())

    # Check for key release

    def on_key_release(self, symbol, modifier): self.inputs.released(
        symbol, modifier)

    def on_update(self, delta_time):
        for sprite in self.spritelist:
            if sprite.update() == True:
                arcade.play_sound(self.laser_sound)
                self.laserlist.append(
                    Laser(40, self.spritelist[0].get_target_angle()))

        self.asteroidlist.update()
        self.laserlist.update()
        self.explosionlist.update()

        # Update keyboard inputs
        self.inputs.update()

        # Check for collisions with the laser and the asteroids
        # Delete both if there is contact
        if (len(self.laserlist) > 0 and len(self.asteroidlist) > 0):
            if arcade.check_for_collision(self.asteroidlist[0], self.laserlist[0]):
                #expolode when hits asteroid with laser 
                arcade.play_sound(self.explosion_sound)
                self.laserlist.pop(0)
                self.asteroidlist.pop(0)
                self.tracker.addscore()

        # spawn_counter is used to spawn multiple asteroids with a 30 tick gap
        if len(self.asteroidlist) <= 0 and self.spawning == False:
            self.spawning = True
            self.spawn_counter = self.spawn_interval * self.spawn_amount
        if self.spawn_counter % self.spawn_interval == 0:
            self.asteroidlist.append(Astroid(2, self.data.random_word(self.tracker.getscore())))
        if self.spawn_counter >= 2:  self.spawn_counter -= 1
        if self.spawn_counter < 2: self.spawning = False


        if len(self.asteroidlist) > 0 and len(self.spritelist) > 0:
            if arcade.check_for_collision(self.asteroidlist[0], self.spritelist[0]):
                
                self.asteroidlist.pop(0)
                if self.tracker.gethp() > 1:
                    self.tracker.minushp()
                    arcade.play_sound(self.explosion_asteroid_sound)
                else:
                    self.tracker.minushp()
                    self.boom.center_y = self.ship.center_y
                    self.boom.center_x = self.ship.center_x
                    self.spritelist.append(self.boom)
                    arcade.play_sound(self.explosion_sound)
                    # Wait 1 seconds
                    #self.spritelist.pop(-1)

                    # wait 1 second
                    self.wait_dur(100)

        if self.waiting == True: self.wait_dur(100) # continue waiting
        else:
            if self.sig_gameover == True:
                self.gameover.gather(
                    str(self.tracker.getscore()), self.inputs, self.db)
                self.window.show_view(self.gameover)
                    
        for laser in self.laserlist:
            if laser.get_pos()[0] > SCREEN_WIDTH or laser.get_pos()[0] < 0:
                laser.remove_from_sprite_lists()
            if laser.get_pos()[1] > SCREEN_HEIGHT or laser.get_pos()[1] < 0:
                laser.remove_from_sprite_lists()