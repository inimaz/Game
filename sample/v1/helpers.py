import numpy as np
import random
import logging
import global_variables as g
import helpers_draw as hd
import logging



   
#In here we are going to start our matrix world
def start_game(n_players):
    #world is going to be a nxn matrix
    
    #Now we say who is owning what. conq_countries will store the number of countries per player
    #conq_countries[0] will correspond to player0...
    g.initialize()
    g.initialize_draw()
    conq_countries = g.conq_countries
    world = g.world
    for k in range (0,n_players):
        i= rand_num()
        j= rand_num()
        while conq_countries[k] < n_players:
            while world[i,j] >=0:
                i= rand_num()
                j= rand_num()
            world[i,j] = k
            conq_countries[k] +=1
    return world



def global_turn(world,n_players,select_grid,event,text,computer_turn):
    if computer_turn:
        current_player_id = 1
        
        while current_player_id <= n_players-1:
#            hd.print_text('%%%%%%%%%%%%%%% NEXT Player %%%%%%%%%%%%%%% \nIt is the turn of Player ' + repr(current_player_id) + '.')
            world = individual_turn(world,current_player_id)
            #If someone has conquered the world, world size will be 0
            if world.size == 0:
                break
#            hd.print_text('This is the world today')
            current_player_id += 1
        
#        hd.print_text('It is the end of a wonderful year')
        computer_turn=False
    else:
        text,world,select_grid,computer_turn=human_turn(text,world,select_grid,event)
    return  text,world,select_grid,computer_turn       


def individual_turn(world,current_player_id):
    #First we check that the curent player has countries to atack from
    if current_player_id in count_countries(world)[0]:    
        my_turn = True

    else:
        my_turn = False
    #Now we start the turn
    while my_turn== True:
        x_origin= rand_num()
        y_origin= rand_num()
        defender_pos = search(world,current_player_id,x_origin,y_origin)
#        attacker_pos = (x_origin,y_origin)
        if defender_pos != -1:
            defender_id = world[defender_pos]
#            hd.print_text('Player ' + repr(current_player_id) +' attacks from country ' + repr(attacker_pos))
#            hd.print_text('The target country is ' + repr(defender_pos)+ '. It belongs to Player ' + repr(defender_id))
            if combat(current_player_id,defender_id):
                world[defender_pos]= current_player_id
#                hd.print_text('Player ' + repr(current_player_id) + ' has conquered ' + repr(defender_pos))
#                hd.print_text('This territory used to belong to Player ' + repr(defender_id))
                
            else:
#                hd.print_text('Player ' + repr(current_player_id) + ' has lost the battle and needs some rest.')   
#                hd.print_text('Now it`s next player`s turn')

                my_turn= False
        if count_countries(world)[1][0] == g.n_countries:
#            hd.print_text('Player ' + repr(current_player_id) + ' has conquered the world!')
            #We return an empty array to global_turn
            g.end_game=True
            break
            
    return world


def human_turn(text,world,select_grid,event):
    select_grid,text = hd.select_field(event,select_grid,world,text)
    computer_turn= hd.next_turn(event)
    if hd.attack(event):
        world,computer_turn,text,select_grid=human_combat(select_grid,world,text)
        logging.debug("Attacking...")
    

    
    
    return text,world,select_grid,computer_turn  


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
    
# Do a function to count the number of countries per player
def count_countries(x):
    a = np.unique(x,return_counts=True)
    #this returns a matrix in a[0] the numbers, in a[1] the count
    return a


    
def rand_num():
    N = g.size_world-1
    n = random.randint(0,N)
    return n

def ranking(world,n_players):
    N = count_countries(world)
    #N[0] is the player id whereas N[1] is the number of countries
    #To sort it from higher counts of countries to lower counts of countries
    count_sort_ind = np.argsort(-N[1])
    Players=N[0][count_sort_ind]
    Countries =N[1][count_sort_ind]
    
    n=N[0].size
    #And now we start printing the ranking
#    hd.print_text('This is the final ranking')

    Ranking=np.zeros((n_players,3))
    for i in range(0,n):
        player = Players[i]
        countries = Countries[i]
#Note that in python we start to count from 0. If we want to print Position 1, we have to do i+1
        Ranking[i]=([i+1,player,countries])
        
    #And now the latest thing, we attach the ones that did not survive
    for i in range(0,n_players):
        if i not in Players:
            #The last loop ended up in n. This one starts in n+1
            Ranking[n][:]=([n+1,i,0])
    Ranking=Ranking.astype(int)
    return Ranking
            
def human_combat(select_grid,world,text):
    n=0
    defenders=np.zeros((4,2))-1
    defenders=defenders.astype(int)
    computer_turn=False
    for row in range(g.n_players):
        for column in range(g.n_players):
#            if select_grid[row][column] == -1:
#                attacker_pos = (row,column)
            if select_grid[row][column] == 2:
                defenders [n]= (row,column)
                n+=1
    for i in range (n):
        defender_pos= tuple(defenders[i])
        if defender_pos !=(-1,-1):
            attacker = g.human_playerid
            logging.debug("Country "+ repr(defender_pos) + "is been attacked by player.")
            defender = world[defender_pos]
            if combat(attacker,defender) and world[defender_pos]!= attacker :
                world[defender_pos]= attacker
                logging.debug( 'Human player conquered ' + repr(defender_pos)+'. It used to belong to' + repr(defender))
            else:
                computer_turn=True
                select_grid = np.zeros((g.n_players,g.n_players))
                text= 'You were not able to conquer ' + repr(defender_pos)
                break
            
    return world,computer_turn,text,select_grid
            
            
            
            

