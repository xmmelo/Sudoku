from re import X
from block import *
from square import *

HEIGHT = 9
WIDTH = 9

def orderByX(squares):
    XBlocks = []
    for x in range(1, HEIGHT + 1):
        XBlocks.append(block(x, [p for p in squares if p.x == x]))
    return XBlocks

def orderByY(squares):
    YBlocks = []
    for y in range(1, WIDTH + 1):
        YBlocks.append(block(y, [p for p in squares if p.y == y]))
    return YBlocks

def orderByBlocks(squares):
    SquareBlock = []
    ID = 1
    for x in range(3, HEIGHT + 3, 3):
        for y in range(3, WIDTH + 3, 3):  
            # ids = [p.ID for p in squaresForBlock]
            # print(str(ID) + '!!' + str(ids[:]) )
            SquareBlock.append(block(ID, [p for p in squares if (x-3 < p.x <= x and y-3 < p.y <= y)]))
            ID = ID + 1     
    
    return SquareBlock

def generateGameSquaresFromBoard(board):
    gamesquares = []
    ID = 1
    x = 1
    for line in board:
        y = 1
        for value in line:
            gamesquare = square(x,y,ID)
            
            if value != 0:
                gamesquare.setValue(value)
        
            gamesquares.append(gamesquare)
            ID = ID + 1
            y = y + 1

        x = x + 1

    print('GAME SQUARES: ' + str(len(gamesquares)))
    return gamesquares