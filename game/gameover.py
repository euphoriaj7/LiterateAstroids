import arcade
from game.constants import (
    WORKING_DIRECTORY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)

class GameOver(arcade.View):

    def __init__(self):
        super().__init__()
        self.words = ""

    def gather(self, score, inputs):
        self.fscore = score
        self.inputs = inputs

    def on_show(self):
        arcade.set_background_color(arcade.color.BEIGE)
        self.end = arcade.load_texture(
            WORKING_DIRECTORY+"/game/images/stars.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.end)

        arcade.draw_text("Literate Astroids", SCREEN_WIDTH / 3,
                         SCREEN_HEIGHT - SCREEN_HEIGHT / 6, arcade.color.WHITE, 50)
        arcade.draw_text("Final Score: "+self.fscore, SCREEN_WIDTH /
                         13, SCREEN_HEIGHT - SCREEN_HEIGHT / 3, arcade.color.WHITE, 40)
        arcade.draw_text("High Scores", SCREEN_WIDTH / 13,
                         SCREEN_HEIGHT / 2, arcade.color.WHITE, 40)
        arcade.draw_text("Add Name: "+ str(self.inputs.get_input()), SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 2, arcade.color.WHITE, 40)

    def on_key_press(self, symbol, modifer):
        
        self.inputs.pressed(symbol, modifer, '')
        if symbol == arcade.key.ENTER:
            update_database(self.inputs.get_input(), self.fscore)
            #update highscores list
            #stop player from doing more input?

    def on_key_release(self, symbol, modifier): self.inputs.released(
        symbol, modifier)
    
    def on_update(self, delta_time):
        self.inputs.update()

#           ||
#           ||
#          \  /
#           \/
    def update_database(name, score):
        #submit name and score) to firestore

