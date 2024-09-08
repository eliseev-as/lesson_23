from utils import random_bool


class Clouds:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]

    def update(self, clouds=1, max_clouds=20, clouds_lightning=1, max_clouds_lightning=10):
        for ri in range(self.height):
            for ci in range(self.width):
                if random_bool(clouds, max_clouds):
                    self.cells[ri][ci] = 1
                    if random_bool(clouds_lightning, max_clouds_lightning):
                        self.cells[ri][ci] = 2
                else:
                    self.cells[ri][ci] = 0

    def export_data(self):
        return {
            'cells': self.cells,
        }

    def import_data(self, data):
        self.cells = data['cells'] or [[0 for _ in range(self.width)] for _ in range(self.height)]
