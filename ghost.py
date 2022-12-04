from character import Character
import random

class Ghost(Character):
    def __init__(self, name, mood, speed, color, position, sprite, coin_level=0):
        super().__init__(name, coin_level, position)
        self.name = name
        self.mood = mood
        self.speed = speed
        self.color = color
        self.position = position
        self.sprite = sprite
        self.coin_level = coin_level

    def mood_behaviour(self, pac_position):
        '''
        depending on mood, modify coin level/movement
        color: red, name: blinky, personality: chaser
        color: pink, name: pinky, personality: ambusher
        color: cyan, name: inky, personality: fickle
        color: orange, name: clyde, personality: feigned ignorance
        '''
        if self.color == "red":
            # distance_between = self.position - pac_position
            if self.position > pac_position:
                self.position -= 1
                return self.position
            elif self.position < pac_position:
                self.position += 1
                return self.position
            # elif distance_between >= 1:
            #     self.position -= 1
            #     return self.position
            # elif distance_between <= 1:
            #     self.position += 1
            #     return self.position

            self.position += random.randint(1, self.speed) # modifies movement on board index from between 1 and speed
            return self.position

        elif self.color == "pink":
            if self.position > pac_position:
                self.position -= 1
                return self.position
            elif self.position < pac_position:
                self.position += 1
                return self.position

            self.position += random.randint(1, self.speed) # modifies movement on board index from between 1 and speed
            return self.position
        elif self.color == "cyan":
            ...
        elif self.color == "orange":
            ...

    def visibility(self):
        '''
        might need to change name to movement, but for now this method
        determines how the ghosts react to pacman
        '''
        ...


if __name__ == "__main__":
    hero = Ghost("bob", 100, "happy")
    hero.eat()