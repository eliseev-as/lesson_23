import os
import time

from pynput import keyboard

from clouds import Clouds
from helicopter import Helicopter
from map import Map

TICK_SLEEP = 0.05
TREE_UPDATE = 50
CLOUDS_UPDATE = 30
FIRE_UPDATE = 100
MAP_WIDTH, MAP_HEIGHT = 30, 30
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

field = Map(MAP_WIDTH, MAP_HEIGHT)
helicopter = Helicopter(MAP_WIDTH, MAP_HEIGHT)
clouds = Clouds(MAP_WIDTH, MAP_HEIGHT)


def process_key(key):
    global helicopter
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helicopter.move(dx, dy)


listener = keyboard.Listener(
    on_press=None,
    on_release=process_key, )
listener.start()
tick = 1

while True:
    os.system('clear')

    field.process_helicopter(helicopter)
    helicopter.print_stats()
    field.print_map(helicopter, clouds)

    print("TICK", tick)
    tick += 1
    time.sleep(TICK_SLEEP)

    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRE_UPDATE == 0:
        field.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()
