import json
import os
import time

from pynput import keyboard

from clouds import Clouds
from helicopter import Helicopter
from map import Map

TICK_SLEEP = 0.05
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 75
MAP_WIDTH, MAP_HEIGHT = 30, 30
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

clouds = Clouds(MAP_WIDTH, MAP_HEIGHT)
field = Map(MAP_WIDTH, MAP_HEIGHT, clouds)
helicopter = Helicopter(MAP_WIDTH, MAP_HEIGHT)
tick = 1


def process_key(key):
    global helicopter, tick, clouds, field
    c = key.char.lower()

    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helicopter.move(dx, dy)
    elif c == 'f':
        data = {
            'helicopter': helicopter.export_data(),
            'clouds': clouds.export_data(),
            'field': field.export_data(),
            "tick": tick,
        }
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    elif c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helicopter.import_data(data['helicopter'])
            field.import_data(data['field'])
            clouds.import_data(data['clouds'])


listener = keyboard.Listener(
    on_press=None,
    on_release=process_key, )
listener.start()

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
