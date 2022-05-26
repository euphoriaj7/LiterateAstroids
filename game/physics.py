#   physics.py outline:
#
#   __init__ (x, y, deltaX, deltaY, rotation)
#
#   set_pos()       // Sets the (x,y) coordinate
#   set_velocity()  // Sets the velocity vector
#   set_rotation()  // Sets rotation of the object in radians
#
#   get_pos()       // Returns the (x,y) coordinate
#   get_velocity()  // Returns the velocity vector
#   get_rotation()  // Returns the angle of rotation in radians
#
#   point_to()      // Sets the rotation to have the front of the object face a particular coordinate
#   tick_update()   // Sets the (x,y) position to the position + the velocity vector

from game.constants import (
    CENTER_X,
    CENTER_Y,
)

import math
class Physics():

    def __init__(self, x, y, deltaX, deltaY, rotation):
        self.x = x
        self.y = y
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.rotation = rotation

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_velocity(self, deltaX, deltaY):
        self.deltaX = deltaX
        self.deltaY = deltaY

    def set_rotation(self, rotation): self.rotation = rotation

    def get_pos(self):      return (self.x, self.y)
    def get_velocity(self): return (self.deltaX, self.deltaY)
    def get_rotation(self): return (self.rotation)

    def point_to(self, x, y): self.rotation = math.atan2(y-CENTER_Y, x-CENTER_X) - math.pi/2

    def tick_update(self):
        self.x = self.x + self.deltaX
        self.y = self.y + self.deltaY