import arcade
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE
)

class Director(arcade.View):

    def __init__(self):
        super().__init__()

    def setup(self):
        self.background = arcade.load_texture('game\images\stars.png')
    
    def on_draw(self):
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
