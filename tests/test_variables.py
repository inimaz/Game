# -*- coding: utf-8 -*-

"""
This is to be run in the command line with
pytest *nameOfFile*
"""
import sys
import helpers as h
import numpy as np

#We define the variables
current_player_id = 0            
n_players = 16

world = h.start_game(n_players)
world0 = np.array([[0,0,0],
                  [1,2,1],
                  [1,2,2]])


