import arcade
from game.constants import (
WORKING_DIRECTORY,
SCREEN_HEIGHT,
SCREEN_WIDTH
)
from game.tracker import Tracker

class GameOver(arcade.View):

    def __init__(self):
        super().__init__()
        self.tracker = Tracker
        
    def on_show(self):
        arcade.set_background_color(arcade.color.BEIGE)
        self.end = arcade.load_texture(WORKING_DIRECTORY+"\game\images\stars.png")
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.end)
        arcade.draw_text("Final Score: ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 45)