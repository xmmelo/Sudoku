from tkinter import *
from sudoku import *


board = [
    [0,0,7,0,4,0,0,0,0],
    [0,0,0,0,0,8,0,0,6],
    [0,4,1,0,0,0,9,0,0],
    [0,0,0,0,0,0,1,7,0],
    [0,0,0,0,0,6,0,0,0],
    [0,0,8,7,0,0,2,0,0],
    [3,0,0,0,0,0,0,0,0],
    [0,0,0,1,2,0,0,0,0],
    [8,6,0,0,7,6,0,0,5]
]


board3 = [
    [4,1,0,3,0,0,7,6,0],
    [0,9,3,0,7,0,4,0,1],
    [2,0,0,1,4,0,0,8,3],
    [9,5,8,0,0,0,0,0,7],
    [3,4,0,0,0,7,0,1,0],
    [0,7,2,8,9,3,5,4,0],
    [0,8,0,2,0,0,3,7,4],
    [0,0,4,0,0,0,1,9,5],
    [0,0,0,0,5,0,6,0,0]
]

board2 = [
    [0,0,0,0,9,3,7,2,0],
    [7,0,0,1,0,6,8,0,0],
    [0,0,5,0,0,0,0,9,0],
    [0,0,0,0,1,0,6,0,0],
    [9,1,0,0,0,0,0,8,0],
    [0,5,8,9,0,2,0,0,0],
    [3,9,0,6,2,4,0,7,8],
    [5,7,6,0,8,9,0,4,1],
    [0,0,2,0,0,0,0,6,3]
]

testGameSquares = generateGameSquaresFromBoard(board2)

gameSquares = createGame(testGameSquares)

def squareCreateUI(gameSquares): 
    
    for square in gameSquares:
        v = StringVar()
        entry = Entry(main, textvariable=v, justify="center",font=("Arial",16))
        entry.place(x=square.x*40, y=square.y*40, width=40, height=40)
        entry.config(highlightbackground = "black", highlightcolor= "black")
        square.setEntry(entry)

def quit_frame():
    main.destroy()
             

def solve_sudoku():
    solve(gameSquares)


#mainprogramm
main = Tk()
main.geometry("500x540")
main.resizable(width=0, height=0)

label=Label(main, text="Sudoku Bruteforce Solver")
label["font"]="Arial"
label.place(x=150,y=0)

button1=Button(main, text="quit", command = quit_frame)
button1.place(x=50,y=450)


button2=Button(main, text="Solve", command = solve_sudoku)
button2.place(x=150,y=450)

squareCreateUI(testGameSquares)
main.mainloop()