from character import Character

class Ghost(Character):
    def __init__(self, name, mood, color, position, sprite, coin_level=0):
        super().__init__(name, coin_level, position)
        self.name = name
        self.mood = mood
        self.color = color
        self.position = position
        self.sprite = sprite
        self.coin_level = coin_level

        '''
        depending on mood, modify coin level/movement
        color: red, name: blinky, personality: chaser
        color: pink, name: pinky, personality: ambusher
        color: cyan, name: inky, personality: fickle
        color: orange, name: clyde, personality: feigned ignorance
        '''

    def blinky_movement(self, pac_position):
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

    def pinky_movement(self, pac_position):
        if self.position > pac_position:
            self.position -= 1
            return self.position
        elif self.position < pac_position:
            self.position += 1
            return self.position

    def move(self, pac_position):
        if self.color == "red":
            self.blinky_movement(pac_position)

        elif self.color == "pink":
            self.pinky_movement(pac_position)

        elif self.color == "cyan":
            ...
        elif self.color == "orange":
            ...
        



if __name__ == "__main__":
    hero = Ghost("bob", 100, "happy")
    hero.eat()