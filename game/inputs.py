import arcade

class Inputs():
    
    def __init__(self):
        pass

    def on_key_pressed(self, input):
        if arcade.key.A: input = input + 'a'
        if arcade.key.B: input = input + 'b'
        if arcade.key.C: input = input + 'c'
        if arcade.key.D: input = input + 'd'
        if arcade.key.E: input = input + 'e'
        if arcade.key.F: input = input + 'f'
        if arcade.key.G: input = input + 'g'
        if arcade.key.H: input = input + 'h'
        if arcade.key.I: input = input + 'i'
        if arcade.key.J: input = input + 'j'
        if arcade.key.K: input = input + 'k'
        if arcade.key.L: input = input + 'l'
        if arcade.key.M: input = input + 'm'
        if arcade.key.N: input = input + 'n'
        if arcade.key.O: input = input + 'o'
        if arcade.key.P: input = input + 'p'
        if arcade.key.Q: input = input + 'q'
        if arcade.key.R: input = input + 'r'
        if arcade.key.S: input = input + 's'
        if arcade.key.T: input = input + 't'
        if arcade.key.U: input = input + 'u'
        if arcade.key.V: input = input + 'v'
        if arcade.key.W: input = input + 'w'
        if arcade.key.X: input = input + 'x'
        if arcade.key.Y: input = input + 'y'
        if arcade.key.Z: input = input + 'z'
        
        elif arcade.key.ENTER: return True
        else: return False