#!/usr/bin/env python3

# === STRUCTURE #1
# These are the modules (libraries) we will use in this code
# We are giving these modules shorter, but distinct, names for convenience
import pandas as pd

from gdpc import geometry as geo
from gdpc import interface

from utils import calculate_middle, calculate_world_slice_size
from constants import STARTX, STARTY, STARTZ, LASTX, LASTY, LASTZ, ED, WOOD_TYPE, BUILD_AREA, WORLDSLICE, FLOWERS, ROADHEIGHT, HEIGHTS, HEIGHTS_WATER, WORLD_MAP, ALL_BLOCKS, CAVE_MAP, ALL_BLOCKS_CAVEMAP
from buildings.BuildFile import BuildFile


# === STRUCTURE #3
# Here we are defining all of our functions to keep our code organised
# They are:

def buildCubeEasyMethod(radius):
    """Build a cube inside the whole area border.
    The size can't be bigger than the world slice's x, z

    :type radius: int
    :param radius: The radius of the cube
    """
    final_radius = min(radius, *calculate_world_slice_size())
    mid_x, mid_z = calculate_middle()
    geo.placeCuboid(ED, 
                    (mid_x - final_radius, STARTY - final_radius, mid_z - final_radius), 
                    (mid_x + final_radius, STARTY + final_radius, mid_z + final_radius),
                    WOOD_TYPE
    )

def getBiomeMap(slideX, slideZ):
    """
    This function returns a dataframe with the biomes of the world slice

    :type slideX: int
    :param slideX: The size of the world slice in X
    :type slideZ: int
    :param slideZ: The size of the world slice in Z

    :rtype: pd.DataFrame
    :return: A dataframe with the biomes of the world slice
    """
    biomes = interface.getBiomes((STARTX+slideX, STARTY, STARTZ+slideZ), (slideX, 1, slideZ), dimension=ED.dimension, retries=ED.retries, timeout=ED.timeout, host=ED.host)
    return pd.DataFrame(biomes, columns=['coordinates', 'biomeId'])
    

def build_house_underground():
    """
    This function builds a house underground
    """
    # Get the best underground sub chunk
    cavechunk = CAVE_MAP.get_best_theorical_cave().get_best_theorical_cavechunk()
    coordinates, facing = cavechunk.get_buildable_informations()
    facing = "north"
    building = BuildFile("underground_house", coordinates, facing)
    print("Starting to build...")
    print(f"Coordinates : {coordinates}")
    print(cavechunk.getBoundaries())
    print(cavechunk.takenDirections())
    print(cavechunk.get_buildable_informations())
    print(len(cavechunk.blocks))
    building.build()
    
    print("A house has been built underground !")
    print(f"Coordinates : {coordinates}")
    cavechunk.update_building(building)



def main():
    try:
        #start_settlement_underground()
        build_house_underground()
        #get_building_at(ED, (STARTX, STARTY, STARTZ), (LASTX, LASTY, LASTZ))
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