from math import *

# 2D vector class
class Vector(object):

    # constructor - takes x and y components
    def __init__(self, x, y):
        self.set(x, y)

    # component setter
    def set(self, xComp, yComp):
        self.x = xComp
        self.y = yComp

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    # calculate vector magnitude
    def mag(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    # return components in formatted string
    def toString(self):
        return "(%.5f,%.5f)" % (self.x, self.y)
