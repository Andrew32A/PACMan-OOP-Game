import random

class Coins():
    def __init__(self, position, sprite, isSuperCoin=False, color="yellow"):
        self.position = position # public
        self.sprite = sprite # public
        self.isSuperCoin = isSuperCoin # public
        self.color = color # public

    def add_coin(self): # unclassified for now since this is unfinished
        add_amount = random.randint(1,50)
        return add_amount

    def subtract_coin(self): # unclassified for now since this is unfinished
        sub_amount = random.randint(1,50)
        return sub_amount
