
import pygame
import numpy as np
import helpers as h

n_players = 10

world = h.start_game(n_players)[0]
color_matrix= h.calculate_colors(n_players)
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
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
WINDOW_HEIGHT = n_players * HEIGHT + (n_players-1)*MARGIN + 2*MARGIN
WINDOW_SIZE = [WINDOW_WIDTH, WINDOW_HEIGHT]
#WINDOW_SIZE = [555, 555]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("The Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            #We set the limits so that if we click on borthers, the max value is the last row
            if row  > (n_players-1):
                row = n_players-1
            if column  > (n_players-1):
                column = n_players-1
            # Set that location to minus one If it is already minus 1, set it to 0
            if select_grid[row][column] == -1:
                select_grid = np.zeros((n_players,n_players))
            else:
                select_grid = np.zeros((n_players,n_players))#This is to select only one field
                select_grid[row][column] = -1
                
                #Now we highlight in another colour the possible targets
                if row + 1 < n_players:
                    select_grid[row + 1][column] = 1
                if row - 1 >= 0:
                    select_grid[row - 1][column] = 1
                if column - 1 >= 0:
                    select_grid[row][column - 1] = 1
                if column + 1 < n_players:
                    select_grid[row][column + 1] = 1
                
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(n_players):
        for column in range(n_players):
            color = WHITE
            if select_grid[row][column] == -1:
                color_margin = GREEN
                pygame.draw.rect(screen,
                             color_margin,
                             [(MARGIN + WIDTH) * column + 2/3 * MARGIN,
                              (MARGIN + HEIGHT) * row + 2/3 * MARGIN,
                              WIDTH + 2/3 * MARGIN,
                              HEIGHT + 2/3 * MARGIN])
            elif select_grid[row][column] == 1:
                color_margin = BLUE
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
            
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()