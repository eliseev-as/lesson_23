from map import CELL_TYPES
from utils import random_cell


class Helicopter:
    __tank = CELL_TYPES[7]
    __score = CELL_TYPES[8]

    def __init__(self, width, height):
        rc = random_cell(width, height)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.width = width
        self.height = height
        self.tank = 0
        self.max_tank = 1
        self.score = 0

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if 0 <= nx < self.height and 0 <= ny < self.width:
            self.x, self.y = nx, ny

    def print_stats(self):
        print(self.__tank, self.tank, '/', self.max_tank, sep='', end=' | ')
        print(self.__score, self.score)
