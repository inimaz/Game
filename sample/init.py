#we import our global variables and the packages needed
import globals, config

#Let's create
def main ():
    
    print ('This is a game called Game')
    n_players = int(input('Welcome, please tell me the number of players :'))
    n_countries = n_players**2
    print('There are',n_countries,'countries')
    
    start_game(n_players)
    #We update the globals
#        globals.n_players = n_players
#        globals.n_countries = n_countries
#        
    
    
    
#In here we are going to start our matrix world
def start_game(n_players):
    #world is going to be a nxn matrix
    world = np.ones((n_players,n_players))
    print('This is the world we live in')
    return world

def combat():
    return

if __name__ == "__main__":
    main()