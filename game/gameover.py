import arcade
from game.constants import (
    WORKING_DIRECTORY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    FONT
)

class GameOver(arcade.View):

    def __init__(self):
        super().__init__()
        self.words = ""
        self.enter_name = True
        self.db = None
        self.fscore = None
        self.result = ""


    def gather(self, score, inputs, db):
        """
        Gather information for scores and scoreboard
        """

        #assign score to member variable for display and add to database
        self.fscore = score

        #assign user's name to member variable for display and add to database
        self.inputs = inputs

        #assign database to variable
        self.db = db

        #Connect to database
        self.db.initialize_firestore()

        #get the top five scores from the database
        self.highscores = self.db.get_top_five()
        
        
        
    def on_show(self):
        arcade.set_background_color(arcade.color.BEIGE)
        self.end = arcade.load_texture(
            WORKING_DIRECTORY+"/game/images/stars.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.end)

        arcade.draw_text("Literate Astroids", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - SCREEN_HEIGHT / 6, arcade.color.WHITE, 50, anchor_x="center", font_name=(FONT,))
        # User Score and Name Entry
        arcade.draw_text("Final Score: "+ str(self.fscore), SCREEN_WIDTH /
                         2, SCREEN_HEIGHT - SCREEN_HEIGHT / 3, arcade.color.WHITE, 40, anchor_x="center", font_name=(FONT,))
        arcade.draw_text("Enter your Name", SCREEN_WIDTH - SCREEN_WIDTH / 4,
                    SCREEN_HEIGHT / 2, arcade.color.WHITE, 40, anchor_x="center", font_name=(FONT,))
        arcade.draw_text("-> " + str(self.inputs.get_input()), SCREEN_WIDTH / 1.8,
                    SCREEN_HEIGHT / 2 - 50, arcade.color.WHITE, 40, font_name=(FONT,))
        arcade.draw_text(self.result, SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 4, arcade.color.WHITE, 40, font_name=(FONT,))
        # Top Scores
        arcade.draw_text("High Scores", SCREEN_WIDTH / 4,
                         SCREEN_HEIGHT / 2, arcade.color.WHITE, 40, anchor_x="center", font_name=(FONT,))
        arcade.draw_text(self.highscores["name1"]+": "+str(self.highscores["score1"]), SCREEN_WIDTH / 4,
                         SCREEN_HEIGHT / 2 - 50, arcade.color.WHITE, 40, anchor_x="center", font_name=(FONT,))
        arcade.draw_text(self.highscores["name2"]+": "+str(self.highscores["score2"]), SCREEN_WIDTH / 4,
                         SCREEN_HEIGHT / 2 - 50 * 2, arcade.color.WHITE, 40, anchor_x="center", font_name=(FONT,))
        arcade.draw_text(self.highscores["name3"]+": "+str(self.highscores["score3"]), SCREEN_WIDTH / 4,
                         SCREEN_HEIGHT / 2 - 50 * 3, arcade.color.WHITE, 40, anchor_x="center", font_name=(FONT,))
        arcade.draw_text(self.highscores["name4"]+": "+str(self.highscores["score4"]), SCREEN_WIDTH / 4,
                         SCREEN_HEIGHT / 2 - 50 * 4, arcade.color.WHITE, 40, anchor_x="center", font_name=(FONT,))
        arcade.draw_text(self.highscores["name5"]+": "+str(self.highscores["score5"]), SCREEN_WIDTH / 4,
                         SCREEN_HEIGHT / 2 - 50 * 5, arcade.color.WHITE, 40, anchor_x="center", font_name=(FONT,))
        
    
    
    def on_key_press(self, symbol, modifer):
        if self.enter_name == True:
            self.inputs.pressed(symbol, modifer, '')
            if symbol == arcade.key.ENTER:
                self.result = str(self.db.add_new_score(self.inputs.get_input(), self.fscore))
                #stop player from doing more input?   
                self.enter_name = False
                self.highscores = self.db.get_top_five()
                

    def on_key_release(self, symbol, modifier): self.inputs.released(
        symbol, modifier)
    
    def on_update(self, delta_time):
        self.inputs.update()
