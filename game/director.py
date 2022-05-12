import arcade
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from game.actor import Actor

class Director(arcade.View):

    def __init__(self):
        super().__init__()

    def setup(self):
        self.background = arcade.load_texture('game\images\stars.png')
        self.spritelist = arcade.sprite_list()
        self.actor = Actor()
        self.spritelist.append(self.actor) # adds actor(all sprites) to sprite list
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.spritelist.draw() # adds all actors to screen
    
    def on_update(self):
        self.spritelist.update()
        #update actors
        #call check collisions
        #update health & score
    
