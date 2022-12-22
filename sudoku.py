from square import *
from util import *

HEIGHT = 9
WIDTH = 9

def createGame(gameSquares = []):
    
    # if len(gameSquares) == 0:
    #     for x in range(1, HEIGHT + 1):
    #         for y in range(1, WIDTH + 1):
    #             gameSquares.append(square(y, x))

    XBlocks = orderByX(gameSquares)
    YBlocks = orderByY(gameSquares)
    SquareBlocks = orderByBlocks(gameSquares)
    
    for gameSquare in gameSquares:
        gameSquare.setXBlock(XBlocks)
        gameSquare.setYBlock(YBlocks)
        gameSquare.setSquareBlock(SquareBlocks)


    return gameSquares


def solve(gameSquares):

    gameSquares.sort(reverse=False, key=lambda e: e.ID) 
    notSolved = True
    i = 0 
    
    while(notSolved):
        
        print("iteração: " + str(i))
        
        for gameSquare in gameSquares:          
            gameSquare.solve()

        

        print("Quadrados resolvidos: " + str(len([x for x in gameSquares if x.hasValue == True])))

        print(str(any(x for x in gameSquares if x.hasValue == False)))
        
        i = i + 1
        notSolved = any(x for x in gameSquares if x.hasValue == False)

        gameLine = ''

        for square in gameSquares:
            gameLine = gameLine + ' ! ' + str(square.value) + ' ! '
            if (square.ID % 9 == 0):
                print(gameLine)
                gameLine = ''

        for square in gameSquares:
            squareStatus = str(square.ID) + ' ! ' + str(square.possibleValues)[:]
            print(squareStatus)

        
        
        # for x in range(1, HEIGHT + 1):           
        #     for y in range(1, WIDTH + 1):
        #         squarino = next((sqr for sqr in gameSquares if sqr.x == x and sqr.y == y), None)

        #         gameLine = gameLine + ' ! ' + str(squarino.value) + ' ! '

        #     print(gameLine)
        #     gameLine = ''



        

        # for x in range(1, HEIGHT + 1):           
        #     for y in range(1, WIDTH + 1):
        #         squarino = next((sqr for sqr in gameSquares if sqr.x == x and sqr.y == y), None)

        #         gameLine = gameLine + ' ! ' + str(squarino.value) + ' ! '

        #     print(gameLine)
        #     gameLine = ''

        # for x in range(1, HEIGHT + 1):
                    
        #             for y in range(1, WIDTH + 1):
        #                 squarino = next((sqr for sqr in gameSquares if sqr.x == x and sqr.y == y), None)

        #                 squareVal  = 0

        #                 if squarino.hasValue:
        #                     squareVal = squarino.value
                        
        #                 gameLine = gameLine + ' ! ' + str(squareVal) + ' ! '

        #             print(gameLine)
        #             gameLine = ''
             
        








