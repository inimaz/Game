
import pygame
import numpy as np
import helpers as h
import constants
import helpers_draw as hd

n_players = 10

world = h.start_game(n_players)[0]
color_matrix= h.calculate_colors(n_players)

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

CHAT_HEIGHT = 5*HEIGHT
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. It wil contain the selected positions
select_grid = np.zeros((n_players,n_players))
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
# For the window size to be according to the width and height
# WINDOW_WIDTH =  n_players * WIDTH + Number of margins in between* MARGIN + 2*MARGIN(MARGIN left and right)
WINDOW_WIDTH = n_players * WIDTH + (n_players-1)*MARGIN + 2*MARGIN
WINDOW_HEIGHT = n_players * HEIGHT + (n_players-1)*MARGIN + 3*MARGIN + CHAT_HEIGHT
WINDOW_SIZE = [WINDOW_WIDTH, WINDOW_HEIGHT]
#WINDOW_SIZE = [555, 555]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("The Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


text = "Welcome to a Game called The Game. \nLet's have fun with this game.\nConquer all countries to win!"
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
#        If we want to select one field 
        select_grid = hd.select_field(event,select_grid)            
                

 
    # Set the screen background
    screen.fill(constants.BLACK)
 
    # Draw the grid
    for row in range(n_players):
        for column in range(n_players):
            color = constants.WHITE
            if select_grid[row][column] == -1:
                color_margin = constants.GREEN
                pygame.draw.rect(screen,
                             color_margin,
                             [(MARGIN + WIDTH) * column + 2/3 * MARGIN,
                              (MARGIN + HEIGHT) * row + 2/3 * MARGIN,
                              WIDTH + 2/3 * MARGIN,
                              HEIGHT + 2/3 * MARGIN])
            elif select_grid[row][column] == 1:
                color_margin = constants.BLUE
                pygame.draw.rect(screen,
                             color_margin,
                             [(MARGIN + WIDTH) * column + 2/3 * MARGIN,
                              (MARGIN + HEIGHT) * row + 2/3 * MARGIN,
                              WIDTH + 2/3 * MARGIN,
                              HEIGHT + 2/3 * MARGIN])
            pygame.draw.rect(screen,
                             color_matrix [world[row][column]],
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    hd.print_text(text,screen)         
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()