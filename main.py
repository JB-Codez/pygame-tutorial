import pygame
import random
import math

import pygame
from pygame import mixer


# Initialize the pygame
pygame.init()

# create the screen
# this line creates the window but it immediately closes/exits
screen = pygame.display.set_mode((800,600)) # width, height (also, screen is the VAR name)


# Background
background = pygame.image.load('imgs/background.png')

# Background sound
mixer.music.load('snds/background.wav')
mixer.music.play(-1)

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
enemyImg=[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('imgs/enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)


# Bullet

# Ready State - you can't see the bullet on the screen
# Fire state - the bullet is currently moving
bulletImg = pygame.image.load('imgs/bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 2
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf')

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

    
def player(x, y):
    # screen.blit(playerImg, (playerX, playerY))
    screen.blit(playerImg, (x, y)) # draw (what,where)

def enemy(x,y, i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10)) # shows up in the center of the spaceship

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) +(math.pow(enemyY-bulletY,2) )) # distance between bullet and the enemy
    if distance < 27:
        return True
    else:
        return False

# keep our game running
# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    # this is drawn first
    screen.fill((0,0,0)) # by default this doesn't work - we need to update it
    #playerX += .01

    # Background Image
    screen.blit(background,(0,0))
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the X button has been pressed, i.e. close
            running = False
        # this will appear constantly in the game

        # if keystroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:
            #print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                #print("Left arrow is pressed")
                playerX_change = - 5
            if event.key == pygame.K_RIGHT:
                #print("Right arrow is pressed")
                playerX_change = + 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('snds/laser.wav')
                    bullet_Sound.play()
                    # get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY) # starting location of our bullet

        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                #print("Keystoke has been released")
                playerX_change = 0.0
    
    # Player movement
    # Checking for boundaries of spaceship so
    # it doesn't go out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: # 800-64
        playerX = 736

    

    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
   
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736: # 800-64
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('snds/explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 100
            #print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i], enemyY[i], i)




    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # default for bullet is READY
    # when spacebar hit, state changes to FIRE
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    

    
    player(playerX, playerY)

    show_score(textX, textY)

    pygame.display.update() # needed to display 
