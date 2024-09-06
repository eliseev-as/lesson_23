from utils import random_bool, random_cell, next_random_cell, check_bounds

CELL_TYPES = "🟩🌲🌊🏥🏪🔥🚁🪣🏆🔲"

TREE_BONUS = 100
UPGRADE_COST = 500


class Map():
    __border = CELL_TYPES[9]
    __helicopter = CELL_TYPES[6]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]
        self.generate_forest(3, 10)
        self.generate_river(20)
        self.generate_river(20)
        self.generate_upgrade_shop()

    def print_map(self, helicopter):
        print(self.__border * (self.width + 2))

        for ri in range(self.height):
            print(self.__border, end='')

            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if helicopter.x == ri and helicopter.y == ci:
                    print(self.__helicopter, end='')
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end='')
            print(self.__border)
        print(self.__border * (self.width + 2))

    def generate_forest(self, cutoff, max_value):
        for ri in range(self.height):
            for ci in range(self.width):
                if random_bool(cutoff, max_value):
                    self.cells[ri][ci] = 1

    def generate_tree(self):
        c = random_cell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1

    def generate_river(self, length):
        rc = random_cell(self.width, self.height)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while length > 0:
            next_rc = next_random_cell(rx, ry)
            next_x, next_y = next_rc[0], next_rc[1]
            if check_bounds(next_x, next_y, self.width, self.height):
                self.cells[next_x][next_y] = 2
                rx, ry = next_x, next_y
                length -= 1

    def generate_upgrade_shop(self):
        c = random_cell(self.width, self.height)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def add_fire(self):
        c = random_cell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def update_fires(self):
        for ri in range(self.height):
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0

        for _ in range(10):
            self.add_fire()

    def process_helicopter(self, helicopter):
        c = self.cells[helicopter.x][helicopter.y]
        if c == 2:
            helicopter.tank = helicopter.max_tank
        if c == 5 and helicopter.tank > 0:
            helicopter.tank -= 1
            helicopter.score += TREE_BONUS
            self.cells[helicopter.x][helicopter.y] = 1
        if c == 4 and helicopter.score >= UPGRADE_COST:
            helicopter.max_tank += 1
            helicopter.score -= UPGRADE_COST
