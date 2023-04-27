import logging

from termcolor import colored

from gdpc import Editor

logging.basicConfig(format=colored("%(name)s - %(levelname)s - %(message)s", color="yellow"))

ED = Editor(buffering=True)

BUILD_AREA = ED.getBuildArea()  # BUILDAREA
STARTX, STARTY, STARTZ = BUILD_AREA.begin
LASTX, LASTY, LASTZ = BUILD_AREA.last

WORLDSLICE = ED.loadWorldSlice(BUILD_AREA.toRect(), cache=True)  # this takes a while