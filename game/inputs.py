from game.data import Data
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SHIP_SCALE,
    CENTER_X,
    CENTER_Y,
)

import arcade

class Inputs(arcade.Sprite):
    
    def __init__(self):
        super().__init__("game/images/spaceship.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.word_list = None
        self.data = Data()
        self.active_word = ""
        self.input = ""
        self.get_word()

    # \\\ GET WORD //
    # Sets the active word to a random word from the word list
    def get_word(self): 
        self.active_word = self.data.random_word()
        self.active_word = self.active_word[:-1]

    # \\\ DRAW ///
    # Displays the current status of the input string on the screen
    # Displays the active word to match TEST CODE
    def draw(self):
        # Display input string
        arcade.draw_text(
            self.input,
            CENTER_X - 200,
            CENTER_Y - 300,
            arcade.color.RED,
            25
            )
        # Display active word
        arcade.draw_text(
            self.active_word,
            CENTER_X + 320,
            CENTER_Y - 335,
            arcade.color.RED,
            25
            )

    # \\\ PRESSED ///
    # Checks for keyboard input and appends that character to the input string.
    # If enter is pressed and the input string is equal to active_word, then the
    # string is reset and a TRUE is returned.
    # Backspace deletes the last character from the input string.
    def pressed(self, symbol, modifier):
        # Check the symbol with the alphabet and add the appropriate char

        # UPPERCASE
        if modifier & arcade.key.MOD_SHIFT:
            if symbol == arcade.key.A: self.input = self.input + 'A'
            if symbol == arcade.key.B: self.input = self.input + 'B'
            if symbol == arcade.key.C: self.input = self.input + 'C'
            if symbol == arcade.key.D: self.input = self.input + 'D'
            if symbol == arcade.key.E: self.input = self.input + 'E'
            if symbol == arcade.key.F: self.input = self.input + 'F'
            if symbol == arcade.key.G: self.input = self.input + 'G'
            if symbol == arcade.key.H: self.input = self.input + 'H'
            if symbol == arcade.key.I: self.input = self.input + 'I'
            if symbol == arcade.key.J: self.input = self.input + 'J'
            if symbol == arcade.key.K: self.input = self.input + 'K'
            if symbol == arcade.key.L: self.input = self.input + 'L'
            if symbol == arcade.key.M: self.input = self.input + 'M'
            if symbol == arcade.key.N: self.input = self.input + 'N'
            if symbol == arcade.key.O: self.input = self.input + 'O'
            if symbol == arcade.key.P: self.input = self.input + 'P'
            if symbol == arcade.key.Q: self.input = self.input + 'Q'
            if symbol == arcade.key.R: self.input = self.input + 'R'
            if symbol == arcade.key.S: self.input = self.input + 'S'
            if symbol == arcade.key.T: self.input = self.input + 'T'
            if symbol == arcade.key.U: self.input = self.input + 'U'
            if symbol == arcade.key.V: self.input = self.input + 'V'
            if symbol == arcade.key.W: self.input = self.input + 'W'
            if symbol == arcade.key.X: self.input = self.input + 'X'
            if symbol == arcade.key.Y: self.input = self.input + 'Y'
            if symbol == arcade.key.Z: self.input = self.input + 'Z'

        # LOWERCASE
        else:
            if symbol == arcade.key.A: self.input = self.input + 'a'
            if symbol == arcade.key.B: self.input = self.input + 'b'
            if symbol == arcade.key.C: self.input = self.input + 'c'
            if symbol == arcade.key.D: self.input = self.input + 'd'
            if symbol == arcade.key.E: self.input = self.input + 'e'
            if symbol == arcade.key.F: self.input = self.input + 'f'
            if symbol == arcade.key.G: self.input = self.input + 'g'
            if symbol == arcade.key.H: self.input = self.input + 'h'
            if symbol == arcade.key.I: self.input = self.input + 'i'
            if symbol == arcade.key.J: self.input = self.input + 'j'
            if symbol == arcade.key.K: self.input = self.input + 'k'
            if symbol == arcade.key.L: self.input = self.input + 'l'
            if symbol == arcade.key.M: self.input = self.input + 'm'
            if symbol == arcade.key.N: self.input = self.input + 'n'
            if symbol == arcade.key.O: self.input = self.input + 'o'
            if symbol == arcade.key.P: self.input = self.input + 'p'
            if symbol == arcade.key.Q: self.input = self.input + 'q'
            if symbol == arcade.key.R: self.input = self.input + 'r'
            if symbol == arcade.key.S: self.input = self.input + 's'
            if symbol == arcade.key.T: self.input = self.input + 't'
            if symbol == arcade.key.U: self.input = self.input + 'u'
            if symbol == arcade.key.V: self.input = self.input + 'v'
            if symbol == arcade.key.W: self.input = self.input + 'w'
            if symbol == arcade.key.X: self.input = self.input + 'x'
            if symbol == arcade.key.Y: self.input = self.input + 'y'
            if symbol == arcade.key.Z: self.input = self.input + 'z'

        # On SPACE, append the space character to the input string
        if symbol == arcade.key.SPACE: self.input = self.input + ' '
        
        # If enter, check vs active_word
        # Clear input and get a new word if they match
        if symbol == arcade.key.ENTER:
            if self.active_word == self.input:
                self.input = ""
                self.get_word()

        # On backspace, delete the last character from input
        if symbol == arcade.key.BACKSPACE: self.input = self.input[:-1]