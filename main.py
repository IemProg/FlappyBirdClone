"""
Author: @Iem-Prog
Date: 22, Sept 2017
Description: A Clone of the famous Flappy Bird game written with Python using PyGame module.
"""

import pygame, time
from random import randint, randrange

black = (0, 0, 0)
white = (255, 255, 255)
GREEN = (0, 255, 0)

sunset = (253, 72, 47)

greenyellow = (184, 255, 0)
brightblue = (47, 228, 253)
orange = (255, 113, 0)
yellow = (255, 236, 0)
purple = (252, 67, 255)
ColorChoices = [greenyellow, brightblue, orange, yellow, purple]

HEIGHT = 550
WIDTH = 800

ImageHEIGHT = 40
ImageWidth = 30

#Initialization of pygame module
pygame.init()

display = pygame.display.set_mode((WIDTH, HEIGHT))        #Create a window with 800*400
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()                      #To measure the frames per time

def Game_Over():
    msgGame("Game Over!")

def BirdFlipping(x, y, img):
    display.blit(img, (x, y))

def score(score):
    font = pygame.font.Font("freesansbold.ttf", 18)
    text = font.render("Score: "+ str(score), True, white)
    display.blit(text, [5, 5])

def Blocks(x_block, y_block, b_width, b_height, gap, colorChoice):
    pygame.draw.rect(display, colorChoice, [x_block, y_block, b_width, b_height])
    pygame.draw.rect(display, colorChoice, [x_block, y_block + b_height + gap, b_width, HEIGHT])

def quit_or_replay():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key

    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def msgGame(text):
    SmallText = pygame.font.Font("freesansbold.ttf", 22)
    LargeText = pygame.font.Font("freesansbold.ttf", 70)

    titleTextSurf, titleTextRect = makeTextObjs(text, LargeText)
    titleTextRect.center = WIDTH/2, HEIGHT/2
    display.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs("Press any key to continue!", SmallText)
    typTextRect.center = WIDTH/2, (HEIGHT/2 + 100)
    display.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(0.1)

    while quit_or_replay() == None:
        clock.tick()
    main()

IMG = pygame.image.load('flappy.ico')               #Uploading a bird photo

def main():
    x = 150
    y = 200
    y_move = 0

    x_block = WIDTH
    y_block = 0
    block_width = 75
    block_height = randint(0, (HEIGHT/2))
    gap = ImageHEIGHT * 3
    block_move = 5
    current_score = 0

    BlockColor = ColorChoices[randrange(0, 5)]

    GAMEOVER = False

    #Main loop
    while not GAMEOVER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAMEOVER = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
        y += y_move

        display.fill((0, 0, 0))               #Display Black color
        BirdFlipping(x, y, IMG)                #Draw the FlappyBird

        #Drawing blocks
        Blocks(x_block, y_block, block_width, block_height, gap, BlockColor)
        score(current_score)
        x_block -= block_move

        if (y > HEIGHT-40 or y < 0):
            Game_Over()                    #If Bird touches boundaries, Game is Over

        if x_block < (-1*block_width):           #If the Block is moved off on the screen "No more blocks is screen"
            x_block = WIDTH
            block_height = randint(0, (HEIGHT/2))
            current_score +=1

        if x + ImageWidth > x_block:
            if x < x_block + block_width:
                #print("Possible crash!")
                if y < block_height:
                    #print("Y crossover UPPER")
                    if x- ImageWidth < block_width + x_block:
                        #print("Game Over!")
                        Game_Over()

        if x + ImageWidth > x_block:
            #print('x crossover')
            if y + ImageHEIGHT > block_height + gap:
                #print("Y crossover lower")
                if x < block_width + x_block:
                    #print("Game over LOWER")
                    Game_Over()

        #if (x_block < (x - block_width) < x_block + block_move):
        #   current_score += 1
        #   gap = 0

        if (current_score >=2) and (current_score <= 5):
            block_move = 6
            gap = ImageHEIGHT * 2.6

        pygame.display.update()                 #Update the screen
        clock.tick(80)                     #100 frames per second

main()
pygame.quit()
quit()