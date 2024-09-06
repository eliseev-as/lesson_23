from utils import random_bool, random_cell, next_random_cell, check_bounds

CELL_TYPES = "🟩🌲🌊🏥🏪🔥💧🏆🔲"


class Map():
    __border = CELL_TYPES[8]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]

    def print_map(self):
        print(self.__border * (self.width + 2))

        for row in self.cells:
            print(self.__border, end='')

            for cell in row:
                if 0 <= cell < len(CELL_TYPES):
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

        for _ in range(5):
            self.add_fire()
