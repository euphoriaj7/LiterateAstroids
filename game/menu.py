import arcade
from game.constants import (SCREEN_WIDTH, SCREEN_HEIGHT, WORKING_DIRECTORY)
from game.director import Director

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.BEIGE)
        self.background = arcade.load_texture(WORKING_DIRECTORY+"\game\images\classmenu.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        director_view = Director()
        director_view.setup()
        self.window.show_view(director_view)
    