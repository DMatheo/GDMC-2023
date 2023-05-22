from utils import apply_heightmap, flood_fill, setNeighbouringCaveChunks
import pandas as pd
import numpy as np
import time
from math import ceil, floor
from random import randint

class Cavemap:
    def __init__(self, ED, HEIGHTS_SURFACE, HEIGHTS_WATER, ALL_BLOCKS):
        #Get the blocks
        self.cave_map_blocks = self.__get_cave_map(HEIGHTS_SURFACE, HEIGHTS_WATER, ALL_BLOCKS)
        print("Start of get caves")
        ctime = time.time()
        #Get the caves
        self.caves = self.__get_caves(ED)
        print("End of get caves")
        print(f"Took {time.time() - ctime} seconds to run")

    def __get_caves(self, ED):

        # Flood fill
        list_of_caves = []
        blocks = set(self.cave_map_blocks[['x','y','z']].to_records(index=False).tolist())
        while len(blocks) > 0:
            #Flood fill
            blocks, blocks_in_singular_cave = flood_fill(blocks, ED, *next(iter(blocks)))
            list_of_caves.append(Cave(blocks_in_singular_cave))
        list_of_caves.sort()
        return list_of_caves

    def get_best_theorical_cave(self):
        return self.caves[0]

    def __get_cave_map(self, HEIGHTS_SURFACE, HEIGHTS_WATER, ALL_BLOCKS):
        """
        This function returns a dataframe containing all the blocks contained inside a cave in the world slice
        (This function won't return the blocks forming the cave, but the blocks inside the cave, such as air, water, stalactites, etc..)

        :rtype: pd.DataFrame
        :return: The dataframe containing all the caves in the world slice
        """
        # Calculating the cavemap
        # Logic : all_blocks - blocks_above_height_in_heightmap - solid_blocks 
        # (solid being FULL blocks, so stalactites, stalagmites, etc.. arent solid.)

        #Compare two different dataframes (here, HEIGHTS and HEIGHTS_WATER) and return a dataframe with the lowest value for each cell
        HEIGHTS = HEIGHTS_SURFACE.where(HEIGHTS_SURFACE < HEIGHTS_WATER, HEIGHTS_WATER)

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

    def get_blocks(self):
        return self.cave_map_blocks
    

    def get_caves(self):
        return self.caves


