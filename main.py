from constants import ED, BUILD_AREA, STARTX, STARTY, STARTZ, LASTX, LASTY, LASTZ, WORLDSLICE

from gdpc import Block
from gdpc import geometry as geo

from utils import get_building_at, str_to_file

from settlements.Surface import Surface

def main():
    try:
        centerX = (STARTX + LASTX) // 2
        centerZ = (STARTZ + LASTZ) // 2
        radius = 124
        village = Surface("Village", (centerX, 30, centerZ), 20, (centerX - radius, centerZ - radius), (centerX + radius, centerZ + radius))
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