from constants import ED, BUILD_AREA, STARTX, STARTY, STARTZ, LASTX, LASTY, LASTZ, WORLDSLICE, NO_WATER_NO_LEAVES_NP_ARR

from gdpc import Block
from gdpc import geometry as geo

from utils import get_best_starting_point

from settlements.Surface import Surface
from settlements.Underground import Underground

from random import randint

def main():
    try:
        print("Researching...")
        start_indexes = get_best_starting_point(NO_WATER_NO_LEAVES_NP_ARR)
        print(start_indexes)
        # str_to_file(get_building_at((-10,-60, 3), (10, -40, 20)), "simple_house")
        village = Surface("Village", (STARTX + start_indexes[0], 30, STARTZ + start_indexes[1]), 20, (STARTX, STARTZ), (LASTX - STARTX, LASTZ - STARTZ))
        
        rooms_width = randint(6, 9)
        rooms_walls_width = randint(2, 4)
        walls_width = randint(2, 4)
        floors_height = randint(4, 6)
        nbfloors = randint(3, 4)
        temple = Underground("Temple", village, rooms_width, rooms_walls_width, walls_width, floors_height, nbfloors)

        village.settle()
        temple.settle()
        

    except KeyboardInterrupt: # useful for aborting a run-away program
        print("Pressed Ctrl-C to kill program.")

# === STRUCTURE #4
# The code in here will only run if we run the file directly (not imported).
# This prevents people from accidentally running your generator.
# It is recommended to directly call a function here, because any variables
# you declare outside a function will be global.
if __name__ == '__main__':
    main()