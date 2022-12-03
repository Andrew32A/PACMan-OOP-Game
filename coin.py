import random

class Coins():
    def __init__(self, isSuperCoin=False, color="yellow"):
        self.isSuperCoin = isSuperCoin
        self.color = color

    def add_coin(self):
        add_amount = random.randint(1,50)
        return add_amount

    def subtract_coin(self):
        sub_amount = random.randint(1,50)
        return sub_amount
