from numpy import *
from molecule import *
from random import *

# PROGRAM MAIN
def main(window, molecules, timeStep):
    for i in range(500):  # run steps
        for m in range(len(molecules)):  # update each molecule in list
            molecules[m].step(timeStep)  # step molecule forward
            molecules[m].reflect(timeStep)  # reflect if conditions are met
            for n in range(m,len(molecules)):  
            	# check each other molecule for collision condition
            	if molecules[n].__ne__(molecules[m]) and math.sqrt((molecules[m].pos-molecules[n].pos).dot(molecules[m].pos-molecules[n].pos)) < 10:
            		# perform collision
            		collision = collide(molecules[m],molecules[n])
            		molecules[m].setVel(collision[0])
            		molecules[n].setVel(collision[1])
            		print("COLLISION") 
            		molecules[m].step(timeStep)
            		molecules[n].step(timeStep)

## ADD MECHANISM TO ENSURE PARTICLES DON'T OVERLAP
# also why are the molecules disappearing below the ground eventually when i turn on acceleration?
def random_molecules(n,window,velRange,massRange):
	array = []
	for i in range(n):
		pos = np.array([random() * window.width, random() * window.height])
		vel = np.array([(random()-1/2)*2 * velRange, (random()-1/2)*2 * velRange])
		mass = random()*massRange
		molecule = Molecule(i,window,mass,pos,vel,"black") # ,np.array([0,0.5]))
		array.append(molecule)
	return array

def chosen_molecules():
	molecule_0 = Molecule(0, window, 1, np.array([0.0,0.0]), np.array([2.0,1.0]),"blue",np.array([0.0,0.5]))
	molecule_1 = Molecule(1, window, 2, np.array([190.0,0.0]), np.array([-1.5,2.0]), "red",np.array([0.0,0.5]))
	molecule_2 = Molecule(2, window, 5, np.array([125.0,0.0]), np.array([-1.0,-1.0]), "green",np.array([0.0,0.5]))
	molecule_3 = Molecule(3, window, 0.1, np.array([100.0,0.0]), np.array([0,-1.5]), "black",np.array([0.0,0.5]))
	return molecule_0, molecule_1, molecule_2, molecule_3  # molecules list

# set up sim
t = 0.5
window = GraphWin("FluidSim",200,200)  # create window
molecules = random_molecules(20,window,2,10)

# run sim
main(window, molecules, t)