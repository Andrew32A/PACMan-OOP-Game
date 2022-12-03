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



# instantiate objects
pac = Pacman("Pacman", "male", 70, "<", 0)




# game loop
while True:
    # fills board with - before being updated with object placement
    for i in range (0, 140, 1):
        gameBoard.insert(i, "-")

    # place objects on gameboard
    gameBoard[pac.position] = pac.sprite # pacman displayed on board

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
    directionalInput = input("Input [w] = up, [s] = down, [a] = left, [d] = right: ").lower()
    if directionalInput == "a":
        pac.position -= 1
    elif directionalInput == "d":
        pac.position += 1
    elif directionalInput == "w":
        pac.position -= 20
    elif directionalInput == "s":
        pac.position +=20
    
    else:
        print("Please enter a valid input")

    os.system("clear")



