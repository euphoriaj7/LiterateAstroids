# fucnitons
# - score/points
import arcade
import math
from game.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    CENTER_X,
    CENTER_Y,
    SHIP_SCALE,
    WORKING_DIRECTORY,
)


class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__(WORKING_DIRECTORY+"/game/images/spaceship.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2

        self.rotation_time = 10
        self.rotation_tick = self.rotation_time+2

        self.start_angle = 0
        self.target_angle = 0
        self.delta_angle = 0

    def get_target_angle(self): return self.target_angle

    def point_to(self, pos):
        self.start_angle = self.angle
        self.target_angle = (
            (math.atan2(pos[1] - CENTER_Y, pos[0] - CENTER_X) - math.pi/2) * 180/math.pi)

        if self.target_angle > 180:
            self.target_angle -= 360
        if self.target_angle < -180:
            self.target_angle += 360

        self.delta_angle = self.target_angle - self.start_angle
        self.rotation_tick = 0

        if self.delta_angle > 180:
            self.delta_angle -= 360
        if self.delta_angle < -180:
            self.delta_angle += 360

    def update(self):
        super().update()

        if self.rotation_tick <= self.rotation_time:
            self.rotation_tick += 1
            self.angle = (self.start_angle + ((self.delta_angle/2) * math.sin(
                ((math.pi/self.rotation_time)*self.rotation_tick)-(math.pi/2))) + (self.delta_angle/2))

        if self.rotation_tick == self.rotation_time+1:
            self.rotation_tick += 1
            self.angle = self.target_angle
            return True

        return False
