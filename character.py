class Character:
    def __init__ (self, name, coin_level):
        self.name = name
        self.coin_level = coin_level

    def move(self):
        pass

    def eat(self):
        print("test")
        pass

    def get_coins(self):
        """
        method takes in instance of coin class to generate random amounts of coins
        """
        pass

    def show_coins(self):
        return self.coin_level