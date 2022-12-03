from character import Character
from coin import Coins
from ghost import Ghost
from pacman import Pacman

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
    for i in range (0, 139, 1):
        gameBoard.insert(i, "-")

createBoard()

# game loop
while True:
    directionalInput = input("Input [a] to go left and [d] to go right: ")

    if directionalInput == "a":
        ...
    elif directionalInput == "d":
        ...
    else:
        print("Please input either [a] or [d]")


    gameBoardDisplay = ''.join(gameBoard) # removes brackets and commas
    print (gameBoardDisplay, sep=" ")

