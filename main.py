from numpy import *
from molecule import *

# PROGRAM MAIN
def main(window, molecules, timeStep):
    for i in range(50000):  # run 1000 steps
        for m in range(len(molecules)):  # update each molecule in list

            molecules[m].step(timeStep)  # step molecule forward
            molecules[m].reflect(timeStep)  # reflect if conditions are met

            for n in range(m,len(molecules)):  
            	# check each other molecule for collision condition
            	if molecules[n].__ne__(molecules[m]) and math.sqrt((molecules[m].pos-molecules[n].pos).dot(molecules[m].pos-molecules[n].pos)) < 1:

            		# perform collision
            		collision = collide(molecules[m],molecules[n])
            		molecules[m].setVel(collision[0])
            		molecules[n].setVel(collision[1])
            		print("COLLISION") 

# set up sim
t = 0.05
window = GraphWin("FluidSim",100,100)  # create window
molecule_0 = Molecule(0, window, 1, np.array([0.0,0.0]), np.array([2.0,1.0]),"blue")
molecule_1 = Molecule(1, window, 2, np.array([50.0,0.0]), np.array([-1.5,2.0]), "red")
molecule_2 = Molecule(2, window, 5, np.array([25.0,0.0]), np.array([0,-1.0]), "green")
molecule_3 = Molecule(3, window, 0.1, np.array([12.0,0.0]), np.array([0,-2.0]), "black")
molecules = [molecule_0, molecule_1, molecule_2, molecule_3]  # molecules list

# run sim
main(window, molecules, t)