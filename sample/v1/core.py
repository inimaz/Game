
import pygame
#import pygame_textinput
import numpy as np
import helpers as h
import global_variables as g
import helpers_draw as hd

n_players = g.n_players
world = h.start_game(n_players)[0]
 
# Create a 2 dimensional array. It wil contain the selected positions
select_grid = np.zeros((n_players,n_players))
 
# Initialize pygame
pygame.init()


#hd.print_text ('There are ' + repr(g.n_countries) + ' countries')
#hd.print_text('Each player has '+ repr(g.n_players) + ' countries')
#print('This is the world we live in')

# Set the HEIGHT and WIDTH of the screen
# For the window size to be according to the width and height
# WINDOW_WIDTH =  n_players * WIDTH + Number of margins in between* MARGIN + 2*MARGIN(MARGIN left and right)

WINDOW_SIZE = g.WINDOW_SIZE
#WINDOW_SIZE = [555, 555]
screen = pygame.display.set_mode(WINDOW_SIZE)
# Set title of screen
pygame.display.set_caption("The Game")
 
# Loop until the user clicks the close button.
done = False
end_game=False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
text="Welcome to a Game called The Game. \nLet's have fun with this game.\nConquer all countries to win!"

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
#        If we want to select one field 
        text,select_grid,computer_turn=h.human_turn(world,select_grid,event,text)               
#    end_game =h.main_loop(n_players,world,end_game)
    Ranking=h.ranking(world,n_players)
    #All CODE TO DRAW SHOULD GO BELOW THIS LINE
    # Set the screen background
    screen.fill(g.BLACK)
 
    # Draw the grid
    hd.draw_world(world,select_grid,end_game,Ranking)
#
    hd.print_text(text,False)
    hd.display_ranking(Ranking)
    hd.next_turn_button()    
    hd.attack_button()
    #All CODE TO DRAW SHOULD GO ABOVE THIS LINE 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()