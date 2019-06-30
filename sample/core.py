#we import our global variables and the packages needed

import numpy as np
import random

import helpers as h 

#Let's create
def main ():
    

    print ('This is a game called Game')
    n_players = int(input('Welcome, please tell me the number of players :'))
    h.g.initialize(n_players)

    print ('There are ' + repr(h.g.n_countries) + ' countries')

    world ,year= h.start_game(n_players)
    
    while year < 5:
        print('It is the year ' + repr(year) + ' of this era')
        
        h.global_turn(world , year,n_players)
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@ Happy New Year! @@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('End of the game')
    
    
def summary(year,world):
    print('It is ',year, 'a. G.')
    print('This is the world we live in')
    print(world)
    return year,world,ranking


if __name__ == "__main__":
    main()