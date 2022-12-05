from character import Character
from coin import Coins

class Pacman(Character): # removed inheritance for now
    def __init__(self, name, gender, position, sprite, coin_level=0):
        super().__init__(name, coin_level, position)
        self.__gender = gender # protected
        self.position = position # public
        self.sprite = sprite # public
        pass

    def _pick_up_coin(self, coin_list): # protected
       for coin in coin_list:
        if self.position == coin.position:
            self.coin_level += 10
            return coin_list.remove(coin)

    def _is_alive(self, ghost1_position, ghost2_position): # protected
        '''
        reset game after game over
        '''
        if self.position == ghost1_position:
            return True
        elif self.position == ghost2_position:
            return True
        else:
            return False

    def __gender_behaviour(self): # private because it's unused for now
        '''
        depending on gender, modify coin level
        '''
        added_coin = Coins.add_coin(100)
        pass

if __name__ == "__main__":
    hero = Pacman("bob", 100, "happy")
    hero.eat()