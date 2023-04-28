#!/usr/bin/env python3

# === STRUCTURE #1
# These are the modules (libraries) we will use in this code
# We are giving these modules shorter, but distinct, names for convenience

import numpy as np
import pandas as pd

from math import ceil
from random import randint
from itertools import groupby
from operator import itemgetter

from gdpc import Block
from gdpc import geometry as geo
from gdpc import minecraft_tools as mt
from gdpc import editor_tools as et
from gdpc import interface

from constants import STARTX, STARTY, STARTZ, LASTX, LASTY, LASTZ, WORLDSLICE, ED, HEIGHTS, ALL_BLOCKS



# === STRUCTURE #3
# Here we are defining all of our functions to keep our code organised
# They are:
# - placeFurniture()
# - buildCubeHarderMethod()
# - buildCubeEasierMethod()

def placeFurniture():
    """
    This function places a bed, a crafting table and a furnace
    in the top middle of the build area.
    """
    mid_x, mid_z = calculateMiddle()
    final_radius = min(8, *calculateWorldSliceSize())
    ED.placeBlock((mid_x, STARTY + final_radius+1, mid_z), Block(f"birch_door", {"facing": "north"}))
    sign_data = mt.signData(line1="hOi", line2="and this is...", line3="BOB ! or not", line4="UNDERTALE")
    ED.placeBlock(
        (mid_x+1, STARTY + final_radius+1, mid_z), 
        Block(
            f"{getBiomeWoodType()}_sign", 
            {"rotation": 0}, 
            data=sign_data
        )
    )    
    ED.placeBlock(
        (mid_x+2, STARTY + final_radius+1, mid_z), 
        Block(
            f"minecraft:chest", 
            {"facing": "south", "type":"left"}, 
            data='{Items: [\
                        {id:"minecraft:dirt",Count:1b,Slot:0b},\
                        {id: "minecraft:acacia_door",Count:13b,Slot:1b},\
                        {id:"minecraft:iron_bars",Count:64b,Slot:2b},\
                        {id:"minecraft:lantern",Count:3b,Slot:14b},\
                        {id:"minecraft:spruce_fence",Count:1b,Slot:26b}\
                    ]\
            }'
        )
    )
    et.placeContainerBlock(ED, (mid_x+3, STARTY+final_radius+1, mid_z), Block("minecraft:chest"), [((3,1), "wheat")])
    book_data = mt.bookData(
        "This is a book.\nAnd I love it !",
        "My book", 
        "ShinryuSHH", 
        "The story", 
        "blue")
    et.placeLectern(ED, (mid_x+4, STARTY+final_radius+1, mid_z), "north", book_data)


def buildCubeHarderMethod(radius):
    """
    This function builds a cube of radius radius

    :type radius: int
    :param radius: Radius of the cube
    """

    chosen_wood_type=getBiomeWoodType()
    chosen_wood_type=getBiomeWoodTypeDifferent()
    final_radius = min(radius, *calculateWorldSliceSize())
    mid_x, mid_z = calculateMiddle()
    geo.placeCuboid(ED, 
                    (mid_x - final_radius, STARTY - final_radius, mid_z - final_radius), 
                    (mid_x + final_radius, STARTY + final_radius, mid_z + final_radius),
                    Block(chosen_wood_type+"_wood")
    )

