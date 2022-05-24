import arcade

class Inputs():
    
    def __init__(self):
        self.word_list = None
        self.active_word = "test"
        self.input = ""

    # \\\ PRESSED ///
    # Checks for keyboard input and appends that character to the input string.
    # If enter is pressed and the input string is equal to active_word, then the
    # string is reset and a TRUE is returned.
    # Backspace deletes the last character from the input string.
    def pressed(self, symbol, modifier):
        # Check the symbol with the alphabet and add the appropriate char
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
        if symbol == arcade.key.SPACE: self.input = self.input + ' '
        
        # If enter, check vs active_word
        # Clear input and return true if they match
        if symbol == arcade.key.ENTER:
            if (self.active_word == self.input):
                self.input = ""
                print (self.input)  # TESTING LINE
                return True
        # On backspace, delete the last character from input
        if symbol == arcade.key.BACKSPACE: self.input = self.input[:-1]

        print (self.input)  # TESTING LINE
        return False