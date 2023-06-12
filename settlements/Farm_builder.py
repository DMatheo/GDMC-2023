from constants import ED, STARTX, STARTZ, LASTX, LASTZ, GROUND_BLOCKS
from buildings.Windmill import Windmill

from gdpc import Block
from glm import ivec3


import random


class Farm_builder:

    # the higher the number, the lower the probability (1/number)
    WATER_PROB = 4

    def __init__(self, surface_settlement):
        self.surface_settlement = surface_settlement

    def create_farm(self, road):
        if road["direction"] == "north":
            self.create_north_farm(road["end"])
        elif road["direction"] == "south":
            self.create_south_farm(road["start"])
        elif road["direction"] == "east":
            self.create_east_farm(road["start"])
        elif road["direction"] == "west":
            self.create_west_farm(road["end"])

    def create_north_farm(self, starting_coord):
        length = starting_coord[1] - STARTZ
        if length < Windmill.DIMENSIONS['north'][2]:
            return

        z = STARTZ + (length - Windmill.DIMENSIONS['north'][2])
        x = starting_coord[0] - Windmill.DIMENSIONS['north'][0] // 2 - 1
        y = self.surface_settlement.get_area_altitude_difference_and_maxy((x, z), (Windmill.DIMENSIONS['north'][0], Windmill.DIMENSIONS['north'][2]))[1]
        windmill = Windmill((x, y, z), "south", self.surface_settlement)
        windmill.build()

        self.create_wheat_field(
            STARTX,
            LASTX,
            STARTZ,
            starting_coord[1] - 3,
            (windmill.coord[0], windmill.coord[0] + windmill.DIMENSIONS[windmill.facing][0], windmill.coord[2], starting_coord[1]),
            (windmill.coord[0] -1, self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][windmill.coord[0] -1 - self.surface_settlement.location[0]][windmill.coord[2] - self.surface_settlement.location[1]] - 1, windmill.coord[2])
        )

    def create_south_farm(self, starting_coord):
        length = LASTZ - starting_coord[1]
        if length < Windmill.DIMENSIONS['north'][2]:
            return

        z = starting_coord[1] + (length - Windmill.DIMENSIONS['north'][2]) // 2
        x = starting_coord[0] - Windmill.DIMENSIONS['north'][0] // 2
        y = self.surface_settlement.get_area_altitude_difference_and_maxy((x, z), (Windmill.DIMENSIONS['north'][0], Windmill.DIMENSIONS['north'][2]))[1]
        windmill = Windmill((x, y, z), "north", self.surface_settlement)
        windmill.build()

        self.create_wheat_field(
            STARTX,
            LASTX,
            starting_coord[1] + 3,
            LASTZ,
            (windmill.coord[0], windmill.coord[0] + windmill.DIMENSIONS[windmill.facing][0], starting_coord[1], windmill.coord[2] + windmill.DIMENSIONS[windmill.facing][2]),
            (windmill.coord[0] -1, self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][windmill.coord[0] -1 - self.surface_settlement.location[0]][windmill.coord[2] - self.surface_settlement.location[1]] - 1, windmill.coord[2])
        )

    def create_east_farm(self, starting_coord):
        length = LASTX - starting_coord[0]
        if length < Windmill.DIMENSIONS['east'][0]:
            return
        x = LASTX - (length - Windmill.DIMENSIONS['east'][0]) // 2 - Windmill.DIMENSIONS['east'][0]
        z = starting_coord[1] - Windmill.DIMENSIONS['east'][2] // 2
        y = self.surface_settlement.get_area_altitude_difference_and_maxy((x, z), (Windmill.DIMENSIONS['east'][0], Windmill.DIMENSIONS['east'][2]))[1]
        windmill = Windmill((x, y, z), "west", self.surface_settlement)
        windmill.build()
        
        self.create_wheat_field(
            starting_coord[0] + 3,
            LASTX,
            STARTZ,
            LASTZ,
            (starting_coord[0], windmill.coord[0] + windmill.DIMENSIONS[windmill.facing][0], windmill.coord[2], windmill.coord[2] + windmill.DIMENSIONS[windmill.facing][2]),
            (windmill.coord[0], self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][windmill.coord[0] - self.surface_settlement.location[0]][windmill.coord[2] - 1 - self.surface_settlement.location[1]] - 1, windmill.coord[2] - 1)
        )

    def create_west_farm(self, starting_coord):
        length = starting_coord[0] - STARTX
        if length < Windmill.DIMENSIONS['east'][0]:
            return
        x = STARTX + (length - Windmill.DIMENSIONS['east'][0]) // 2
        z = starting_coord[1] - Windmill.DIMENSIONS['east'][2] // 2
        y = self.surface_settlement.get_area_altitude_difference_and_maxy((x, z), (Windmill.DIMENSIONS['east'][0], Windmill.DIMENSIONS['east'][2]))[1]
        windmill = Windmill((x, y, z), "east", self.surface_settlement)
        windmill.build()

        self.create_wheat_field(
            STARTX,
            starting_coord[0] - 3,
            STARTZ,
            LASTZ,
            (windmill.coord[0], starting_coord[0], windmill.coord[2], windmill.coord[2] + windmill.DIMENSIONS[windmill.facing][2]),
            (windmill.coord[0], self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][windmill.coord[0] - self.surface_settlement.location[0]][windmill.coord[2] - 1 - self.surface_settlement.location[1]] - 1, windmill.coord[2] - 1)
        )
    
    def create_wheat_field(self, start_x, end_x, start_z, end_z, field_condition, coord):
        x, y, z = coord[0], coord[1], coord[2]
        surrounding_xz_coords = ((x+1, z), (x-1, z), (x, z+1), (x, z-1))
        
        correct_position = True
        for surrounding_coord in surrounding_xz_coords:
            if not any(block_type in ED.getBlock((surrounding_coord[0], y, surrounding_coord[1])).id for block_type in GROUND_BLOCKS):
                correct_position = False

        if correct_position and random.randint(1, self.WATER_PROB) == 1:
            ED.placeBlock((x, y, z), Block("water"))
        else:
            ED.placeBlock((x, y, z), Block("farmland"))
            ED.placeBlock((x, y+1, z), Block("wheat", {"age": 7}))
        
        for surrounding_coord in surrounding_xz_coords:
            surrounding_y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][surrounding_coord[0] - self.surface_settlement.location[0]][surrounding_coord[1] - self.surface_settlement.location[1]] - 1
            if abs(surrounding_y - y) > 1:
                continue
            if surrounding_coord[0] < start_x +2 or surrounding_coord[0] > end_x -2 or surrounding_coord[1] < start_z +2 or surrounding_coord[1] > end_z -2:
                continue
            if surrounding_coord[0] >= field_condition[0] and surrounding_coord[0] < field_condition[1] and surrounding_coord[1] >= field_condition[2] and surrounding_coord[1] <= field_condition[3]:
                continue
            if surrounding_coord[0] < field_condition[0] - 10 or surrounding_coord[0] > field_condition[1] + 10 or surrounding_coord[1] < field_condition[2] - 10 or surrounding_coord[1] > field_condition[3] + 10:
                continue
            if "water" in ED.getBlock((surrounding_coord[0], surrounding_y, surrounding_coord[1])).id:
                continue
            if "farmland" in ED.getBlock((surrounding_coord[0], surrounding_y, surrounding_coord[1])).id:
                continue
            self.create_wheat_field(start_x, end_x, start_z, end_z, field_condition, (surrounding_coord[0], surrounding_y, surrounding_coord[1]))
