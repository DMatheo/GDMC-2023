import pandas as pd
import numpy as np
from gdpc import Block

class Worldmap:
    def __init__(self, STARTX, STARTZ, WORLDSLICE, HEIGHTS):
        #Get the blocks
        self.blocks = self.__get_blocks_in_slice(STARTX, STARTZ, WORLDSLICE, HEIGHTS)

        #Get the dominant wood
        self.wood_type = self.__get_dominant_wood_type()
    
    def __get_blocks_in_slice(self, STARTX, STARTZ, WORLDSLICE, heightmap = None):
        """ 
        Gets all the blocks in the slice
        Be warned : this algorithm is costly and should only be called once.
        Note : U60 is because the longest block id in Minecraft is less than 60 characters long.

        :type heightmap: List(List(int))
        :param heightmap: List of List of top Y coordinates

        :return: Dataframe with all blocks in the current slice
        """
        data = np.fromiter(
            (( ((STARTX // 16) + key.x) * 16 + i % 16, key.y * 16 + (i // 256), ((STARTZ // 16) + key.z) * 16 + (i // 16) % 16, str(section.getBlockStateTagAtIndex(i)["Name"]))    
            for key, section in WORLDSLICE._sections.items() for i in range(len(section.blockStatesBitArray))),
            dtype=[('x', int), ('y', int), ('z', int), ('Name', 'U60')],
            count=-1
        )

        df = pd.DataFrame.from_records(data)
        if (heightmap is not None) :
            df = df[df['z'].isin(heightmap.columns.values.tolist())]
            df = df[df['x'].isin(heightmap.index.values.tolist())]
        return df

    def __get_dominant_wood_type(self):
        """
        This function returns the wood type of the most common tree in the world slice
        This is a second function, as the first one uses the biomes, and this one uses all actual blocks

        :rtype: str
        :return: The wood type of the most common tree in the world slice (OAK, etc..)
        """
        blocks_count = pd.DataFrame(pd.Series(self.blocks["Name"].values.ravel()).value_counts()).reset_index()
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

    def get_blocks(self):
        return self.blocks
    
    def get_wood_type(self):
        return self.wood_type
    