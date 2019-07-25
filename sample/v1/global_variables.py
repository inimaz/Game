# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:18:50 2019

@author: iimazchacon
"""

#This file is to initialize all the globals
import numpy as np

n_players = 5
year = 0
human_playerid=0
year_max= 10
select_grid_0=[]

def initialize():
    
    global n_countries
    global conq_countries
    global world
    global size_world
    global select_grid_0
    global attack_mat
    global defense_mat
    
    n_countries= n_players**2
    conq_countries = np.zeros((n_players,1))
    conq_countries = conq_countries.astype(int)
    world = np.zeros((n_players,n_players))-1
    #We would like to have int, not float
    world = world.astype(int)
    size_world = np.shape(world)[1]
    select_grid_0 = np.zeros((n_players,n_players))
    attack_mat = np.ones((n_players,n_players))
    defense_mat = np.ones((n_players,n_players))

############# Drawing constants ############
    #####################################
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
# This sets the margin between each cell
MARGIN = 5

CHAT_HEIGHT = 5*HEIGHT
CHAT_WIDTH = (MARGIN + WIDTH) * n_players - MARGIN
 




RANKING_WIDTH=6*WIDTH
RANKING_HEIGHT= n_players * HEIGHT + (n_players-1)*MARGIN
RANKING_XPOS= n_players * WIDTH + (n_players-1)*MARGIN + 2*MARGIN
RANKING_YPOS= MARGIN
WINDOW_WIDTH = n_players * WIDTH + (n_players-1)*MARGIN + 4*MARGIN + RANKING_WIDTH
WINDOW_HEIGHT = n_players * HEIGHT + (n_players-1)*MARGIN + 3*MARGIN + CHAT_HEIGHT
WINDOW_SIZE = [WINDOW_WIDTH, WINDOW_HEIGHT]

NEXT_TURN_xpos= WINDOW_WIDTH-6*WIDTH
NEXT_TURN_ypos = WINDOW_HEIGHT-2*WIDTH
NEXT_TURN_HEIGHT= HEIGHT
NEXT_TURN_WIDTH = 5*WIDTH

ATTACK_xpos=NEXT_TURN_xpos
ATTACK_ypos = NEXT_TURN_ypos - WIDTH -2*MARGIN

START_xpos=WINDOW_WIDTH/2
START_ypos=WINDOW_HEIGHT/2
START_WIDTH = 25*MARGIN
START_HEIGHT = 10*MARGIN

color_matrix =[]
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
PURPLE = (102, 0, 102)
##############################################################################
#################################################################
##### This is used by the pygame interface to randomize colors


def calculate_colors (n_players):
    color_matrix = np.zeros((n_players,3))

    for row in range(0,n_players):
        color = list(np.random.choice(range(256), size=3))
        r=0
        while (color == color_matrix[r]).all():
            #This returns a random color
            color = list(np.random.choice(range(256), size=3))
            r+=1
        color_matrix[row]= color
        
    return color_matrix


def initialize_draw ():
    global color_matrix
    color_matrix=calculate_colors(n_players)
    
end_game=False