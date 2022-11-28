from character import Character
from coin import Coins

class Pacman(Character):
    def __init__(self, name, gender, coin_level=0):
        super().__init__(name, coin_level)
        self.gender = gender
        pass

    def gender_behaviour(self):
        '''
        depending on gender, modify coin level
        '''
        added_coin = Coins.add_coin(100)
        pass

hero = Pacman("bob", 100, "happy")
hero.eat()