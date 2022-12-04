from character import Character
from coin import Coins

class Pacman(Character): # removed inheritance for now
    def __init__(self, name, gender, position, sprite, coin_level=0):
        super().__init__(name, coin_level, position)
        self.gender = gender
        self.position = position
        self.sprite = sprite
        pass

    def gender_behaviour(self):
        '''
        depending on gender, modify coin level
        '''
        added_coin = Coins.add_coin(100)
        pass

    def respawn(self):
        '''
        reset game after game over
        '''


if __name__ == "__main__":
    hero = Pacman("bob", 100, "happy")
    hero.eat()