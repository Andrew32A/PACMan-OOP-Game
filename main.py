from coin import Coins
from ghost import Ghost
from pacman import Pacman
import os
import random

# colors for later that we can tie into the color attribute to make things look pretty
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'

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
pac = Pacman("Pacman", "male", 70, "<", 0) # pacman
blinky = Ghost("Blinky", "chaser", "red", random.randint(21, 40), "m", 0) # blinky/red ghost
pinky = Ghost("Pinky", "ambusher", "pink", random.randint(1, 20), "m", 0) # pinky/pink ghost

coin_list = []
for i in range(84, 99, 1): # creates 20 coins on lower lines
    coin_clone = Coins(i, "o", False, "white")
    coin_list.append(coin_clone)

superCoin = Coins(True, "yellow")

# helper function to DRY code
def ghost_display():
    blinky._move(pac.position)
    pinky._move(pac.position)

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
    print(f"Score: {pac.coin_level}")
    gameBoardDisplay = ''.join(gameBoard) # removes brackets and commas
    for i in range(1, 140, 20):
        print(gameBoardDisplay[-19+i:0+i])

    # user input, add w and s for up and down to jump levels later
    directionalInput = input("Input [w] = up, [s] = down, [a] = left, [d] = right: ").lower()
    if directionalInput == "a":
        pac.sprite = ">"
        pac.move(directionalInput)
        ghost_display()
    elif directionalInput == "d":
        pac.sprite = "<"
        pac.move(directionalInput)
        ghost_display()
    elif directionalInput == "w":
        pac.move(directionalInput)
        ghost_display()
    elif directionalInput == "s":
        pac.move(directionalInput)
        ghost_display()
    else:
        print("Please enter a valid input")

    # checks if pacman collides with ghost, ends game if true
    if (pac._is_alive(blinky.position, pinky.position)):
        os.system("clear")
        gameBoard = f"""
        ---------- Game over ----------\n
        Your final score: {pac.coin_level}
        """
        print(gameBoard)
        break

    # checks if pacman collides with a coin, delete the coin and add to pac's score
    pac._pick_up_coin(coin_list)
        

    os.system("clear")



