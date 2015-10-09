# These are import statements, just like in Java!
# They help us so we don't have to rewrite code someone else has already written
import pygame, sys
from random import randint
from pygame.locals import *
from Helpers import *
from Constants import *



# This is the head of the snake.
# What type is it?!?!
snakeHead = Rect(blockSize, blockSize, blockSize, blockSize)

# This is the body of the snake.
# These brackets mean that the body is a list;
# In other words, there might be many parts to the body.
snakeBody = []

# This is the apple.
# Calling randomRect starts the apple off in a random place on the screen.
apple = randomRect()
PowerUp1=randomRect()
PowerUp2=randomRect()
PowerUp1B=randomRect()
PowerUp2B=randomRect()
PowerUp1C=randomRect()
PowerUp2C=randomRect()
Apple2=randomRect()
Apple3=randomRect()
Apple4=randomRect()
Apple5=randomRect()
Apple6=randomRect()
Apple7=randomRect()
Apple8=randomRect()
Apple9=randomRect()
Apple10=randomRect()
RWall=randomRect()
# Set up the screen. Don't worry about this code - it tells python that we want a screen of a certain size
pygame.init()
scrHeight = yBound * blockSize
scrWidth = xBound * blockSize
screen = pygame.display.set_mode((scrHeight, scrWidth))
initWalls(screen)
clock = pygame.time.Clock()
score=0

# This loop is very interesting. When will it stop running?
# (hint- when is the while condition false?)
while True:
    clock.tick(5+score/2)

    # This gets the keyboard input. Don't worry too much about the first couple lines.
    for keypress in pygame.event.get():
        if keypress.type == QUIT:
            quitGame()

        # This is where we switch directions based on which key is pressed.
        # What do you think elif means? Does it sound like anything you've heard before?
        # Why do we check direction != UP, direction != DOWN, etc. ?
        elif keypress.type == KEYDOWN:
            # Check for the up arrow key
            if keypress.key == K_UP and direction != DOWN:
                direction = UP
            # Check for the down arrow key
            elif keypress.key == K_DOWN and direction != UP:
                direction = DOWN
            # Check for the left arrow key
            elif keypress.key == K_LEFT and direction != RIGHT:
                direction = LEFT
            # Check for the right arrow key
            elif keypress.key == K_RIGHT and direction != LEFT:
                direction = RIGHT

    # Copy the head for later use.
    oldPiece = snakeHead.copy()
    # Move the head in the direction we are facing.
    snakeHead = moveHead(snakeHead, direction)

    # Update the snake's body (excluding the head).
    # This piece of code takes each piece in the body and shifts it to where the next piece is
    # so it looks like the snake is moving!
    for i in range(0, len(snakeBody)):
        temp = snakeBody[i].copy()
        snakeBody[i] = moveBody(oldPiece, snakeBody[i])
        oldPiece = temp

    # These are variables that are True or False depending on conditions.
    # What do we call these kinds of variables?
    hasHitWall = snakeHead.collidelist(walls) != -1
    hasHitBody = snakeHead.collidelist(snakeBody) != -1
    hasEaten = snakeHead.colliderect(apple)
    SlowDown=snakeHead.colliderect(PowerUp1)
    SpeedUp=snakeHead.colliderect(PowerUp2)
    SlowDown2=snakeHead.colliderect(PowerUp1B)
    SpeedUp2=snakeHead.colliderect(PowerUp2B)
    SlowDown3=snakeHead.colliderect(PowerUp1C)
    SpeedUp3=snakeHead.colliderect(PowerUp2C)
    hasEaten2=snakeHead.colliderect(Apple2)
    hasEaten3=snakeHead.colliderect(Apple3)
    hasEaten4=snakeHead.colliderect(Apple4)
    hasEaten5=snakeHead.colliderect(Apple5)
    hasEaten6=snakeHead.colliderect(Apple6)
    hasEaten7=snakeHead.colliderect(Apple7)
    hasEaten8=snakeHead.colliderect(Apple8)
    hasEaten9=snakeHead.colliderect(Apple9)
    hasEaten10=snakeHead.colliderect(Apple10)
    hasHitRWall=snakeHead.colliderect(RWall)
    # Checks if the head collides with the wall.
    if(hasHitWall):
        quitGame()
    if(hasHitBody):
        quitGame()
    if(hasHitRWall):
        quitGame()
    # We need to check if the head has collided with the body!
    # How can we do this?
    # (hint- it should be very similar to the line above!)
    # Go ahead and do it here!


    # Checks if the head collides with the apple.
    if (hasEaten):
        apple = randomRect()
        snakeBody.append(oldPiece)
        score=score+1
    if (SlowDown):
        PowerUp1=randomRect()
        score=score-3
    if (SpeedUp):
        PowerUp2=randomRect()
        score=score+5
    if (SlowDown2):
        PowerUp1B=randomRect()
        score=score-3
    if (SpeedUp2):
        PowerUp2B=randomRect()
        score=score+5
    if (SlowDown3):
        PowerUp1C=randomRect()
        score=score-3
    if (SpeedUp3):
        PowerUp2C=randomRect()
        score=score+5
    if (hasEaten2):
        Apple2 = randomRect()
        snakeBody.append(oldPiece)
        score=score+1
    if (hasEaten3):
        Apple3 = randomRect()
        snakeBody.append(oldPiece)
        score=score+1
    if (hasEaten4):
        Apple4 = randomRect()
        snakeBody.append(oldPiece)
        score=score+1
    if (hasEaten5):
        Apple5 = randomRect()
        snakeBody.append(oldPiece)
        score=score+1
    if (hasEaten6):
        Apple6 = randomRect()
        snakeBody.append(oldPiece)
        score=score+1
    if (hasEaten7):
        Apple7 = randomRect()
        snakeBody.append(oldPiece)
        score=score+1
    if (hasEaten8):
        Apple8 = randomRect()
        snakeBody.append(oldPiece)
        score=score+1
    if (hasEaten9):
        Apple9 = randomRect()
        snakeBody.append(oldPiece)
        score=score+1
    if (hasEaten10):
        Apple10 = randomRect()
        snakeBody.append(oldPiece)
        score=score+1

    #Graphically draws all the updates we just made.
    draw(oldPiece, snakeHead, snakeBody, apple, Apple2, Apple3, Apple4, Apple5, Apple6, Apple7, Apple8, Apple9, Apple10, hasEaten, PowerUp1, PowerUp2B, PowerUp1B, PowerUp2, PowerUp2C, PowerUp1C, RWall, screen)
    pygame.display.flip()






