import pygame
import global_variables as g
import numpy as np
import logging

MARGIN = g.MARGIN
WIDTH= g.WIDTH
HEIGHT = g.HEIGHT
n_players = g.n_players
CHAT_HEIGHT = g.CHAT_HEIGHT
CHAT_WIDTH= g.CHAT_WIDTH
text_pos =  [2*MARGIN, (MARGIN + HEIGHT) * n_players + 2*MARGIN]
z=""

screen = pygame.display.set_mode(g.WINDOW_SIZE)

def print_text(Text,paused = False,screen=screen):


    r=pygame.draw.rect(screen,
                             g.WHITE,
                             [ MARGIN,
                              (MARGIN + HEIGHT) * n_players + MARGIN,
                             CHAT_WIDTH,
                              CHAT_HEIGHT])
    
    max_width = r.w
    # Select the font to use, size, bold, italics
    font =  pygame.font.SysFont('Calibri', 15, True, False)
    blit_text(Text,text_pos,font,max_width,paused)
    if paused:
        input('Press enter to continue: ')
#    time.sleep(2)
    

    
def blit_text(text, pos, font,max_width=screen.get_size()[0],paused=False,surface=screen, color=pygame.Color('black')):
    if paused:
        text= text + "\nPress Enter to continue."
        
    
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.

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
    
        

def select_field(event,select_grid,world,text):
    if (select_grid==np.zeros((n_players,n_players))).all():
        text= 'It is your turn, Player '+ repr(g.human_playerid)+ '. Choose wisely'
    if event.type == pygame.MOUSEBUTTONDOWN:
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        column = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)
        #We set the limits so that if we click on borthers, the max value is the last row
        if row< n_players and column <n_players:
            if row  == n_players:
                row = n_players-1
            if column == (n_players-1):
                column = n_players-1
            # Set that location to minus one If it is already minus 1, set it to 0
            if select_grid[row][column] == -1:
                select_grid = np.zeros((n_players,n_players))
            elif select_grid[row][column] == 1 and world[row][column]!= g.human_playerid:#If it is a field that the country can attack
                select_grid[row][column] = 2
            elif select_grid[row][column] == 1 and world[row][column]== g.human_playerid:#If it is a field that the country can attack
                select_grid[row][column] = 0
                text='The target country is ' + repr(pos)+ '. It belongs to Player ' + repr(world[row][column]) + '. Click again to attack this country.'
            elif world[row][column]== g.human_playerid:#To select only the ones from the human player
                select_grid = np.zeros((n_players,n_players))#This is to select only one field
                select_grid[row][column] = -1
                text='Player ' + repr(g.human_playerid) +' attacks from country ' + repr(pos)
                #Now we highlight in another colour the possible countries to be attacked from the selected country
                if row + 1 < n_players and world[row + 1][column]!=g.human_playerid:
                    select_grid[row + 1][column] = 1
                if row - 1 >= 0 and world[row - 1][column]!=g.human_playerid:
                    select_grid[row - 1][column] = 1
                if column - 1 >= 0 and world[row][column-1]!=g.human_playerid:
                    select_grid[row][column - 1] = 1
                if column + 1 < n_players and world[row][column + 1]!=g.human_playerid:
                    select_grid[row][column + 1] = 1
    #        z = "Click %s Grid coordinates:  %s %s" % (pos,row,column)
    return select_grid,text
def next_turn(event,computer_turn=False):
    if event.type == pygame.MOUSEBUTTONDOWN:
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        if pos[0]>=g.NEXT_TURN_xpos and pos[0]<=(g.NEXT_TURN_xpos+g.NEXT_TURN_WIDTH) and pos[1]>=g.NEXT_TURN_ypos and pos[1]<=(g.NEXT_TURN_ypos+g.NEXT_TURN_HEIGHT):
            computer_turn=True
            logging.debug('You have clicked Next_Turn button')
    return computer_turn

def attack(event,attackFlag=False):
    if event.type == pygame.MOUSEBUTTONDOWN:
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        if pos[0]>=g.ATTACK_xpos and pos[0]<=(g.ATTACK_xpos+g.NEXT_TURN_WIDTH) and pos[1]>=g.ATTACK_ypos and pos[1]<=(g.ATTACK_ypos+g.NEXT_TURN_HEIGHT):
            attackFlag=True
            logging.debug('You have clicked Attack button')
    return attackFlag

