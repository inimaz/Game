#we import our global variables and the packages needed
import helpers as h 

#Let's create
def main ():
    
    
    print ('This is a game called Game')
    n_players = int(input('Welcome, please tell me the number of players :'))
    year_max= 10

    world ,year= h.start_game(n_players)
    
    while year < year_max:
        print('It is the year ' + repr(year) + ' of this era')
        
        world = h.global_turn(world , n_players)
        if world.size == 0:
            break
        
        h.pause()
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@ Happy New Year! @@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        year += 1
    if year == year_max:
        h.ranking(world,n_players)
    
    print('')
    print('End of the game')
    


if __name__ == "__main__":
    main()