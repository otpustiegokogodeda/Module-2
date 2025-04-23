import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def update_score(self, delta):
        self.score += delta


class Computer:
    def __init__(self):
        self.score = 0

    def roll_dice(self):
        return random.randint(1, 6)