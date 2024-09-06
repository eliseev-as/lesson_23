import os
import time

from map import Map

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_WIDTH, MAP_HEIGHT = 30, 30

field = Map(30, 30)
field.generate_forest(3, 10)
field.generate_river(20)
field.generate_river(20)
field.print_map()

tick = 1

while True:
    os.system('clear')
    print("TICK", tick)
    field.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRE_UPDATE == 0:
        field.update_fires()
