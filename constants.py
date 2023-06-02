import logging

from termcolor import colored

from gdpc import Editor

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
    "ice"
)

DECORATIVE_GROUND_BLOCKS = FLOWERS + (
    "grass",
    "snow"
)

CLIFF_BLOCKS = (
    "stone",
    "andesite",
    "diorite",
    "cobblestone"
)

ROAD_BLOCKS = (
    "dirt_path",
    "stone_bricks",
    "campfire",
)