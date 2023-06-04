import pygame

# Initialize the pygame
pygame.init()

# create the screen
# this line creates the window but it immediately closes/exits
screen = pygame.display.set_mode((800,600))


# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('imgs/ufo.png')
pygame.display.set_icon(icon)

# keep our game running
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the X button has been pressed, i.e. close
            running = False
    # this will appear constantly in the game
    # RGB - Red, Green, Blue
    screen.fill((0,0,0)) # by default this doesn't work - we need to update it
    pygame.display.update()
