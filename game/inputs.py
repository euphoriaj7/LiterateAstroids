# from tkinter.font import Font
from game.data import Data
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SHIP_SCALE,
    CENTER_X,
    CENTER_Y,
    FONT
)

import arcade

class Inputs(arcade.Sprite):
    
    def __init__(self):
        super().__init__(None, SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.input = ""
        self.is_backspace = False
        self.backspace_counter = 0

    def get_input(self):
        return self.input
    # \\\ DRAW ///
    # Displays the current status of the input string on the screen
    # Displays the active word to match TEST CODE
    def draw(self, score):
        # Display input string
        arcade.draw_text(
            self.input,
            CENTER_X - 200,
            CENTER_Y - 300,
            arcade.color.GREEN,
            30, font_name=(FONT,))
        # Display active word
        arcade.draw_text(
            score,
            CENTER_X + 320,
            CENTER_Y - 335,
            arcade.color.GREEN,
            30, font_name=(FONT,))
    
    # \\\ Update ///
    # Watches for signals related to "held down" keys and performs related code
    # on the clock update
    def update(self):
        if len(self.input) <= 0:    self.is_backspace = False       # If the word is empty, stop deleting characters
        if self.is_backspace:       self.backspace_counter += 1     # While backspae is held down, increment backspace_counter
        
        # This uses a modulo to backspace every nth clock cycle. The value of the nth comes from two different speeds (CURRENTLY 3rd and 5th)
        if (self.backspace_counter < 10):   # Use a slower speed for the first 2 loops of the modulo
            if self.backspace_counter % 5 >= 4: self.input = self.input[:-1]    # Backspace every 5th cycle (starting from the first of the loop)
        else:
            if self.backspace_counter % 3 >= 2: self.input = self.input[:-1]    # Backspace every 3rd cycle (starting from the first of the loop)

    # \\\ PRESSED ///
    # Watches for all keyboard inputs and performs actions based on their value
    def pressed(self, symbol, modifier, active_word):
        # For each key input in the alphabet, that appropriate character will
        # append to the input string. If shift is held down, letters will#
        # append as capital letters.
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
            if active_word == self.input and active_word != "":
                self.input = ""
                return True

        # Signal the update function to start deleting characters
        if symbol == arcade.key.BACKSPACE: self.is_backspace = True

        return False
    
    # \\\ RELEASED ///
    # Watches for all keyboard releases and performs actions based on their value
    def released(self, symbol, modifier):
        # On BACKSPACE             
        if symbol == arcade.key.BACKSPACE:
            self.backspace_counter = 0  # Reset the backspace_counter
            self.is_backspace = False   # Signal the update function to stop deleting characters