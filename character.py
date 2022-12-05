from coin import Coins

class Character:
    def __init__ (self, name, coin_level, position):
        self.name = name # public
        self.coin_level = coin_level # public
        self.position = position # public

    def move(self, movement_direction): # public
        """
        either calculate positioning on a grid or create a battler that fights another object
        """
        if movement_direction == "a":
            self.position -= 1
            return self.position
        elif movement_direction == "d":
            self.position += 1
            return self.position
        elif movement_direction == "w":
            self.position -= 20
            return self.position
        elif movement_direction == "s":
            self.position += 20
            return self.position

    def eat(self, enemy): # unclassified for now since this is unfinished
        if self.coin_level > enemy.coin_level:
            print(f"{self.name} ate {enemy.name}")
        else:
            print(f"{enemy.name} ate {self.name}")

    def get_coins(self): # unclassified for now since this is unfinished
        """
        method takes in instance of coin class to generate random amounts of coins
        """
        self.coin_level = Coins.add_coin(self) - Coins.subtract_coin(self) #insert coins generated from coin.py
        return self.coin_level

    def show_coins(self): # unclassified for now since this is unfinished
        """
        might be a little redundant since get_coins returns coin amount
        """
        print(self.coin_level)



if __name__ == "__main__":
    ghost1 = Character("ghosty", 20)
    print(ghost1.name)
    print(ghost1.get_coins())