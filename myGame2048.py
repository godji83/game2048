import pygame, sys, random
from pygame.locals import *


#The init() function in pygame initializes the pygame engine. This line must be included before you begin writing any pygame code.
pygame.init()

print_message = pygame.USEREVENT + 0
pygame.time.set_timer(print_message, 3000)

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (238, 75, 43)
SQURE_WH = 90
BORDER_WH = 10
SCREEN_WH = 5*BORDER_WH + 4*SQURE_WH

font = pygame.font.SysFont("Sans Serif", 50)

def initBoard():
    game_board = [[0, 0, 0, 0], # 1, 2, 3, 4
                  [0, 0, 0, 0], # 5, 6, 7, 8
                  [0, 0, 0, 0], # 9,10,11,12
                  [0, 0, 0, 0]] #13,14,15,16
    
    for i in range(2):
        position = random.randint(1, 16)
        number = random.randint(1, 2)
        print(position)
        print(number)
        if(position > 12):
            game_board[3][position - 13] = number * 2
        elif(position > 8):
            game_board[2][position - 9] = number * 2
        elif(position > 4):
            game_board[1][position - 5] = number * 2
        else:
            game_board[0][position - 1] = number * 2

    return game_board

game_board = initBoard()
game_board = [[2, 4, 8, 16], # 1, 2, 3, 4
              [32, 64, 128, 256], # 5, 6, 7, 8
              [512, 1024, 2048, 4096], # 9,10,11,12
              [8192, 16384, 32768, 65536]]

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((SCREEN_WH,SCREEN_WH))

pygame.display.set_caption("MyGame2048")
color1 = pygame.Color(0, 0, 0)

def drowBoard():
    global displaysurface
    displaysurface.fill(BLACK)

    for row in range(4):
        for col in range(4):
            rect = pygame.Surface((SQURE_WH, SQURE_WH))
            rect.fill(WHITE)
            row_r = BORDER_WH + row * SQURE_WH + row * BORDER_WH
            col_c = BORDER_WH + col * SQURE_WH + col * BORDER_WH
            displaysurface.blit(rect, (row_r, col_c))

            if(game_board[row][col] > 0):
                text = font.render(str(game_board[row][col]), True, RED)
                w = text.get_width()
                h = text.get_height()
                displaysurface.blit(text, (row_r + (SQURE_WH - w)/2, col_c + (SQURE_WH - h)/2))
            
#Game loop begins
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Exit!")
            pygame.quit()
            sys.exit()
        elif event.type == print_message:
            print("Hello World")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up")
            elif event.key == pygame.K_DOWN:
                print("down")
            elif event.key == pygame.K_LEFT:
                print("left")
            elif event.key == pygame.K_RIGHT:
                print("right")

        else:
            print(event)
        
    drowBoard()

    pygame.display.update()
    FramePerSec.tick(FPS)