def getBiomeWoodType():
    """
    This function returns the wood type of the biome

    :rtype: str
    :return: The wood type of the biome
    """
    heights = pd.DataFrame(WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"])
    heights.apply(heightMapRowToBlockMapRow)
    blocks_count = pd.DataFrame(pd.Series(heights.values.ravel()).value_counts()).reset_index()
    blocks_count.columns = ['block', 'amount']
    logs_in_height_map = blocks_count[blocks_count['block'].str.contains('log')]
    chosen_block = Block("minecraft:stone")
    if len(logs_in_height_map) > 0:
        chosen_block = logs_in_height_map['block'].iloc[0].replace('_log', '')

    if (type(chosen_block) != str):
        chosen_block = chosen_block.id
    return chosen_block.split(':')[1]

def buildHouseInCave():
    """
    This function builds a house in a cave
    """
    #Get largest caves
    largest_caves, largest_possible_cave = getLargestCaves()
    if (largest_caves is None or largest_possible_cave is None):
        print("No caves found !")
        return
    
    


def getLargestCaves():
    """
    This function returns a dataframe containing all the largest caves in the world slice, 
    aswell as Series containing the coordinates of the largest cave

    :rtype: pd.DataFrame, pd.Series
    :return: The dataframe containing all the largest caves in the world slice,
    aswell as Series containing the coordinates of the largest cave
    """

    cavemap = getCaveMap()
    cavemap.drop(['Name'], inplace=True, axis=1)

    # Changing the column and rows to current x and z, stocking y in lists for each coordinate
    underground_sequences = cavemap.groupby(['x', 'z'])['y'].apply(list).reset_index()
    # Now, for each value of y, I'll apply the largest sequence in a given list of number :
    underground_sequences['y'] = underground_sequences['y'].apply(getLargestSequence)
    # Now, I'll add a column with the length of the sequences, for later use
    underground_sequences['Length_of_sequence'] = underground_sequences['y'].str.len()

    # Should return :
    # - 2D map with biggest cave spotted, with top Y and bottom Y, for every X & Z
    # - Row with the largest cave
    return underground_sequences, underground_sequences.loc[underground_sequences['Length_of_sequence'].idxmax()]

def getLargestSequence(list_of_y):
    """
    This function returns the largest sequence of numbers in a list of numbers
    Credits to 
    https://stackoverflow.com/questions/60965915/python-program-program-to-find-largest-sequence-in-a-given-list-of-numbers

    :type list_of_y: pd.Series
    :param list_of_y: List of Y coordinates
    """
    new_l = []
    for k, g in groupby(enumerate(list_of_y), lambda ix : ix[0] - ix[1]):
        new_l.append(list(map(itemgetter(1), g)))
    return max(new_l, key=lambda x: len(x))

def getCaveMap():
    """
    This function returns a dataframe containing all the blocks contained inside a cave in the world slice
    (This function won't return the blocks forming the cave, but the blocks inside the cave, such as air, water, stalactites, etc..)

    :rtype: pd.DataFrame
    :return: The dataframe containing all the caves in the world slice
    """
    # Calculating the cavemap
    # Logic : all_blocks - blocks_above_height_in_heightmap - solid_blocks 
    # (solid being FULL blocks, so stalactites, stalagmites, etc.. arent solid.)

    # Getting a dictionnary of the heightmap for faster access
    height_dict = pd.DataFrame.to_dict(HEIGHTS, orient='index')

    # Getting the numpy values of each cell
    all_blocks_array = ALL_BLOCKS.values

    # Initialize holder so it is faster to define
    updated_array = np.zeros_like(all_blocks_array)

    # Apply heightmap on each row
    # Costly...
    for i, row in enumerate(all_blocks_array):
        updated_array[i] = apply_heightmap(row, height_dict)

    # Get back the dataframe    
    all_blocks_updated = pd.DataFrame(updated_array, columns=ALL_BLOCKS.columns.values).dropna()

    # Only get cave blocks
    list_of_cave_blocks = ["minecraft:air", "minecraft:cave_air","minecraft:brown_mushroom", "minecraft:red_mushroom", "minecraft:water",
    "minecraft:lava", "minecraft:cobweb", "minecraft:glow_lichen", "minecraft:chain", "minecraft:vine", "minecraft:grass", "minecraft:spore_blossom",
    "minecraft:small_dripleaf", "minecraft:moss_carpet", "minecraft:hanging_roots", "minecraft:big_dripleaf", "minecraft:tall_grass", "minecraft:large_fen",
    "minecraft:pointed_dripstone"]

    final_result = all_blocks_updated[all_blocks_updated['Name'].isin(list_of_cave_blocks)]

    return final_result

def apply_heightmap(row, heightmap_dict):
    """
    This function returns the row if the block is below the heightmap, else it returns None

    :type row: pd.Series
    :param row: The row to check
    """

    x, y, z, name = row 
    if heightmap_dict[x][z] > y:
        return row
    return None

def getBiomeWoodTypeDifferent():
    """
    This function returns the wood type of the most common tree in the world slice
    This is a second function, as the first one uses the biomes, and this one uses all actual blocks

    :rtype: str
    :return: The wood type of the most common tree in the world slice (OAK, etc..)
    """

    blocks_count = pd.DataFrame(pd.Series(ALL_BLOCKS.values.ravel()).value_counts()).reset_index()
    blocks_count.columns = ['block', 'amount']
    logs_in_height_map = blocks_count[blocks_count['block'].str.contains('log')]

    # Default block is stone
    chosen_block = Block("minecraft:stone")

    # If there are logs in the height map, we take the first one
    #TODO : There can be blocks that are not logs apparently, have to fix that
    if len(logs_in_height_map) > 0:
        chosen_block = logs_in_height_map['block'].iloc[0].replace('_log', '')
    if (type(chosen_block) != str):
        chosen_block = chosen_block.id
    return chosen_block.split(':')[1]

def heightMapRowToBlockMapRow(row):
    """
    This function returns a row of the block map, from a row of the height map

    :type row: pd.Series
    :param row: The row to convert
    """

    for i in range(0, len(row)):
        row[i] = {'x':STARTX+i, 
                  'y':row[i], 
                  'z':STARTZ+row.name,
                  'block':ED.getBlock((STARTX+i, row[i], STARTZ+row.name)).id
                  }
    
    return row[i]

def buildCubeEasyMethod(radius):
    """Build a cube inside the whole area border.
    The size can't be bigger than the world slice's x, z

    :type radius: int
    :param radius: The radius of the cube
    """
    final_radius = min(radius, *calculateWorldSliceSize())
    mid_x, mid_z = calculateMiddle()
    geo.placeCuboid(ED, 
                    (mid_x - final_radius, STARTY - final_radius, mid_z - final_radius), 
                    (mid_x + final_radius, STARTY + final_radius, mid_z + final_radius),
                    mostCommonWoodType(*calculateWorldSliceSize())
    )

def mostCommonWoodType(*slice_sizes):
    """
    This function returns the most common wood type in the world slice

    :type slice_sizes: tuple
    :param slice_sizes: The size of the world slice (in X and Z)
    """

    block = Block("minecraft:stone")
    biomes = getBiomeMap(*slice_sizes)
    most_common_biome = biomes["biomeId"].mode()[0]

    if "savanna" in most_common_biome:
        block = Block("minecraft:acacia_wood")
    elif "jungle" in most_common_biome:
        block = Block("minecraft:jungle_wood")
    elif "birch" in most_common_biome:
        block = Block("minecraft:birch_wood")
    elif "dark" in most_common_biome:
        block = Block("minecraft:dark_oak_wood")
    elif "mangrove" in most_common_biome:
        block = Block("minecraft:mangrove_wood")
    elif "warm" in most_common_biome:
        block = Block(f"minecraft:dead_horn_coral_block")
    elif "mushroom_field" in most_common_biome:
        blockName = ["brown_mushroom_block", "red_mushroom_block", "mushroom_stem"][randint(0,2)]
        block = Block(f"minecraft:{blockName}")
    elif most_common_biome == "minecraft:deep_dark":
        block = Block("minecraft:sculk")
    elif most_common_biome == "minecraft:lush_caves":
        block = Block("minecraft:moss_block")
    elif any(b in most_common_biome for b in ["spruce", "taiga", "grove", "tundra", "pine", "snowy_plains"]):
        block = Block("minecraft:spruce_wood")
    elif any(b in most_common_biome for b in ["beach", "desert"]):
        block = Block("minecraft:sandstone")
    elif any(b in most_common_biome for b in ["frozen", "cold", "snowy"]):
        block = Block("minecraft:blue_ice")
    elif most_common_biome == "minecraft:forest" or any(b in most_common_biome for b in ["badlands", "meadow", "swamp", "windswept", "wooded", "plains" ]):
        block = Block("minecraft:oak_wood")
            

    return block

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
    

def calculateWorldSliceSize():
    """
    Calculates the size in X and in Z.   

    :rtype: tuple
    :return: A tuple with the size in X and in Z 
    """
    return (abs(STARTX-LASTX), abs(STARTZ-LASTZ))

def calculateMiddle():
    """
    Gets the middle point in x and z.

    :rtype: tuple
    :return: A tuple with the middle point in x and z
    """
    return ( ceil((STARTX+LASTX)/2), ceil((STARTZ + LASTZ)/2) )

def buildPerimeter():
    """
    Build a wall along the build area border.
    In this function we're building a simple wall around the build area
    pillar-by-pillar, which means we can adjust to the terrain height
    """
    # HEIGHTMAP
    # Heightmaps are an easy way to get the uppermost block at any coordinate
    # There are four types available in a world slice:
    # - 'WORLD_SURFACE': The top non-air blocks
    # - 'MOTION_BLOCKING': The top blocks with a hitbox or fluid
    # - 'MOTION_BLOCKING_NO_LEAVES': Like MOTION_BLOCKING but ignoring leaves
    # - 'OCEAN_FLOOR': The top solid blocks
    heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

    print("Building east-west walls...")

    for x in range(STARTX, LASTX + 1):
        # The northern wall
        y = heights[(x - STARTX, 0)]
        geo.placeCuboid(ED, (x, y - 2, STARTZ), (x, y, STARTZ), Block("granite"))
        geo.placeCuboid(ED, (x, y + 1, STARTZ), (x, y + 4, STARTZ), Block("granite_wall"))
        # The southern wall
        y = heights[(x - STARTX, LASTZ - STARTZ)]
        geo.placeCuboid(ED, (x, y - 2, LASTZ), (x, y, LASTZ), Block("red_sandstone"))
        geo.placeCuboid(ED, (x, y + 1, LASTZ), (x, y + 4, LASTZ), Block("red_sandstone_wall"))

    print("Building north-south walls...")

    for z in range(STARTZ, LASTZ + 1):
        # The western wall
        y = heights[(0, z - STARTZ)]
        geo.placeCuboid(ED, (STARTX, y - 2, z), (STARTX, y, z), Block("sandstone"))
        geo.placeCuboid(ED, (STARTX, y + 1, z), (STARTX, y + 4, z), Block("sandstone_wall"))
        # The eastern wall
        y = heights[(LASTX - STARTX, z - STARTZ)]
        geo.placeCuboid(ED, (LASTX, y - 2, z), (LASTX, y, z), Block("prismarine"))
        geo.placeCuboid(ED, (LASTX, y + 1, z), (LASTX, y + 4, z), Block("prismarine_wall"))


def buildRoads():
    """Build a road from north to south and east to west."""
    xaxis = STARTX + (LASTX - STARTX) // 2  # Getting start + half the length
    zaxis = STARTZ + (LASTZ - STARTZ) // 2
    heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

    print("Calculating road height...")
    # Caclulating the average height along where we want to build our road
    y = heights[(xaxis - STARTX, zaxis - STARTZ)]
    for x in range(STARTX, LASTX + 1):
        newy = heights[(x - STARTX, zaxis - STARTZ)]
        y = (y + newy) // 2
    for z in range(STARTZ, LASTZ + 1):
        newy = heights[(xaxis - STARTX, z - STARTZ)]
        y = (y + newy) // 2

    # GLOBAL
    # By calling 'global ROADHEIGHT' we allow writing to ROADHEIGHT.
    # If 'global' is not called, a new, local variable is created.
    global ROADHEIGHT
    ROADHEIGHT = y

    print("Building east-west road...")

    geo.placeCuboid(ED, (xaxis - 2, y, STARTZ), (xaxis - 2, y, LASTZ), Block("end_stone_bricks"))
    geo.placeCuboid(ED, (xaxis - 1, y, STARTZ), (xaxis + 1, y, LASTZ), Block("gold_block"))
    geo.placeCuboid(ED, (xaxis + 2, y, STARTZ), (xaxis + 2, y, LASTZ), Block("end_stone_bricks"))
    geo.placeCuboid(ED, (xaxis - 1, y + 1, STARTZ), (xaxis + 1, y + 3, LASTZ), Block("air"))

    print("Building north-south road...")

    geo.placeCuboid(ED, (STARTX, y, zaxis - 2), (LASTX, y, zaxis - 2), Block("end_stone_bricks"))
    geo.placeCuboid(ED, (STARTX, y, zaxis - 1), (LASTX, y, zaxis + 1), Block("gold_block"))
    geo.placeCuboid(ED, (STARTX, y, zaxis + 2), (LASTX, y, zaxis + 2), Block("end_stone_bricks"))
    geo.placeCuboid(ED, (STARTX, y + 1, zaxis - 1), (LASTX, y + 3, zaxis + 1), Block("air"))


def buildCity():
    xaxis = STARTX + (LASTX - STARTX) // 2  # Getting center
    zaxis = STARTZ + (LASTZ - STARTZ) // 2
    y = ROADHEIGHT

    print("Building city platform...")
    # Building a platform and clearing a dome for the city to sit in
    geo.placeCylinder(ED, (xaxis, y,      zaxis), 39, 1, Block("end_stone_bricks"))
    geo.placeCylinder(ED, (xaxis, y,      zaxis), 37, 1, Block("gold_block"))
    geo.placeCylinder(ED, (xaxis, y +  1, zaxis), 37, 3, Block("air"))
    geo.placeCylinder(ED, (xaxis, y +  4, zaxis), 35, 2, Block("air"))
    geo.placeCylinder(ED, (xaxis, y +  6, zaxis), 33, 1, Block("air"))
    geo.placeCylinder(ED, (xaxis, y +  7, zaxis), 32, 1, Block("air"))
    geo.placeCylinder(ED, (xaxis, y +  8, zaxis), 27, 1, Block("air"))
    geo.placeCylinder(ED, (xaxis, y +  9, zaxis), 21, 1, Block("air"))
    geo.placeCylinder(ED, (xaxis, y + 10, zaxis), 13, 1, Block("air"))
    geo.placeCylinder(ED, (xaxis, y + 11, zaxis),  3, 1, Block("air"))

    for _ in range(50):
        buildTower(randint(xaxis - 20, xaxis + 20),
                   randint(zaxis - 20, zaxis + 20))

    # Place a book on a Lectern.
    # See the wiki for book formatting codes.
    ED.placeBlock((xaxis, y, zaxis), Block("emerald_block"))
    bookData = mt.bookData("This book has a page!")
    et.placeLectern(ED, (xaxis, y + 1, zaxis), bookData=bookData)


def buildTower(x, z):
    radius = 3
    diameter = 2*radius + 1
    y = ROADHEIGHT

    print(f"Building tower at {x}, {z}...")
    # If the blocks to the north, south, east and west aren't all gold
    if not (
            ED.getBlock((x - radius, y, z)).id == "minecraft:gold_block"
        and ED.getBlock((x + radius, y, z)).id == "minecraft:gold_block"
        and ED.getBlock((x, y, z - radius)).id == "minecraft:gold_block"
        and ED.getBlock((x, y, z + radius)).id == "minecraft:gold_block"
    ):
        return  # Return without building anything

    # Lay the foundation
    geo.placeCylinder(ED, (x, y, z), diameter, 1, Block("emerald_block"))

    # Build ground floor
    geo.placeCylinder(ED, (x, y + 1, z), diameter, 3, Block("lime_concrete"), tube=True)

    # Extend height
    height = randint(5, 20)
    geo.placeCylinder(ED, (x, y + 4, z), diameter, height, Block("lime_concrete"), tube=True)
    height += 4

    # Build roof
    geo.placeCylinder(ED, (x, y + height, z), diameter, 1, Block("emerald_block"))
    geo.placeCylinder(ED, (x, y + height + 1, z), diameter-2, 2, Block("emerald_block"))
    geo.placeCuboid(ED, (x, y + height, z), (x, y + height + 2, z), Block("lime_stained_glass"))
    ED.placeBlock((x, y + 1, z), Block("beacon"))

    # Trim sides and add windows and doors
    # NOTE: When placing doors, you only need to place the bottom block.
    geo.placeCuboid(ED, (x + radius, y + 1, z), (x + radius, y + height + 2, z), Block("air"))
    geo.placeCuboid(ED, (x + radius - 1, y + 1, z), (x + radius - 1, y + height + 2, z), Block("lime_stained_glass"))
    ED.placeBlock((x + radius - 1, y + 1, z), Block("warped_door", {"facing": "west"}))

    geo.placeCuboid(ED, (x - radius, y + 1, z), (x - radius, y + height + 2, z), Block("air"))
    geo.placeCuboid(ED, (x - radius + 1, y + 1, z), (x - radius + 1, y + height + 2, z), Block("lime_stained_glass"))
    ED.placeBlock((x - radius + 1, y + 1, z), Block("warped_door", {"facing": "east"}))

    geo.placeCuboid(ED, (x, y + 1, z + radius), (x, y + height + 2, z + radius), Block("air"))
    geo.placeCuboid(ED, (x, y + 1, z + radius - 1), (x, y + height + 2, z + radius - 1), Block("lime_stained_glass"))
    ED.placeBlock((x, y + 1, z + radius - 1), Block("warped_door", {"facing": "north"}))

    geo.placeCuboid(ED, (x, y + 1, z - radius), (x, y + height + 2, z - radius), Block("air"))
    geo.placeCuboid(ED, (x, y + 1, z - radius + 1), (x, y + height + 2, z - radius + 1), Block("lime_stained_glass"))
    ED.placeBlock((x, y + 1, z - radius + 1), Block("warped_door", {"facing": "south"}))


def get_building_at(coord_start, coord_end):

    startx, starty, startz = coord_start
    maxx, maxy, maxz = coord_start
    blocks = ""
    # needed_ressources = {}

    for x in range(coord_start[0], coord_end[0]):

        for y in range(coord_start[1], coord_end[1]):

            for z in range(coord_start[2], coord_end[2]):

                block = ED.getBlock((x, y, z))
                block_name = block.id[10:]

                if block_name != "air":
                    if x > maxx:
                        maxx = x
                    if y > maxy:
                        maxy = y
                    if z > maxz:
                        maxz = z
                    blocks += f"(({x - startx}, {y - starty}, {z - startz}), '{block.id[10:]}', {block.states}),\n"""
                    # if block_name not in needed_ressources:
                    #     needed_ressources[block_name] = 1
                    # else :
                    #     needed_ressources[block_name] += 1
    return f"Dimensions : ({maxx - startx}, {maxy - starty}, {maxz - startz})\n\n" + blocks

def main():
    try:
        buildHouseInCave()
        #buildCubeEasyMethod(3)
        #buildCubeHarderMethod(3)
        #placeFurniture()
        
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