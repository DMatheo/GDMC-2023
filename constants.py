import logging
import pandas as pd
import numpy as np
import time

from termcolor import colored

from gdpc import Editor

logging.basicConfig(format=colored(
    "%(name)s - %(levelname)s - %(message)s", color="yellow"))

ED = Editor(buffering=True)

BUILD_AREA = ED.getBuildArea()  # BUILDAREA
STARTX, STARTY, STARTZ = BUILD_AREA.begin
LASTX, LASTY, LASTZ = BUILD_AREA.last


# WORLDSLICE
# Using the start and end coordinates we are generating a world slice
# It contains all manner of information, including heightmaps and biomes
# For further information on what information it contains, see
# https://minecraft.fandom.com/wiki/Chunk_format
#
# IMPORTANT: Keep in mind that a wold slice is a 'snapshot' of the world,
# and any changes you make later on will not be reflected in the world slice
WORLDSLICE = ED.loadWorldSlice(BUILD_AREA.toRect(), cache=True)  # this takes a while

FLOWERS = (
    "allium",
    "azure_bluet",
    "blue_orchid",
    "lily_of_the_valley",
    "oxeye_daisy",
    "poppy",
    "dandelion"
)

ROADHEIGHT = 0

def getBlocksInSlice(heightmap = None):

    """ 
    Gets all the blocks in the slice
    Be warned : this algorithm is costly and should only be called once.

    :type heightmap: List(List(int))
    :param heightmap: List of List of top Y coordinates

    :return: Dataframe with all blocks in the current slice
    """
    #Handmade
    #data = [{   'x' : ((STARTX // 16) + key.x) * 16 + i % 16,
    #            'y' : key.y * 16 + (i // 256),
    #            'z' : ((STARTZ // 16) + key.z) * 16 + (i // 16) % 16,
    #            'Name': str(section.getBlockStateTagAtIndex(i)["Name"])}    
    #        for key, section in WORLDSLICE._sections.items() for i in range(len(section.blockStatesBitArray))
    #        ]
    
    #faster, but using copilot...
    data = np.fromiter(
        (( ((STARTX // 16) + key.x) * 16 + i % 16, key.y * 16 + (i // 256), ((STARTZ // 16) + key.z) * 16 + (i // 16) % 16, str(section.getBlockStateTagAtIndex(i)["Name"]))    
        for key, section in WORLDSLICE._sections.items() for i in range(len(section.blockStatesBitArray))),
        dtype=[('x', int), ('y', int), ('z', int), ('Name', 'U16')],
        count=-1
    )

    df = pd.DataFrame.from_records(data)
    if (heightmap is not None) :
        df = df[df['z'].isin(heightmap.columns.values.tolist())]
        df = df[df['x'].isin(heightmap.index.values.tolist())]
    return df

rough_exec_time = time.time()

print("Getting height map..")
HEIGHTS = pd.DataFrame(WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"])
HEIGHTS.index = [x for x in range(STARTX, LASTX+1)]
HEIGHTS.columns = [z for z in range(STARTZ, LASTZ+1)]
print("Height map obtained !")
print(HEIGHTS)
print(f"Heightmap took {time.time()-rough_exec_time}")

print("Getting all blocks..")
rough_exec_time = time.time()
ALL_BLOCKS = getBlocksInSlice(HEIGHTS)
print("All blocks obtained !")
print(ALL_BLOCKS)
print(f"All blocks took {time.time() - rough_exec_time}")

