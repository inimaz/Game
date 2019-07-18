# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)


n_players = 10
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
CHAT_HEIGHT = 5*HEIGHT
 
# This sets the margin between each cell
MARGIN = 5

def initialize ():
    WINDOW_WIDTH = n_players * WIDTH + (n_players-1)*MARGIN + 2*MARGIN
    WINDOW_HEIGHT = n_players * HEIGHT + (n_players-1)*MARGIN + 2*MARGIN + CHAT_HEIGHT
    WINDOW_SIZE = [WINDOW_WIDTH, WINDOW_HEIGHT]
    return WINDOW_SIZE