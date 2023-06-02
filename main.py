import pygame

# Initialize the pygame
pygame.init()

# create the screen
# this line creates the window but it immediately closes/exits
screen = pygame.display.set_mode((800,600))


# keep our game running
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the X button has been pressed, i.e. close
            running = False
