import random

class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def roll_dice(self) -> int:
        return random.randint(1, 6)

    def update_score(self, diff: int):
        self.score += diff


class Computer:
    def __init__(self):
        self.name = "Компьютер"

    def roll_dice(self) -> int:
        return random.randint(1, 6)