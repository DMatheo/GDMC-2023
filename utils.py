from math import ceil

from itertools import groupby
from operator import itemgetter
import numpy as np
from gdpc import Block
import random
#Mathematical functions
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

def get_largest_sequence(list_of_y):
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

def calculate_world_slice_size(STARTX, LASTX, STARTZ, LASTZ):
    """
    Calculates the size in X and in Z.   

    :rtype: tuple
    :return: A tuple with the size in X and in Z 
    """
    return (abs(STARTX-LASTX), abs(STARTZ-LASTZ))

def calculate_middle(STARTX, LASTX, STARTZ, LASTZ):
    """
    Gets the middle point in x and z.

    :rtype: tuple
    :return: A tuple with the middle point in x and z
    """
    return ( ceil((STARTX+LASTX)/2), ceil((STARTZ + LASTZ)/2) )


def flood_fill(blocks_init, ED, startx, starty, startz):
    stack = set([(startx, starty, startz)])
    blocks = blocks_init
    cave = set()
    #leblock = random.choice(["minecraft:cyan_wool", "minecraft:blue_wool", "minecraft:light_blue_wool", "minecraft:lime_wool", "minecraft:green_wool", "minecraft:yellow_wool", "minecraft:orange_wool", "minecraft:red_wool", "minecraft:magenta_wool", "minecraft:purple_wool", "minecraft:pink_wool", "minecraft:white_wool", "minecraft:light_gray_wool", "minecraft:gray_wool", "minecraft:black_wool"])
    while len(stack) != 0:
        for _ in range(len(stack)):
            point = stack.pop()
            blocks.remove(point)
            cave.add(point)
            x,y,z = point
            #ED.placeBlock((x, y, z), Block(leblock))
            for neighbour in neighbours(x, y, z):
                if neighbour in blocks and neighbour not in cave and neighbour not in stack:
                    stack.add(neighbour)
    return blocks, cave

def neighbours(x, y, z):
    return [
        (x+1, y, z), 
        (x-1, y, z), 
        (x, y+1, z), 
        (x, y-1, z), 
        (x, y, z+1), 
        (x, y, z-1)
    ]

def setNeighbouringCaveChunks(cave_chunks, split_distance, distance_x, distance_y, distance_z):
    for x in range(0, distance_x, split_distance):
        for y in range(0, distance_y, split_distance):
            for z in range(0, distance_z, split_distance):
                cave_chunk = cave_chunks[x//split_distance,y//split_distance,z//split_distance]
                if cave_chunk is not None:
                    if x//split_distance > 0:
                        cave_chunk.addNeighbour("west",cave_chunks[x//split_distance-1,y//split_distance,z//split_distance])
                    if x//split_distance < cave_chunks.shape[0]-1:
                        cave_chunk.addNeighbour("east", cave_chunks[x//split_distance+1,y//split_distance,z//split_distance])
                    if y//split_distance > 0:
                        cave_chunk.addNeighbour("down", cave_chunks[x//split_distance,y//split_distance-1,z//split_distance])
                    if y//split_distance < cave_chunks.shape[1]-1:
                        cave_chunk.addNeighbour("up", cave_chunks[x//split_distance,y//split_distance+1,z//split_distance])
                    if z//split_distance > 0:
                        cave_chunk.addNeighbour("north", cave_chunks[x//split_distance,y//split_distance,z//split_distance-1])
                    if z//split_distance < cave_chunks.shape[2]-1:
                        cave_chunk.addNeighbour("south", cave_chunks[x//split_distance,y//split_distance,z//split_distance+1])