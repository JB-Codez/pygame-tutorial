import pygame

# Initialize the pygame
pygame.init()

# create the screen
# this line creates the window but it immediately closes/exits
screen = pygame.display.set_mode((800,600)) # width, height (also, screen is the VAR name)


# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('imgs/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('imgs/space-invaders.png')
playerX = 370 
playerY = 480
    
def player():
    screen.blit(playerImg, (playerX, playerY)) # draw (what,where)

# keep our game running
# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    # this is drawn first
    screen.fill((0,0,0)) # by default this doesn't work - we need to update it

            
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the X button has been pressed, i.e. close
            running = False
    # this will appear constantly in the game

    player()
    pygame.display.update() # need to dispaly stuff
