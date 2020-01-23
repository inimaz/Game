
import pygame
import numpy as np
import helpers as h
import global_variables as g
import helpers_draw as hd
import logging

logger = logging.getLogger(__name__)


def main():
    # For logging
    logging.basicConfig(filename='Game.log', level=logging.DEBUG)

    n_players = g.n_players
    world = h.start_game(n_players)
    # Create a 2 dimensional array. It wil contain the selected positions
    select_grid = np.zeros((n_players, n_players))

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    # For the window size to be according to the width and height

    WINDOW_SIZE = g.WINDOW_SIZE
    screen = pygame.display.set_mode(WINDOW_SIZE)
    # Set title of screen
    pygame.display.set_caption("The Game")

    # Loop until the user clicks the close button.
    done = False
    end_game = False
    computer_turn = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    game_intro(screen, clock)
    text = "Welcome to a Game called The Game.\nLet's have fun" + \
        " with this game.\nConquer all countries to win!"

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                logging.info('Exit game')
    #        If we want to select one field
            text, world, select_grid, computer_turn = h.global_turn(
                world, n_players, select_grid, event, text, computer_turn)
        Ranking = h.ranking(world, n_players)
        # All CODE TO DRAW SHOULD GO BELOW THIS LINE
        # Set the screen background
        screen.fill(g.BLACK)

        # Draw the grid

        if g.end_game:
            hd.final_ranking(Ranking)
        else:
            hd.draw_world(world, select_grid, end_game, Ranking)
            hd.print_text(text)
            hd.display_ranking(Ranking)
            hd.next_turn_button()
            hd.attack_button()
        # All CODE TO DRAW SHOULD GO ABOVE THIS LINE
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


def game_intro(screen, clock):

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            intro = not (hd.start_game(event))

        screen.fill(g.WHITE)
        hd.start_button()

        pygame.display.update()
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


if __name__ == '__main__':
    main()
