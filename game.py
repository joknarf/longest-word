# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
    def is_valid(self, word):
        # check word not empty
        if word == '':
            return False

        # check each letters in word is in grid
        # letters can be used only once
        grid_copy = self.grid.copy()
        for char in word:
            if char in grid_copy:
                grid_copy.remove(char)
            else:
                return False
        return True
