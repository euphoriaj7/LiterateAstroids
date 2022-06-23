import arcade
from game.constants import (
    WORKING_DIRECTORY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    # FONT
)

class GameOver(arcade.View):

    def __init__(self):
        super().__init__()
        self.words = ""
        self.enter_name = True
        self.db = None
        self.fscore = None
        self.result = ""
        self.FONT = "Kenny Pixel"

    def gather(self, score, inputs, db):
        self.fscore = score
        self.inputs = inputs
        self.db = db
        self.db.initialize_firestore()
        
    def on_show(self):
        arcade.set_background_color(arcade.color.BEIGE)
        self.end = arcade.load_texture(
            WORKING_DIRECTORY+"/game/images/stars.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.end)

        arcade.draw_text("Literate Astroids", SCREEN_WIDTH / 3,
                         SCREEN_HEIGHT - SCREEN_HEIGHT / 6, arcade.color.WHITE, 50, font_name="Kenny Pixel")
        arcade.draw_text("Final Score: "+ str(self.fscore), SCREEN_WIDTH /
                         2, SCREEN_HEIGHT - SCREEN_HEIGHT / 3, arcade.color.WHITE, 40, font_name="Kenny Pixel")
        arcade.draw_text("High Scores", SCREEN_WIDTH / 13,
                         SCREEN_HEIGHT - SCREEN_HEIGHT / 3, arcade.color.WHITE, 40, font_name="Kenny Pixel")
        arcade.draw_text("Add Name: "+ str(self.inputs.get_input()), SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 2, arcade.color.WHITE, 40, font_name="Kenny Pixel")
        arcade.draw_text(self.result, SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 4, arcade.color.WHITE, 40, font_name="Kenny Pixel")
    
    
        
    def on_key_press(self, symbol, modifer):
        if self.enter_name == True:
            self.inputs.pressed(symbol, modifer, '')
            if symbol == arcade.key.ENTER:
                self.result = str(self.db.add_new_score(self.inputs.get_input(), self.fscore))
                #stop player from doing more input?   
                self.enter_name = False
                


    def on_key_release(self, symbol, modifier): self.inputs.released(
        symbol, modifier)
    
    def on_update(self, delta_time):
        self.inputs.update()
