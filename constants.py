import logging
import pandas as pd
import time
from Worldmap import Worldmap
from Cavemap import Cavemap
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
WORLD_MAP = Worldmap(STARTX, STARTZ, WORLDSLICE, HEIGHTS)
ALL_BLOCKS = WORLD_MAP.get_blocks()
print("All blocks obtained !")
print(ALL_BLOCKS)
print(f"All blocks took {time.time() - rough_exec_time}")

print("Getting the cave map...")
rough_exec_time = time.time()
CAVE_MAP = Cavemap(HEIGHTS, ALL_BLOCKS)
ALL_BLOCKS_CAVEMAP = CAVE_MAP.get_blocks()
print("Cave map obtained !")
print(ALL_BLOCKS_CAVEMAP)
print(f"Cave map took {time.time() - rough_exec_time}")

WOOD_TYPE = WORLD_MAP.get_wood_type()
print(WOOD_TYPE)