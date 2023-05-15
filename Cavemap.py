from utils import get_largest_sequence, apply_heightmap
import pandas as pd
import numpy as np

class Cavemap:
    def __init__(self, HEIGHTS, ALL_BLOCKS):
        #Get the blocks
        self.cave_map_blocks = self.__get_cave_map(HEIGHTS, ALL_BLOCKS)

        #Get the largest intervals
        self.largest_intervals = self.__get_largest_caves()

        #Get the caves
        self.caves = self.__get_caves()

    def __get_caves(self):
        """
        Gets the caves
        """
        #Get largest caves
        largest_caves, largest_possible_cave = self.__get_largest_caves()
        if (largest_caves is None or largest_possible_cave is None):
            print("No caves found !")
            return

    def __get_cave_map(self, HEIGHTS, ALL_BLOCKS):
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

    def __get_largest_caves(self):
        """
        This function returns a dataframe containing all the largest caves in the world slice, 
        aswell as Series containing the coordinates of the largest cave

        :rtype: pd.DataFrame, pd.Series
        :return: The dataframe containing all the largest caves in the world slice,
        aswell as Series containing the coordinates of the largest cave
        """


        # Changing the column and rows to current x and z, stocking y in lists for each coordinate
        underground_sequences = self.cave_map_blocks.drop(['Name'], inplace=False, axis=1).groupby(['x', 'z'])['y'].apply(list).reset_index()
        # Now, for each value of y, I'll apply the largest sequence in a given list of number :
        underground_sequences['y'] = underground_sequences['y'].apply(get_largest_sequence)
        # Now, I'll add a column with the length of the sequences, for later use
        underground_sequences['Length_of_sequence'] = underground_sequences['y'].str.len()

        # Should return :
        # - 2D map with biggest cave spotted, with top Y and bottom Y, for every X & Z
        # - Row with the largest cave
        return underground_sequences, underground_sequences.loc[underground_sequences['Length_of_sequence'].idxmax()]

    def get_blocks(self):
        return self.cave_map_blocks
    
    def get_largest_intervals(self):
        return self.largest_intervals

    def get_caves(self):
        return self.caves