def start_game(event):
    startFlag=False
    if event.type == pygame.MOUSEBUTTONDOWN:
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        if pos[0]>=g.START_xpos and pos[0]<=(g.START_xpos+g.START_WIDTH) and pos[1]>=g.START_ypos and pos[1]<=(g.START_ypos+g.START_HEIGHT):
            startFlag=True
            logging.debug('You have clicked Start button')
    return startFlag

def draw_world(world,select_grid = g.select_grid_0,end_game=False,Ranking=0):
    
    if end_game:
        global text
        display_ranking(Ranking)
        text='End of the game'
    else:
        for row in range(g.n_players):
            for column in range(g.n_players):
                if select_grid[row][column] == -1:
                    color_margin = g.GREEN
                    pygame.draw.rect(screen,
                                 color_margin,
                                 [(MARGIN + WIDTH) * column + 2/3 * MARGIN,
                                  (MARGIN + HEIGHT) * row + 2/3 * MARGIN,
                                  WIDTH + 2/3 * MARGIN,
                                  HEIGHT + 2/3 * MARGIN])
                elif select_grid[row][column] == 1:
                    color_margin = g.WHITE
                    pygame.draw.rect(screen,
                                 color_margin,
                                 [(MARGIN + WIDTH) * column + 2/3 * MARGIN,
                                  (MARGIN + HEIGHT) * row + 2/3 * MARGIN,
                                  WIDTH + 2/3 * MARGIN,
                                  HEIGHT + 2/3 * MARGIN])
                elif select_grid[row][column] == 2:
                    color_margin = g.RED
                    pygame.draw.rect(screen,
                                 color_margin,
                                 [(MARGIN + WIDTH) * column + 2/3 * MARGIN,
                                  (MARGIN + HEIGHT) * row + 2/3 * MARGIN,
                                  WIDTH + 2/3 * MARGIN,
                                  HEIGHT + 2/3 * MARGIN])
                pygame.draw.rect(screen,
                                 g.color_matrix [world[row][column]],
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
    return
                
def display_ranking(Ranking):
    font = pygame.font.SysFont('Calibri', 15, True, False)
    
    pygame.draw.rect(screen,
                             g.WHITE,
                             [ g.RANKING_XPOS,
                              g.RANKING_YPOS,
                             CHAT_WIDTH,
                              g.WINDOW_HEIGHT-2*MARGIN])
    
    text= 'Player || Countries'
    blit_text(text,(g.RANKING_XPOS + MARGIN,g.RANKING_YPOS+ MARGIN),font)
    for i in range(0,n_players):
        #pos=Ranking[i][0]
        Player=Ranking[i][1]
        Countries=Ranking[i][2]
        text='|| '+ repr(Countries)
        #Where to draw each rectangle?
        x_rect=g.RANKING_XPOS + MARGIN
        y_rect=(g.RANKING_YPOS+ MARGIN)+(MARGIN + HEIGHT) *(i+1)
        pygame.draw.rect(screen,
                     g.color_matrix [Player],
                     [x_rect,
                      y_rect,
                      WIDTH,
                      HEIGHT])
        blit_text(str(Player),(x_rect,y_rect),font)
        blit_text(text,(x_rect+2*WIDTH,y_rect),font)
        
def next_turn_button():
    font=pygame.font.SysFont('Calibri', 15, True, False)
    pygame.draw.rect(screen,
                     g.BLACK,
                     [g.NEXT_TURN_xpos - 1/2 * MARGIN,
                      g.NEXT_TURN_ypos- 1/2 * MARGIN,
                      g.NEXT_TURN_WIDTH +  MARGIN,
                      g.NEXT_TURN_HEIGHT+  MARGIN])
    pygame.draw.rect(screen,
                     g.BLUE,
                     [g.NEXT_TURN_xpos,
                      g.NEXT_TURN_ypos,
                      g.NEXT_TURN_WIDTH,
                      g.NEXT_TURN_HEIGHT])
    
    blit_text('NEXT TURN',(g.NEXT_TURN_xpos+WIDTH,g.NEXT_TURN_ypos),font,color=g.WHITE)
    
def attack_button():
    font=pygame.font.SysFont('Calibri', 15, True, False)
    pygame.draw.rect(screen,
                     g.BLACK,
                     [g.ATTACK_xpos - 1/2 * MARGIN,
                      g.ATTACK_ypos- 1/2 * MARGIN,
                      g.NEXT_TURN_WIDTH +  MARGIN,
                      g.NEXT_TURN_HEIGHT+  MARGIN])
    pygame.draw.rect(screen,
                     g.RED,
                     [g.ATTACK_xpos,
                      g.ATTACK_ypos,
                      g.NEXT_TURN_WIDTH,
                      g.NEXT_TURN_HEIGHT])
    
    blit_text('ATTACK',(g.ATTACK_xpos+WIDTH,g.ATTACK_ypos),font,color=g.WHITE)
    
def start_button():
    font=pygame.font.Font('freesansbold.ttf',25)
    pygame.draw.rect(screen,
                     g.BLACK,
                     [g.START_xpos - 1/2 * MARGIN,
                      g.START_ypos- 1/2 * MARGIN,
                      g.START_WIDTH + MARGIN,
                      g.START_HEIGHT + MARGIN])
    pygame.draw.rect(screen,
                     g.PURPLE,
                     [g.START_xpos,
                      g.START_ypos,
                      g.START_WIDTH,
                      g.START_HEIGHT])
    
    blit_text('START',(g.START_xpos+WIDTH,g.START_ypos),font,color=g.BLACK)
    
    
    
def final_ranking(Ranking):
    font = pygame.font.SysFont('Calibri', 15, True, False)
    
    
    
    pygame.draw.rect(screen,
                             g.WHITE,
                             [ MARGIN,
                              MARGIN,
                             g.WINDOW_WIDTH-3*MARGIN,
                              g.WINDOW_HEIGHT-2*MARGIN])
    
    
    width_rect=g.WINDOW_WIDTH-6*MARGIN
    height_rect=5*MARGIN
    pygame.draw.rect(screen,
                             g.PURPLE,
                             [3*MARGIN,
                              g.RANKING_YPOS+MARGIN,
                             width_rect,
                              height_rect])
    text='Final Ranking'
    blit_text(text,(3*MARGIN + width_rect/2,g.RANKING_YPOS + height_rect/2),font,color=g.WHITE)    
    text= 'Player || Countries'
    blit_text(text,(g.WINDOW_WIDTH/2-2*MARGIN,8*MARGIN),font)
    for i in range(0,n_players):
        pos=Ranking[i][0]
        Player=Ranking[i][1]
        Countries=Ranking[i][2]
        text='|| '+ repr(Countries)
        #Where to draw each rectangle?
        x_rect= g.WINDOW_WIDTH/2-2*MARGIN
        y_rect=(g.RANKING_YPOS+ 6*MARGIN)+(MARGIN + HEIGHT) *(i+1)
        pygame.draw.rect(screen,
                     g.color_matrix [Player],
                     [x_rect,
                      y_rect,
                      WIDTH,
                      HEIGHT])
        blit_text(str(pos),(x_rect-5*MARGIN,y_rect),font)
        blit_text(str(Player),(x_rect,y_rect),font)
        blit_text(text,(x_rect+2*WIDTH,y_rect),font)
        
        

def intro_page():
    font = pygame.font.Font('freesansbold.ttf',115, True, False)
    
    
    
    pygame.draw.rect(screen,
                             g.WHITE,
                             [ MARGIN,
                              MARGIN,
                             g.WINDOW_WIDTH-3*MARGIN,
                              g.WINDOW_HEIGHT-2*MARGIN])
    
    
    width_rect=g.WINDOW_WIDTH-6*MARGIN
    height_rect=5*MARGIN
    pygame.draw.rect(screen,
                             g.PURPLE,
                             [3*MARGIN,
                              g.RANKING_YPOS+MARGIN,
                             width_rect,
                              height_rect])