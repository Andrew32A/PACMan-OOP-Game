from character import Character

class Ghost(Character):
    def __init__(self, name, mood, color, position, sprite, coin_level=0):
        super().__init__(name, coin_level, position)
        self._name = name # protected
        self._mood = mood # protected
        self.color = color # public
        self._position = position # public
        self.sprite = sprite # public
        self.__coin_level = coin_level # private, mostly because it's unused

        '''
        depending on mood, modify coin level/movement
        color: red, name: blinky, personality: chaser
        color: pink, name: pinky, personality: ambusher
        color: cyan, name: inky, personality: fickle
        color: orange, name: clyde, personality: feigned ignorance
        '''

    def __blinky_movement(self, pac_position): # private
        if (self.position - pac_position) >= 20:
            self.position -= 20
            return self.position
        elif (self.position - pac_position) <= -20:
            self.position += 20
            return self.position
        elif self.position > pac_position:
            self.position -= 1
            return self.position
        elif self.position < pac_position:
            self.position += 1
            return self.position

    def __pinky_movement(self, pac_position): # private
        if self.position > pac_position:
            self.position -= 1
            return self.position
        elif self.position < pac_position:
            self.position += 1
            return self.position

    def _move(self, pac_position): # protected
        if self.color == "red":
            self.__blinky_movement(pac_position)

        elif self.color == "pink":
            self.__pinky_movement(pac_position)

        elif self.color == "cyan":
            ...
        elif self.color == "orange":
            ...
        



if __name__ == "__main__":
    hero = Ghost("bob", 100, "happy")
    hero.eat()