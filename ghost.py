from character import Character

class Ghost(Character):
    def __init__(self, name, mood, coin_level=0):
        super().__init__(name, coin_level)
        self.mood = mood
        # maybe add color
        pass

    def mood_behaviour(self):
        '''
        depending on mood, modify coin level
        '''
        pass

hero = Ghost("bob", 100, "happy")
hero.eat()