from character import Character
from coin import Coins
from ghost import Ghost
from pacman import Pacman
import os

os.system("clear") # clears terminal upon execution
gameBoard = []
"""
gameboard will look something like:
20 x 7

Score = (coins = 10, supercoins = 50 ghost kills = 100)

- - - - - - - - - - - - - - - - - - - -
- - - 0 o o o o o o o o o o o 0 - - - -
- - - o - - - - - - - - - - - o - - - -
- m - o - - - - - - m - - - - o - - - -
- - - o - - - - - - - - - - - o - - - -
- - - 0 o o o o - < - o o o o 0 - - - -
- - - - - - - - - - - - - - - - - - - -

- = empty space
< = pacman
o = coin
0 = supercoin
m = ghosts
"""

def createBoard():
    for i in range (0, 140, 1):
        gameBoard.insert(i, "-")
    
    gameBoard[70] = "<" # placeholder for pacman creation here

createBoard()

# game loop
while True:
    # displays board
    gameBoardDisplay = ''.join(gameBoard) # removes brackets and commas
    print(gameBoardDisplay[1:20])
    print(gameBoardDisplay[21:40])
    print(gameBoardDisplay[41:60])
    print(gameBoardDisplay[61:80])
    print(gameBoardDisplay[81:100])
    print(gameBoardDisplay[101:120])
    print(gameBoardDisplay[121:140])

    # user input, add w and s for up and down to jump levels later
    directionalInput = input("Input [a] to go left and [d] to go right: ")
    if directionalInput == "a":
        ...
    elif directionalInput == "d":
        ...
    else:
        print("Please input either [a] or [d]")

    os.system("clear")



