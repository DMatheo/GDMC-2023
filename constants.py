import logging

from termcolor import colored

from gdpc import Editor

import numpy as np
import pandas as pd

logging.basicConfig(format=colored(
    "%(name)s - %(levelname)s - %(message)s", color="yellow"))

ED = Editor(buffering=True)

BUILD_AREA = ED.getBuildArea()  # BUILDAREA
STARTX, STARTY, STARTZ = BUILD_AREA.begin
LASTX, LASTY, LASTZ = BUILD_AREA.last

WORLDSLICE = ED.loadWorldSlice(
    BUILD_AREA.toRect(), cache=True)  # this takes a while

FLOWERS = (
    "allium",
    "azure_bluet",
    "blue_orchid",
    "lily_of_the_valley",
    "oxeye_daisy",
    "poppy",
    "dandelion"
)

GROUND_BLOCKS = (
    "dirt",
    "grass_block",
    "stone",
    "sand",
    "terracotta", 
    "water",
    "lava",
    "snow_block",
    "podzol",
    "mud",
    "ice",
    "gravel"
)

DECORATIVE_GROUND_BLOCKS = FLOWERS + (
    "grass",
    "snow",
    "dead_bush",
    "fern"
)

CLIFF_BLOCKS = (
    "stone",
    "andesite",
    "diorite",
    "cobblestone"
)

ROAD_BLOCKS = (
    "dirt_path",
    "stone_bricks"
)

#Heightmap
MOTION_BLOCKING_NO_LEAVES = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
OCEAN_FLOOR = WORLDSLICE.heightmaps["OCEAN_FLOOR"]
WORLD_SURFACE = WORLDSLICE.heightmaps["WORLD_SURFACE"]


MOTION_BLOCKING_NO_LEAVES_DF = pd.DataFrame(MOTION_BLOCKING_NO_LEAVES)
OCEAN_FLOOR_DF = pd.DataFrame(OCEAN_FLOOR)
NO_WATER_NO_LEAVES_NP_ARR = np.where(MOTION_BLOCKING_NO_LEAVES_DF == OCEAN_FLOOR_DF, MOTION_BLOCKING_NO_LEAVES_DF, None)