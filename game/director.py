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
        self.astroidlist = None

    def setup(self):
        self.background = arcade.load_texture('game/images/stars.png')
        #self.forebackground = arcade.load_texture('game\images\shipshell.png')
        self.astroidlist = arcade.sprite_list() # creates a sprite list under name astroidlist
        self.ship = Ship()
        self.astroidlist.append(self.ship) # adds actor(all sprites) to sprite list
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.forebackground)
        self.astroidlist.draw() # adds all actors to screen
        #arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        #place score and word box
    
    #def on_update(self):
        self.astroidlist.update() # updates all actor sprites
        #call check collisions
        #update health & score
    


#MOrgan