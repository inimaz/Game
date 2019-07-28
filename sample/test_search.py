# -*- coding: utf-8 -*-

"""
This is to be run in the command line with
pytest *nameOfFile*

To run all
python -m pytest
or
py.test

if you would like to see details, use -v (verbose)

"""
import sys,os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
print (myPath)
import helpers as h
import numpy as np

#We define the variables
current_player_id = 0            
n_players = 3
h.g.initialize(n_players)
world = np.array([[0,0,0],
                  [1,2,1],
                  [1,2,2]])


def test_rand_num():
   assert h.rand_num() < 3
        
def test_search():
        assert h.search(world,current_player_id,2,2) == -1
        assert h.search(world,current_player_id,0,2) == (1,2)        