from gdpc.vector_tools import distance

from buildings.Small_house import Small_house
from buildings.Shop import Shop

from constants import ED, GROUND_BLOCKS, ROAD_BLOCKS, DECORATIVE_GROUND_BLOCKS

import random

class Building_builder:

    SHOP_NEARBY_DISTANCE = 75

    ALTITUDE_DIFF_MAX = 1

    MINIMUM_SPACE_BETWEEN_BUILDINGS = 8

    NO_BUILDING_SPACE_INTERVAL = (7,13)

    DISTANCE_FROM_ROAD = 2

    def __init__(self, surface_settlement):
        self.surface_settlement = surface_settlement

    def is_shop_nearby(self, coord):
        for building in self.surface_settlement.buildings:

            if "Shop" not in building.name:
                continue

            if distance((building.coord[0], building.coord[2]), coord) < self.SHOP_NEARBY_DISTANCE:
                return True

        return False

    def is_building_possible(self, starting_coord, dimensions, facing):
        """
        Return -999 if not possible, otherwise return the maxy of the area
        """
        if self.surface_settlement.is_water_present(starting_coord, (dimensions[0], dimensions[2])):
            return -999

        area_altitude_difference_and_maxy = self.surface_settlement.get_area_altitude_difference_and_maxy(starting_coord, (dimensions[0], dimensions[2]))
        if area_altitude_difference_and_maxy[2][facing] > self.ALTITUDE_DIFF_MAX:
            return -999


        return area_altitude_difference_and_maxy[1]

    def determine_building(self, starting_coord, facing):

        small_house_starting_coord = (
            starting_coord[0] if not facing == "east" else starting_coord[0] - Small_house.DIMENSIONS[facing][0],
            starting_coord[1] if not facing == "south" else starting_coord[1] - Small_house.DIMENSIONS[facing][2]
        )

        shop_starting_coord = (
            starting_coord[0] if not facing == "east" else starting_coord[0] - Shop.DIMENSIONS[facing][0],
            starting_coord[1] if not facing == "south" else starting_coord[1] - Shop.DIMENSIONS[facing][2]
        )

        y = self.is_building_possible(small_house_starting_coord, Small_house.DIMENSIONS[facing], facing)
        if y > -999 and self.is_shop_nearby(small_house_starting_coord):
            return Small_house((small_house_starting_coord[0], y, small_house_starting_coord[1]), facing, self.surface_settlement)
        
        y = self.is_building_possible(shop_starting_coord, Shop.DIMENSIONS[facing], facing)
        if y > -999:
            return Shop((shop_starting_coord[0], y, shop_starting_coord[1]), facing, self.surface_settlement)

        return None

    def calculate_side_distance(self, x, z, direction):
        distance = 0
        y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
        block_id = ED.getBlock((x, y, z)).id
        while any(road_block in block_id for road_block in ROAD_BLOCKS):
            if direction == "south":
                x += 1
            elif direction == "north":
                x -= 1
            elif direction == "east":
                z -= 1
            else:
                z += 1
            block_id = ED.getBlock((x, y, z)).id
            distance += 1
        return distance

    def is_place_available(self, starting_coord, size, facing):

        x_range = range(starting_coord[0], starting_coord[0] + size[0]) if not facing == "east" else range(starting_coord[0] - size[0], starting_coord[0])
        z_range = range(starting_coord[1], starting_coord[1] + size[1]) if not facing == "south" else range(starting_coord[1] - size[1], starting_coord[1])

        for x in x_range:
            for z in z_range:
                y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
                block = ED.getBlock((x, y, z)).id
                if "air" in block:
                    return False
                while "air" not in block:
                    if not any(block_type in block for block_type in GROUND_BLOCKS + DECORATIVE_GROUND_BLOCKS):
                        return False
                    y += 1
                    block = ED.getBlock((x, y, z)).id
        return True

    def place_buildings_along_road(self, road):
        """
        return available spaces coordinates (for the roads)
        """
        axis = 0 if road["direction"] == "east" or road["direction"] == "west" else 1
        start = road["start"][axis] if road["start"][axis] < road["end"][axis] else road["end"][axis]
        end = road["end"][axis] if road["start"][axis] < road["end"][axis] else road["start"][axis]

        facing = {"north": "east", "south": "west", "west": "north", "east": "south"}.get(road["direction"])
        secondary_axis_coord = road["start"][0 if axis == 1 else 1]
        available_space_coord = secondary_axis_coord
        if road["direction"] == "south" or road["direction"] == "west":
            available_space_coord += road["width"]
            secondary_axis_coord += road["width"] + self.DISTANCE_FROM_ROAD 
        else:
            available_space_coord -= 1
            secondary_axis_coord -= self.DISTANCE_FROM_ROAD + 1

        available_spaces = self.place_buildings_on_a_side(
            axis,
            start,
            end,
            secondary_axis_coord,
            facing,
            available_space_coord
        )

        facing = {"north": "west", "south": "east", "west": "south", "east": "north"}.get(road["direction"])
        secondary_axis_coord = road["start"][0 if axis == 1 else 1]
        available_space_coord = secondary_axis_coord
        if road["direction"] == "south" or road["direction"] == "west":
            available_space_coord -= 1
            secondary_axis_coord -= self.DISTANCE_FROM_ROAD + 1
        else:
            available_space_coord += road["width"]
            secondary_axis_coord += road["width"] + self.DISTANCE_FROM_ROAD
        
        available_spaces += self.place_buildings_on_a_side(
            axis,
            start,
            end,
            secondary_axis_coord,
            facing,
            available_space_coord
        )
        
        return available_spaces

    def place_buildings_on_a_side(self, axis, start, end, secondary_axis_coord, facing, available_space_coord):
        """
        return available spaces coordinates (for the roads)
        """
        available_spaces = list()

        coordinate = start

        while coordinate < end:
            x = coordinate if axis == 0 else secondary_axis_coord
            z = coordinate if axis == 1 else secondary_axis_coord
            
            if not self.is_place_available((x, z), (25, 25), facing):
                coordinate += random.randint(self.NO_BUILDING_SPACE_INTERVAL[0], self.NO_BUILDING_SPACE_INTERVAL[1])
                continue

            building = self.determine_building((x, z), facing)
            if building:
                building.build()
                space = self.MINIMUM_SPACE_BETWEEN_BUILDINGS + random.randint(1, 3)
                available_space_x = coordinate + building.DIMENSIONS[facing][0] + space // 2 if axis == 0 else available_space_coord
                available_space_z = coordinate + building.DIMENSIONS[facing][2] + space // 2 if axis == 1 else available_space_coord
                available_spaces.append(((available_space_x, available_space_z), "north" if facing == "south" else "south" if facing == "north" else "east" if facing == "west" else "west"))
                coordinate += building.DIMENSIONS[facing][0 if axis == 0 else 2] + space
            else:
                coordinate += random.randint(self.NO_BUILDING_SPACE_INTERVAL[0], self.NO_BUILDING_SPACE_INTERVAL[1])
            
        return available_spaces