class Cave:
    def __init__(self, blocks):
        # numpy array of tuple into two dimensional numpy array

        self.all_blocks_for_cave = np.array([np.array(block) for block in blocks])
        self.nb_blocks = len(blocks)
        self.cavechunks = self.__make_cave_chunks()
        self.nb_cave_chunks = len(self.cavechunks)
        self.potential = self.nb_blocks / self.nb_cave_chunks
        print("A cave has been initialized.")

    def __lt__(self, other):
        return self.potential > other.potential

    def __make_cave_chunks(self):
        # Split the cave into 10x10x10 cubes
        split_distance = 11
        
        #Getting the min of the cave, rounded down to the nearest multiple of 10
        min_x = split_distance * floor(self.all_blocks_for_cave[:,0].min()/split_distance)
        min_y = split_distance * floor(self.all_blocks_for_cave[:,1].min()/split_distance)
        min_z = split_distance * floor(self.all_blocks_for_cave[:,2].min()/split_distance)
        print(min_x, min_y, min_z)
        #Getting the max of the cave, rounded up to the nearest multiple of 10
        max_x = split_distance * ceil(self.all_blocks_for_cave[:,0].max()/split_distance)
        max_y = split_distance * ceil(self.all_blocks_for_cave[:,1].max()/split_distance)
        max_z = split_distance * ceil(self.all_blocks_for_cave[:,2].max()/split_distance)
        print(max_x, max_y, max_z)
        #Distances, rounded up to the nearest multiple of 10
        distance_x = split_distance * ceil(abs(max_x - min_x + 1)/split_distance)
        distance_y = split_distance * ceil(abs(max_y - min_y + 1)/split_distance)
        distance_z = split_distance * ceil(abs(max_z - min_z + 1)/split_distance)
        print(distance_x, distance_y, distance_z)
        print(self.all_blocks_for_cave)

        #Splitting the cave into cubes of 10x10x10
        #3 dimensional array of size distance_x/10 * distance_y/10 * distance_z/10 containing empty lists
        cave_chunks = np.empty(
            (ceil(distance_x/split_distance), 
             ceil(distance_y/split_distance), 
             ceil(distance_z/split_distance)), 
             dtype=list)

        #This if for every block in the cave, append it to the corresponding cave chunk :
        #for x,y,z in zip(self.blocks):
        #    cave_chunks[x//split_distance,y//split_distance,z//split_distance].append([x,y,z])
        #Instead, we can locate the blocks that are within the cave chunk
        #We can do this by locating theme to be within each indices, dividing by 10 the coordinates of the blocks, and rounding them down
        #Here's the code
        for x in range(0, distance_x, split_distance):
            for y in range(0, distance_y, split_distance):
                for z in range(0, distance_z, split_distance):
                    #Locating within all the blocks of the cave, the ones that are within the cave chunk
                    blocks_in_cavechunk = self.all_blocks_for_cave[
                        (self.all_blocks_for_cave[:,0] >= min_x + x) & 
                        (self.all_blocks_for_cave[:,0] <  min_x + x + split_distance) & 
                        (self.all_blocks_for_cave[:,1] >=  min_y + y) & 
                        (self.all_blocks_for_cave[:,1] <  min_y + y + split_distance) & 
                        (self.all_blocks_for_cave[:,2] >=  min_z + z) & 
                        (self.all_blocks_for_cave[:,2] <  min_z + z + split_distance)]
                    if (len(blocks_in_cavechunk) > 0):
                        cave_chunks[x//split_distance,y//split_distance,z//split_distance] = Cavechunk(blocks_in_cavechunk, split_distance)
        #Setting neighbours for each cave chunk
        setNeighbouringCaveChunks(cave_chunks, split_distance, distance_x, distance_y, distance_z)
        cave_chunks = cave_chunks.ravel()
        cave_chunks = cave_chunks[cave_chunks.astype(bool)]
        cave_chunks.sort()
        return cave_chunks

    def get_best_theorical_cavechunk(self):
        return self.cavechunks[0]

class Cavechunk:
    def __init__(self, blocks, split_distance):
        self.blocks = blocks
        self.holding_building = False
        self.neighbours = {}
        self.buildable = (len(self.blocks)/split_distance) > (1/4)
        self.possible_directions = ["north", "south", "east", "west", "up", "down"]
        self.split_distance = split_distance


    def __lt__(self, other):
        return len(self.blocks) < len(other.blocks)

    def get_buildable_informations(self):
        #I need two things now :
        #1. The lowest coordinates of the cave chunk and process them to be a multiplier of self.split_distance
        #And I know that blocks holds the coordinates of the blocks in the cave chunk in (x, y, z) format
        #2. The direction that the building should be facing

        #For #1 :
        lowest_x = self.blocks[:,0].min()
        lowest_y = self.blocks[:,1].min()
        lowest_z = self.blocks[:,2].min()
    
        #For #2 :
        taken_directions = self.takenDirections()
        possible_directions = self.getCardinalDirections()
        if len(taken_directions) == 1:
            direction = self.getOpposingCardinalDirection(taken_directions[0])
        else :
            direction = possible_directions[randint(0, len(possible_directions) - 1)] #TODO
        return (lowest_x, lowest_y, lowest_z), direction

    def update_building(self, building):
        building.build()
        self.holding_building = building
        self.buildable = False
        print(self.neighbours)
        for cavechunk in self.neighbours.values():
            cavechunk.setBuildable(False)

    def setBuildable(self, buildable):
        self.buildable = buildable

    def isBuildable(self):
        return self.buildable

    def addNeighbour(self, direction, cavechunk):
        if cavechunk is not None:
            self.neighbours[direction] = cavechunk
    
    def getNeighbours(self):
        return self.neighbours
    
    def getBoundaries(self):
        return list(set(self.possible_directions) - set(self.neighbours.keys()))
    
    def takenDirections(self):
        return set(self.neighbours.keys())

    def getCardinalDirections(self):
        return list(set(self.possible_directions) - set(self.neighbours.keys()) - set(["up", "down"]))
    
    def getOpposingCardinalDirection(self, direction):
        match direction:
            case "north":
                return "south"
            case "south":
                return "north"
            case "east":
                return "west"
            case "west":
                return "east"
            case "up":
                return "down"
            case "down":
                return "up"
            case _:
                return None
