import numpy as np
import random
import global_variables as g

def rand_num():
    N = g.size_world-1
    n = random.randint(0,N)
    return n

#In here we are going to start our matrix world
def start_game(n_players):
    #world is going to be a nxn matrix
    
    #Now we say who is owning what. conq_countries will store the number of countries per player
    #conq_countries[0] will correspond to player0...
    
#    conq_countries = np.zeros((n_players,1))
#    world = np.zeros((n_players,n_players))-1
    conq_countries = g.conq_countries
    world = g.world
    year = g.year
    for k in range (0,n_players):
        i= rand_num()
        j= rand_num()
        while conq_countries[k] < n_players:
            while world[i,j] >=0:
                i= rand_num()
                j= rand_num()
            world[i,j] = k
            conq_countries[k] +=1
    print('These are the countries per player')
    print(conq_countries)
    print('This is the world we live in')
    print(world)
    return world,year



def individual_turn(world,current_player_id):
    my_turn = True
    while my_turn== True:
        x_origin= rand_num()
        y_origin= rand_num()
        defender_pos = search(world,current_player_id,x_origin,y_origin)
        attacker_pos = (x_origin,y_origin)
        if defender_pos != -1:
            defender_id = world[defender_pos]
            print('Player ' + repr(current_player_id) +' attacks from country ' + repr(attacker_pos))
            print('The target country is ' + repr(defender_pos)+ '. It belongs to Player' + repr(defender_id))
            if combat(current_player_id,defender_id):
                world[defender_pos]= current_player_id
                print('Player ' + repr(current_player_id) + ' has conquered ' + repr(defender_pos))
                print('This territory used to belong to Player ' + repr(defender_id))
            else:
                print('Player ' + repr(current_player_id) + ' has lost the battle and needs some rest.')   
                print('Now it`s next player`s turn')
                print('%%%%%%%%%% NEXT Player %%%%%%%%%%%%%%%')
                my_turn= False
#+ ' attacks from country ' + repr(attacker_pos) ' to '+
    return world


def global_turn(world,year,n_players):
    current_player_id = 0
    while current_player_id <= n_players-1:
        print('It is the turn of Player ' + repr(current_player_id))
        world = individual_turn(world,current_player_id)
        print('This is the world today')
        print (world)
        current_player_id += 1
    year += 1         



def search(world,current_player_id,i,j):
          
    if world[i,j]== current_player_id:
         ###########
       #If you need to log i and j uncomment this
#        print('This is i: ' + repr(i))
#        print('This is j: ' + repr(j))
       #############
        
        #Check the 4 neighbour countries and combat them
        #2 conditions
        #First to ensure that the i or j are not out of the matrix.
        # they should be smaller than the size of the matrix -1, since python
        # starts counting on 0

         #Right 
        if j <  (g.size_world-1) and world [i,j+1] != current_player_id:                
            defender_pos = (i,j+1)
        #Left    
        elif j > 0 and world [i,j-1] != current_player_id:                
            defender_pos = (i,j-1)
        #Top    
        elif i <  (g.size_world-1) and world [i+1,j] != current_player_id:                
            defender_pos = (i+1,j)
        #Bottom   
        elif i> 0 and world [i-1,j] != current_player_id:                
            defender_pos = (i-1,j)
        #If none of the neighbouts are attackable, then 
        else :
            defender_pos = -1
    else:
        defender_pos =-1
    return defender_pos
        
                

def combat(atacker,defender):
    attack = random.random()
    defense = random.random()
    if attack > defense:
        return True
    else:
        return False
    
# Do a function to count the number of countries per player. Maybe import counter?
#def count_countries(world):
#    for i in player_id:
#        