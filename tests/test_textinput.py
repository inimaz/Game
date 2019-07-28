import pygame_textinput
import pygame
import helpers_draw as hd
pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInput()

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()
aa="Nothing"
done = False
while not done:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done=True
            exit()

    # Feed it with events every frame
    if textinput.update(events):
        aa=textinput.get_text()
    
    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))
    
   
    font = pygame.font.SysFont('Calibri', 15, True, False)
 
    hd.blit_text(screen,aa,(20,25),font)
    
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()