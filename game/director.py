import arcade
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
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

    def setup(self):
        self.background = arcade.load_texture(WORKING_DIRECTORY+"\game\images\stars.png")
        self.foreground = arcade.load_texture(WORKING_DIRECTORY+"\game\images\shipshell.png")
        
        self.spritelist = arcade.SpriteList() # creates a sprite list under name spritelist
        self.asteroidlist = arcade.SpriteList()
        self.laserlist = arcade.SpriteList()
        
        self.ship = Ship()
        self.inputs = Inputs()
        self.spritelist.append(self.ship) # adds ship to sprite list /// THIS NEEDS TO BE THE FIRST ITEM ///
        self.asteroidlist.append(Astroid(2)) # spawn in the first asteroid
        
    def on_draw(self):
        arcade.start_render()
        # Draw background
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Updates graphics for all sprites
        self.laserlist.draw()
        self.spritelist.draw()
        self.asteroidlist.draw()

        # Draw foreground
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.foreground)

        # Update text on screen
        self.inputs.draw()

    # Check for key press and for is_match signal
    # Spawns new asteroid with new word if there is a match
    # Spawns a new laser pointed at the first asteroid in the list
    def on_key_press(self, symbol, modifer):
        # Waches for the "word matched" signal from the inputs object
        if self.inputs.pressed(symbol, modifer):
            self.asteroidlist.append(Astroid(2))
            self.spritelist[0].point_to(self.asteroidlist[0].get_pos())
            self.laserlist.append(Laser(40, self.spritelist[0].angle))
            
    # Check for key release
    def on_key_release(self, symbol, modifier): self.inputs.released(symbol, modifier)
    
    def on_update(self, delta_time):
        self.spritelist.update() # updates all sprites
        self.asteroidlist.update()
        self.laserlist.update()

        # Update keyboard inputs
        self.inputs.update()

        # Check for collisions with the laser and the asteroids
        # Delete both if there is contact
        if (len(self.laserlist) > 0):
            if arcade.check_for_collision(self.asteroidlist[0], self.laserlist[0]):
                self.laserlist.pop(0)
                self.asteroidlist.pop(0)