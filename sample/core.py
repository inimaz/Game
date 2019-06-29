#we import our global variables and the packages needed

import numpy as np
import pandas as pd
import random

import global_variables as g

import helpers as h 

#Let's create
def main ():
    

    print ('This is a game called Game')
    n_players = int(input('Welcome, please tell me the number of players :'))
    g.initialize(n_players)

    print('There are',g.n_countries,'countries')

    world ,year= h.start_game(n_players)
    
    h.global_turn(world , year)
       
    
    
    
def summary(year,world):
    print('It is ',year, 'a. G.')
    print('This is the world we live in')
    print(world)
    return year,world,ranking


if __name__ == "__main__":
    main()