from coin import Coins

class Character:
    def __init__ (self, name, coin_level):
        self.name = name
        self.coin_level = coin_level

    def move(self):
        """
        either calculate positioning on a grid or create a battler that fights another object
        """
        pass

    def eat(self, enemy):
        if self.coin_level > enemy.coin_level:
            print(f"{self.name} ate {enemy.name}")
        else:
            print(f"{enemy.name} ate {self.name}")

    def get_coins(self):
        """
        method takes in instance of coin class to generate random amounts of coins
        """
        self.coin_level = Coins.add_coin(self) - Coins.subtract_coin(self) #insert coins generated from coin.py
        return self.coin_level

    def show_coins(self):
        """
        might be a little redundant since get_coins returns coin amount
        """
        return self.coin_level



if __name__ == "__main__":
    ghost1 = Character("ghosty", 20)
    print(ghost1.name)
    print(ghost1.get_coins())