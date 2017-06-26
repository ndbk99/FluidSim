from tkinter import *
from graphics import *
from vector_2d import *


# Fluid molecule class
class Molecule(object):

    # constructor - takes mass scalar, position and velocity (and accel) Vector objets
    def __init__(self, i, w, m, p, v, a=Vector(0,0)):
        self.index = i
        self.mass = m
        self.pos = p
        self.vel = v
        self.acc = a
        self.window = w
        self.circle = Circle(Point(self.pos.x, self.pos.y), 5)
        self.circle.draw(self.window)

    # step time forward by one increment
    def step(self, timeStep):
        
        self.circle.undraw()  # undraw old circle

        # double check this math / euler's method use esp re: updating velocity
        self.vel.x += self.acc.x * timeStep
        self.vel.y += self.acc.y * timeStep
        self.pos.x += self.vel.x * timeStep
        self.pos.y += self.vel.y * timeStep

        # draw new circle
        self.circle = Circle(Point(self.pos.x, self.pos.y), 5)
        self.circle.draw(self.window)

    # return index and position vector in formatted string
    def toString(self):
        return "%d : %s" % (self.index, self.pos.toString())

    # reflect molecule if it has hit a wall
    def check(self,t):
        top = 0
        bottom = 100
        left = 0
        right = 100
        if self.pos.x >= right:
            print("REFLECTED RIGHT", self.toString())
            self.vel.x *= -1
            self.step(t)
        if self.pos.x <= left:
            print("REFLECTED LEFT", self.toString())
            self.vel.x *= -1
            self.step(t)
        if self.pos.y <= top:
            print("REFLECTED TOP", self.toString())
            self.vel.y *= -1
            self.step(t)
        if self.pos.y >= bottom:
            print("REFLECTED BOTTOM", self.toString())
            self.vel.y *= -1
            self.step(t)
    

