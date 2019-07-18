import pygame
import constants
import numpy as np

MARGIN = constants.MARGIN
WIDTH= constants.WIDTH
HEIGHT = constants.HEIGHT
n_players = constants.n_players
CHAT_HEIGHT = constants.CHAT_HEIGHT
CHAT_WIDTH= (MARGIN + WIDTH) * n_players - MARGIN
text_pos =  [2*MARGIN, (MARGIN + HEIGHT) * n_players + 2*MARGIN]
z=""

def print_text(Text,screen):


    pygame.draw.rect(screen,
                             constants.WHITE,
                             [ MARGIN,
                              (MARGIN + HEIGHT) * n_players + MARGIN,
                             CHAT_WIDTH,
                              CHAT_HEIGHT])
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 15, True, False)
 
    blit_text(screen,Text,text_pos,font)
    

    
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
        

def select_field(event,select_grid):
    if event.type == pygame.MOUSEBUTTONDOWN:
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
            
            #Now we highlight in another colour the possible countries to be attacked from the selected country
            if row + 1 < n_players:
                select_grid[row + 1][column] = 1
            if row - 1 >= 0:
                select_grid[row - 1][column] = 1
            if column - 1 >= 0:
                select_grid[row][column - 1] = 1
            if column + 1 < n_players:
                select_grid[row][column + 1] = 1
#        z = "Click %s Grid coordinates:  %s %s" % (pos,row,column)
    return select_grid