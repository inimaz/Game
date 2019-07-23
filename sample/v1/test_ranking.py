import helpers as h
import numpy as np

world = np.array([[0,0,0],
                  [1,2,1],
                  [1,2,1]])
#world[1] = (0,0,1)
#
#print(world)
A=h.ranking (world,3)
print(A)