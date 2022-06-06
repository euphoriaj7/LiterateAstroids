import arcade
from game.constants import (
WORKING_DIRECTORY,
SCREEN_HEIGHT,
SCREEN_WIDTH
)

class GameOver(arcade.View):

    def __init__(self):
        super().__init__()
    
    def gather(self, score):
        self.fscore = score

    def on_show(self):
        arcade.set_background_color(arcade.color.BEIGE)
        self.end = arcade.load_texture(WORKING_DIRECTORY+"\game\images\stars.png")
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.end)

        arcade.draw_text("Literate Astroids", SCREEN_WIDTH / 3, SCREEN_HEIGHT - SCREEN_HEIGHT / 6, arcade.color.WHITE, 50)
        arcade.draw_text("Final Score: "+self.fscore, SCREEN_WIDTH / 13, SCREEN_HEIGHT - SCREEN_HEIGHT / 3, arcade.color.WHITE, 40)
        arcade.draw_text("High Scores", SCREEN_WIDTH / 13, SCREEN_HEIGHT / 2, arcade.color.WHITE, 40)
        
        
        arcade.draw_text("Add Name: "+"keyboard inputs", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 40)