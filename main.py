from character import Character
from coin import Coins
from ghost import Ghost
from pacman import Pacman
import os
import random

# colors
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'

os.system("clear") # clears terminal upon execution
gameBoard = []
score = 0

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
pac = Pacman("Pacman", "male", 70, "<", 0) # pacman
blinky = Ghost("Blinky", "chaser", "red", random.randint(21, 40), "m", 0) # blinky/red ghost
pinky = Ghost("Pinky", "ambusher", "pink", random.randint(1, 20), "m", 0) # pinky/pink ghost

coin_list = []
for i in range(81, 101, 1): # creates 20 coins on lower lines
    coin_clone = Coins(i, "o", False, "white")
    coin_list.append(coin_clone)

superCoin = Coins(True, "yellow")

# game loop
while True:
    # fills board with '-' before being updated with object placement
    for i in range (0, 140, 1):
        gameBoard.insert(i, "-")

    # place objects on gameboard
    for coin in coin_list: # coins display
        gameBoard[coin.position] = coin.sprite
    gameBoard[pac.position] = pac.sprite # pacman displayed on board
    gameBoard[blinky.position] = blinky.sprite # blinky displayed on board
    gameBoard[pinky.position] = pinky.sprite # pinky displayed on board

    # displays board
    print(f"Score: {score}")
    gameBoardDisplay = ''.join(gameBoard) # removes brackets and commas
    for i in range(1, 140, 20):
        print(gameBoardDisplay[-19+i:0+i])

    # user input, add w and s for up and down to jump levels later
    directionalInput = input("Input [w] = up, [s] = down, [a] = left, [d] = right: ").lower()
    if directionalInput == "a":
        pac.sprite = ">"
        pac.position -= 1
        blinky.move(pac.position)
        pinky.move(pac.position)
    elif directionalInput == "d":
        pac.sprite = "<"
        pac.position += 1
        blinky.move(pac.position)
        pinky.move(pac.position)
    elif directionalInput == "w":
        pac.position -= 20
        blinky.move(pac.position)
        pinky.move(pac.position)
    elif directionalInput == "s":
        pac.position +=20
        blinky.move(pac.position)
        pinky.move(pac.position)
    else:
        print("Please enter a valid input")

    os.system("clear")



