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
        super().__init__(WORKING_DIRECTORY+"\game\images\spaceship.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.max_speed = 10
        self.target_angle = 0
        self.spin_direction = 0

    def get_target_angle(self): return self.target_angle

    # \\\ POINT TO ///
    # Points the ship towards the passed coordinates
    def point_to(self, pos):
        self.target_angle = ((math.atan2(pos[1] - CENTER_Y, pos[0] - CENTER_X) - math.pi/2) * 180/math.pi)
        if self.target_angle < -180:    self.target_angle += 360
        if self.target_angle > 180:     self.target_angle -= 360

        diff_angle = self.target_angle - self.angle
        if diff_angle > 0:  self.spin_direction = 1 
        else:               self.spin_direction = -1

        if abs(diff_angle) > 180: self.spin_direction *= -1

    def update(self):
        super().update()

        if self.angle > 180:    self.angle -= 360
        if self.angle < -180:   self.angle += 360

        if abs(self.target_angle - self.angle) < abs(self.change_angle):
            self.change_angle = 0
            self.spin_direction = 0
            self.angle = self.target_angle
            return True
        elif abs(self.change_angle) < self.max_speed: self.change_angle += .5 * self.spin_direction

        return False