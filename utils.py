from random import randint


def check_bounds(x, y, width, height):
    if x < 0 or y < 0 or x >= width or y >= height:
        return False
    return True


def random_bool(cutoff, max_value):
    return randint(0, max_value) <= cutoff


def random_cell(width, height):
    x = randint(0, width - 1)
    y = randint(0, height - 1)
    return x, y


def next_random_cell(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = randint(0, 3)
    dx, dy = moves[direction][0], moves[direction][1]
    return x + dx, y + dy
