import pygame
import random

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
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('imgs/enemy.png')
enemyX = random.randint(0,800) 
enemyY = random.randint(50,150)
enemyX_change = 0
    
def player(x, y):
    # screen.blit(playerImg, (playerX, playerY))
    screen.blit(playerImg, (x, y)) # draw (what,where)

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

# keep our game running
# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    # this is drawn first
    screen.fill((0,0,0)) # by default this doesn't work - we need to update it
    #playerX += .01
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the X button has been pressed, i.e. close
            running = False
        # this will appear constantly in the game

        # if keystroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:
            #print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                #print("Left arrow is pressed")
                playerX_change = - 0.1
            if event.key == pygame.K_RIGHT:
                #print("Right arrow is pressed")
                playerX_change = + 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                #print("Keystoke has been released")
                playerX_change = 0.0
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: # 800-64
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update() # need to dispaly stuff
