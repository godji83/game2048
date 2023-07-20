import pygame, sys, random
from pygame.locals import *
import numpy as np

#The init() function in pygame initializes the pygame engine. This line must be included before you begin writing any pygame code.
pygame.init()
pygame.display.set_caption("MyGame2048")

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (238, 75, 43)
SQURE_WH = 90
BORDER_WH = 10
SCREEN_WH = 5*BORDER_WH + 4*SQURE_WH

font = pygame.font.SysFont("Sans Serif", 50)
FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((SCREEN_WH,SCREEN_WH))

game_board = [[0, 0, 0, 0], # 0, 1, 2, 3
              [0, 0, 0, 0], # 4, 5, 6, 7
              [0, 0, 0, 0], # 8, 9,10,11
              [0, 0, 0, 0]] #12,13,14,15
#game_board = [[2, 4, 8, 16], [32, 64, 128, 256], [512, 1024, 2048, 4096], [8192, 16384, 32768, 65536]]

isGameOver = False
isGameSuccess = False

def checkForEmptyPositions():
    global game_board
    canAddNew = False
    for row in range(4):
        for col in range(4):
            if(game_board[col][row] == 0):
                canAddNew = True
                break
        
        if canAddNew: 
            break 

    return canAddNew

def bordIsBlocked():
    global game_board

    isBlocked = True
    for row in range(4):
        for col in range(4):
            if(col + 1 <= 3 and game_board[row][col] == game_board[row][col + 1] or game_board[row][col] == 0):
                isBlocked = False
                break
            elif(row + 1 <= 3 and game_board[row][col] == game_board[row + 1][col]):
                isBlocked = False
                break
        
        if not(isBlocked): 
            break 

    return isBlocked

def addRandomPositionNumber():
    global game_board
    global isGameOver
    global isGameSuccess

    #todo optimize for when bord become with a few number of possible positions to add new number
    canAddNewNumber = checkForEmptyPositions()
    if(canAddNewNumber):
        while canAddNewNumber:
            position = random.randint(0, 15)
            number = random.randint(1, 2)
            print(position)
            print(number)
            if(position > 11 and game_board[3][position - 12] == 0):
                game_board[3][position - 12] = number * 2
                canAddNewNumber = False
            elif(position <= 11 and position > 7 and game_board[2][position - 8] == 0):
                game_board[2][position - 8] = number * 2
                canAddNewNumber = False
            elif(position <= 7 and position > 3 and game_board[1][position - 4] == 0):
                game_board[1][position - 4] = number * 2
                canAddNewNumber = False
            elif(position <= 3 and game_board[0][position] == 0):
                game_board[0][position] = number * 2
                canAddNewNumber = False
    
    if(bordIsBlocked()):
        isGameOver = True
        isGameSuccess = False
        printGameOver()

def initBoard():
    global game_board
    addRandomPositionNumber()
    addRandomPositionNumber()

def printGameOver():
    global displaysurface
    
    if(isGameSuccess):
        text = font.render("Congratulations!", True, RED)
    else:
        text = font.render("Game Over!", True, RED)

    w = text.get_width()
    h = text.get_height()
    #displaysurface.fill(WHITE)
    displaysurface.blit(text, ((SCREEN_WH - w)/2, (SCREEN_WH - h)/2))
    
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

            if(game_board[col][row] > 0):
                text = font.render(str(game_board[col][row]), True, RED)
                w = text.get_width()
                h = text.get_height()
                displaysurface.blit(text, (row_r + (SQURE_WH - w)/2, col_c + (SQURE_WH - h)/2))

    if isGameOver:
        printGameOver()

#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def rotateCounterclockwise():
    global game_board
    #zip (1, 4, 7) (2, 5, 8) (3, 6, 9)
    #list [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    #reversed (3, 6, 9) (2, 5, 8) (1, 4, 7)
    #result [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    game_board = [list(l) for l in reversed(list(zip(*game_board)))]
def rotateClockwise():
    global game_board
    #reversed [7, 8, 9] [4, 5, 6] [1, 2, 3]
    #zip (7, 4, 1) (8, 5, 2) (9, 6, 3)
    #result [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    game_board = [list(l) for l in zip(*reversed(game_board))]

def rotateDouble():
    global game_board
    #reversed [7, 8, 9] [4, 5, 6] [1, 2, 3]
    #result [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    game_board = [list(reversed(l)) for l in reversed(game_board)]

def doMoveAndSum():
    global game_board
    global isGameOver
    global isGameSuccess

    #sum number and move
    for row in range(4):
        column = [num for num in game_board[row] if num > 0]
        if(len(column) > 0):
            cLen = len(column) - 1
            for i in range(cLen):
                if(i < cLen):
                    if(column[i] == column[i + 1]):
                        column[i] = column[i] + column[i + 1]
                        column[i + 1] = 0
                        if(column[i] == 2048):
                            isGameOver = True
                            isGameSuccess = True
                            printGameOver()

            column = [num for num in column if num > 0]
            cLen = len(column) - 1
            for i in range(4):
                if(i > cLen):
                    column = column + [0]

            game_board[row] = column

    #addRandomPositionNumber
    addRandomPositionNumber()

def moveBoard(direction):
    if event.key == pygame.K_LEFT:
        print("left")
        doMoveAndSum()
    elif event.key == pygame.K_RIGHT:
        print("right")
        rotateDouble()
        doMoveAndSum()
        rotateDouble()
    elif event.key == pygame.K_UP:
        print("up")
        rotateCounterclockwise()
        doMoveAndSum()
        rotateClockwise()
    elif event.key == pygame.K_DOWN:
        print("down")
        rotateClockwise()
        doMoveAndSum()
        rotateCounterclockwise()
    
initBoard()

#Game loop begins
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Exit!")
            pygame.quit()
            sys.exit()
        elif not(isGameOver) and event.type == pygame.KEYDOWN:
           moveBoard(event.key)
    
    drowBoard()

    pygame.display.update()
    FramePerSec.tick(FPS)


