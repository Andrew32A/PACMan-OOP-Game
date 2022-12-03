from character import Character

class Ghost(Character):
    def __init__(self, name, mood, speed, color, coin_level=0):
        super().__init__(name, coin_level, speed)
        self.mood = mood
        self.speed = speed
        self.color = color

    def mood_behaviour(self):
        '''
        depending on mood, modify coin level/movement
        color: red, name: blinky, personality: chaser
        color: pink, name: pinky, personality: ambusher
        color: cyan, name: inky, personality: fickle
        color: orange, name: clyde, personality: feigned ignorance
        '''
        if self.color == "red":
            ...
        elif self.color == "pink":
            ...
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