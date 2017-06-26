from tkinter import *
from math import *
from graphics import *

# 2D vector class
class Vector(object):

    # constructor - takes x and y components
    def __init__(self, x, y):
        self.set(x, y)
        # self.dot = oval(1,1,1,1)

    # component setter
    def set(self, xComp, yComp):
        self.x = xComp
        self.y = yComp
        # self.dot.x = 

    # calculate vector magnitude
    def mag(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    # return components in formatted string
    def toString(self):
        return "(%.5f,%.5f)" % (self.x, self.y)


# Fluid molecule class
class Molecule(object):

    # constructor - takes mass scalar, position and velocity (and accel) Vector objets
    def __init__(self, i, window, m, p, v, a=Vector(0,0)):
        self.index = i
        self.mass = m
        self.pos = p
        self.vel = v
        self.acc = a
        self.circle = Circle(Point(self.pos.x, self.pos.y), 5)
        self.circle.draw(window)

    # step time forward by one increment
    def step(self, timeStep):
        
        self.circle.undraw()  # undraw old circle

        # double check this math / euler's method use esp re: updating velocity
        self.vel.x += self.acc.x * timeStep
        self.vel.y += self.acc.y * timeStep
        self.pos.x += self.vel.x * timeStep
        self.pos.y += self.vel.y * timeStep

        self.circle = Circle(Point(self.pos.x, self.pos.y), 5)
        self.circle.draw(window)  # draw new circle

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
    


# PROGRAM MAIN
def main(window, molecules, timeStep):
    for i in range(1000):  # run 1000 steps
        for m in molecules:  # update each molecule in list
            m.step(timeStep)  # step molecule forward
            m.check(timeStep)  # check for reflections

# set up sim
t = 1
window = GraphWin("FluidSim",100,100)  # create window
molecule_1 = Molecule(0, window, 1, Vector(0,0), Vector(2,2))
molecule_2 = Molecule(1, window, 1, Vector(10,10), Vector(-1,0.5))
molecules = [molecule_1, molecule_2]  # molecules list


# run sim
main(window, molecules, t)

