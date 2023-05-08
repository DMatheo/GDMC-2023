from constants import ED, BUILD_AREA, STARTX, STARTY, STARTZ, LASTX, LASTY, LASTZ, WORLDSLICE

from gdpc import Block
from gdpc import geometry as geo

from utils import get_building_at, str_to_file

from buildings.Small_house import Small_house

def place_block():
    ED.placeBlock((0,100,0), Block("red_concrete"))

def get_most_frequent_wood():
    heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
    log_type = {}
    x = STARTX
    for height in heights:
        z = STARTZ
        for y in height:
            id = ED.getBlock((x, y-1, z)).id
            if "log" in id:
                log = id[10:-4]
                if log not in log_type:
                    log_type[log] = 1
                else :
                    log_type[log] += 1
            z += 1
        x += 1
    return max(log_type, key=log_type.get)

def build_cube(block_type):
    geo.placeCuboid(ED, (STARTX, 100, STARTZ), (STARTX + 7, 107, STARTZ + 7), Block(block_type))

def remove_cube():
    geo.placeCuboid(ED, (STARTX, 100, STARTZ), (STARTX + 7, 107, STARTZ + 7), Block("air"))

def place_special_blocks():
    ED.placeBlock((STARTX, 108, STARTZ), Block("chest", data='{Items: [{Slot: 5b, id: "apple", Count: 3b}]}'))
    ED.placeBlock((STARTX + 1, 108, STARTZ), Block("oak_sign", {"rotation": "8"}, data="{Text1: '{\"text\": \"Test\"}'}"))
    ED.placeBlock((STARTX + 2, 108, STARTZ), Block("lectern"))
    ED.placeBlock((STARTX + 3, 108, STARTZ), Block("oak_door"))

def clear_area():
    geo.placeCuboid(ED, (STARTX, 70, STARTZ), (STARTX + 60, 120, STARTZ + 60), Block("air"))

def main():
    try:
        # str_to_file(get_building_at((-10,-60, 3), (10, -40, 20)), "simple_house")
        clear_area()
        house = Small_house((STARTX + 0, STARTY + 75, STARTZ + 0), 'jungle', 'north')
        house.build()
        house = Small_house((STARTX + 25, STARTY + 75, STARTZ + 0), 'jungle', 'south')
        house.build()
        house = Small_house((STARTX + 0, STARTY + 75, STARTZ + 25), 'jungle', 'east')
        house.build()
        house = Small_house((STARTX + 25, STARTY + 75, STARTZ + 25), 'jungle', 'west')
        house.build()
        print("Done!")

    except KeyboardInterrupt: # useful for aborting a run-away program
        print("Pressed Ctrl-C to kill program.")


# === STRUCTURE #4
# The code in here will only run if we run the file directly (not imported).
# This prevents people from accidentally running your generator.
# It is recommended to directly call a function here, because any variables
# you declare outside a function will be global.
if __name__ == '__main__':
    main()