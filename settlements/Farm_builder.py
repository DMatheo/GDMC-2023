from constants import ED, STARTX, STARTZ, LASTX, LASTZ, GROUND_BLOCKS
from buildings.Windmill import Windmill

from gdpc import Block
from glm import ivec3


import random


class Farm_builder:

    def __init__(self, surface_settlement):
        self.surface_settlement = surface_settlement

    def create_farm(self, road):
        if road["direction"] == "north":
            self.create_north_farm(road["end"])
        elif road["direction"] == "south":
            self.create_south_farm(road["end"])
        elif road["direction"] == "east":
            self.create_east_farm(road["end"])
        elif road["direction"] == "west":
            self.create_west_farm(road["end"])

    def create_north_farm(self, starting_coord):
        length = starting_coord[1] - STARTZ
        if length < Windmill.DIMENSIONS['north'][2]:
            return

        z = STARTZ + (length - Windmill.DIMENSIONS['north'][2])
        x = starting_coord[0] - Windmill.DIMENSIONS['north'][0] // 2 - 1
        y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]]
        windmill = Windmill((x, y, z), "south", self.surface_settlement)
        windmill.build()

        self.create_wheat_field(
            STARTX,
            LASTX,
            STARTZ,
            starting_coord[1] - 3,
            windmill,
            (windmill.coord[0], windmill.coord[0] + windmill.DIMENSIONS[windmill.facing][0], windmill.coord[2], starting_coord[1])
        )

    # RESOLVE THIS
    def create_south_farm(self, starting_coord):
        length = LASTZ - starting_coord[1]
        if length < Windmill.DIMENSIONS['north'][2]:
            return

        z = starting_coord[1] + (length - Windmill.DIMENSIONS['north'][2]) // 2
        x = starting_coord[0] - Windmill.DIMENSIONS['north'][0] // 2
        y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]]
        windmill = Windmill((x, y, z), "north", self.surface_settlement)
        windmill.build()

        self.create_wheat_field(
            STARTX,
            LASTX,
            starting_coord[1] + 3,
            LASTZ,
            windmill,
            (windmill.coord[0], windmill.coord[0] + windmill.DIMENSIONS[windmill.facing][0], starting_coord[1], windmill.coord[2] + windmill.DIMENSIONS[windmill.facing][2])
        )

    def create_east_farm(self, starting_coord):
        length = LASTX - starting_coord[0]
        if length < Windmill.DIMENSIONS['east'][0]:
            return
        x = LASTX - (length - Windmill.DIMENSIONS['east'][0]) // 2 - Windmill.DIMENSIONS['east'][0]
        z = starting_coord[1] - Windmill.DIMENSIONS['east'][2] // 2
        y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]]
        windmill = Windmill((x, y, z), "west", self.surface_settlement)
        windmill.build()
        
        self.create_wheat_field(
            starting_coord[0] + 3,
            LASTX,
            STARTZ,
            LASTZ,
            windmill,
            (starting_coord[0], windmill.coord[0] + windmill.DIMENSIONS[windmill.facing][0], windmill.coord[2], windmill.coord[2] + windmill.DIMENSIONS[windmill.facing][2])
        )

    def create_west_farm(self, starting_coord):
        length = starting_coord[0] - STARTX
        if length < Windmill.DIMENSIONS['east'][0]:
            return
        x = STARTX + (length - Windmill.DIMENSIONS['east'][0]) // 2
        z = starting_coord[1] - Windmill.DIMENSIONS['east'][2] // 2
        y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]]
        windmill = Windmill((x, y, z), "east", self.surface_settlement)
        windmill.build()

        self.create_wheat_field(
            STARTX,
            starting_coord[0] - 3,
            STARTZ,
            LASTZ,
            windmill,
            (windmill.coord[0], starting_coord[0], windmill.coord[2], windmill.coord[2] + windmill.DIMENSIONS[windmill.facing][2])
        )

    def create_wheat_field(self, start_x, end_x, start_z, end_z, windmill, field_condition):
        x = start_x + 1
        while x < end_x:
            z = start_z + 1
            while z < end_z - 3:
                if x >= field_condition[0] and x < field_condition[1] and z >= field_condition[2] and z <= field_condition[3]:
                    z += random.randint(5, 8)
                    continue
                y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
                correct_position = True
                for surrounding_coord in ((x+1, y, z), (x-1, y, z), (x, y, z+1), (x, y, z-1)):
                    if not any(block_type in ED.getBlock(surrounding_coord).id for block_type in GROUND_BLOCKS):
                        z += random.randint(3, 5)
                        correct_position = False
                if not correct_position:
                    continue
                ED.placeBlock((x, y, z), Block("water"))
                z += random.randint(5, 8)
            x += random.randint(5, 8)
        
        for x in range(start_x, end_x):
            for z in range(start_z, end_z - 3):
                if x >= field_condition[0] and x < field_condition[1] and z >= field_condition[2] and z <= field_condition[3]:
                    continue
                y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
                if "water" in ED.getBlock((x, y, z)).id:
                    continue
                ED.placeBlock((x, y, z), Block("farmland"))
                ED.placeBlock((x, y+1, z), Block("wheat", {"age": 7}))
