from constants import ED, BUILD_AREA, STARTX, STARTY, STARTZ, LASTX, LASTY, LASTZ, WORLDSLICE

from gdpc import Block
from gdpc import geometry as geo

from utils import get_building_at, str_to_file

from settlements.Surface import Surface

def main():
    try:
        # str_to_file(get_building_at((-10,-60, 3), (10, -40, 20)), "simple_house")
        village = Surface("Village", (50, 50), (STARTX + 50, 30, STARTZ + 50))
        village.settle()

        
    except KeyboardInterrupt: # useful for aborting a run-away program
        print("Pressed Ctrl-C to kill program.")


# === STRUCTURE #4
# The code in here will only run if we run the file directly (not imported).
# This prevents people from accidentally running your generator.
# It is recommended to directly call a function here, because any variables
# you declare outside a function will be global.
if __name__ == '__main__':
    main()