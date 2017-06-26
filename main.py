from vector_2d import *
from molecule import *

# PROGRAM MAIN
def main(window, molecules, timeStep):
    for i in range(100):  # run 1000 steps
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

