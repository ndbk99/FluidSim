from tkinter import *
from graphics import *
import numpy as np
from math import *


# Fluid molecule class
class Molecule(object):

    # constructor - takes mass scalar, position and velocity (and accel) Vector objets
    def __init__(self, i, w, m, p, v, c="black",a=np.array([0,0])):

        self.index = i
        self.mass = m
        self.pos = p
        self.vel = v
        self.color = c
        self.acc = a
        self.window = w
        self.circle = Circle(Point(self.pos[0], self.pos[1]), 5)
        self.circle.draw(self.window)

    # step time forward by one increment
    def step(self, timeStep):
        
        self.circle.undraw()  # undraw old circle
        # euler's method to update position and velocity
        self.vel += self.acc*timeStep
        self.pos += self.vel*timeStep
        # draw new circle at new position
        self.circle = Circle(Point(self.pos[0], self.pos[1]), 5)
        self.circle.setOutline(self.color)
        if self.window.isOpen():
            self.circle.draw(self.window)
        print(self.index, self.pos)

    def setVel(self,velocity):
        self.vel = velocity

    # return index and position vector in formatted string
    def toString(self):

        return "%d : %s" % (self.index, self.pos)

    # reflect molecule if it has hit a wall
    def reflect(self,t):

        top = 0
        bottom = self.window.height
        left = 0
        right = self.window.width

        if self.pos[0] >= right:
            # print("REFLECTED RIGHT", self.toString())
            self.vel[0] *= -1
            self.step(t)
        if self.pos[0] <= left:
            # print("REFLECTED LEFT", self.toString())
            self.vel[0] *= -1
            self.step(t)
        if self.pos[1] <= top:
            # print("REFLECTED TOP", self.toString())
            self.vel[1] *= -1
            self.step(t)
        if self.pos[1] >= bottom:
            # print("REFLECTED BOTTOM", self.toString())
            self.vel[1] *= -1
            self.step(t)

# collision interaction between 2 molecules satisfying conservation of momentum and kinetic energy (could modify the KE part to produce inelastic collisions)
def collide(mol1,mol2):

    # set mass and initial velocity variables
    m = mol1.mass
    n = mol2.mass
    aX = mol1.vel[0]
    bX = mol2.vel[0]
    aY = mol1.vel[1]
    bY = mol2.vel[1]

    # calculate final velocities
    cX = (aX*m - aX*n + 2*bX*n) / (m+n)
    cY = (aY*m - aY*n + 2*bY*n) / (m+n)
    dX = (2*aX*m - bX*m + bX*n) / (m+n)
    dY = (2*aY*m - bY*m + bY*n) / (m+n)

    # calculate and print final velocities
    final_mvel = np.array([cX,cY])
    final_nvel = np.array([dX,dY])
    # print(np.array([aX,aY]), np.array([bX,bY]))
    # print(final_mvel, final_nvel)

    # return final velocities
    return final_mvel, final_nvel
