import arcade
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

    def setup(self):
        self.background = arcade.load_texture('game/images/stars.png')
        self.foreground = arcade.load_texture('game/images/shipshell.png')
        self.spritelist = arcade.SpriteList() # creates a sprite list under name spritelist
        self.ship = Ship()
        self.astroid = Astroid()

        self.spritelist.append(self.ship) # adds actor(all sprites) to sprite list
        self.spritelist.append(self.astroid)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.spritelist.draw() # adds all actors to screen
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.foreground)
        #place score and word box
    
    #def on_update(self):
        #self.spritelist.update() # updates all sprites
        #call check collisions
        #update health & score
    


#MOrgan 