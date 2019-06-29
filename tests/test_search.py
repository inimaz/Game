# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:35:55 2019

@author: iimazchacon
"""
from context import sample
from sample import global_variables as g
from sample import helpers as h
import numpy as np
import unittest

#We define the variables
current_player_id = 0            
n_players = 3
g.initialize(n_players)
world = np.array([[0,0,0],
                  [1,2,1],
                  [1,2,2]])


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

#    def test_startgame(self):
#        world,year=h.start_game(4)
    def test_rand_num(self):
        self.assertLessEqual(h.rand_num(),2)
        
    def test_search(self):
        self.assertEqual(h.search(world,current_player_id,2,2),-1)
        self.assertEqual(h.search(world,current_player_id,0,2),(1,2))
        
if __name__ == '__main__':
    unittest.main()