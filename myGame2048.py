import pygame, sys, random
from pygame.locals import *


#The init() function in pygame initializes the pygame engine. This line must be included before you begin writing any pygame code.
pygame.init()

print_message = pygame.USEREVENT + 0
pygame.time.set_timer(print_message, 3000)

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SQURE_WH = 90

game_board = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
FramePerSec = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
mySurface = pygame.Surface((SQURE_WH, SQURE_WH))

pygame.display.set_caption("MyGame2048")
color1 = pygame.Color(0, 0, 0) 

#Game loop begins
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Exit!")
            pygame.quit()
            sys.exit()
        elif event.type == print_message:
            print("Hello World")
        
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(mySurface, (50,50))
    pygame.display.update()
    FramePerSec.tick(FPS)