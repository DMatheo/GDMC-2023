from constants import ED, GROUND_BLOCKS, STARTX, STARTZ, LASTX, LASTZ, DECORATIVE_GROUND_BLOCKS

from gdpc import Block

import random

class Road_builder():

    ROAD_VALUE_SUB_PART_LENGHT = 15

    MINIMUM_SPACE_BETWEEN_ROADS = 30

    OUT_OF_BOUNDS_MARGIN = 30

    MINIMUM_ROAD_VALUE = -200

    def __init__(self, surface_settlement):
        self.surface_settlement = surface_settlement
        self.roads = list()
    
    def calculate_main_roads(self, width=3, min_lenght=30):
        add = 1 if self.surface_settlement.cave_size % 2 == 0 else 0
        divided_width = width // 2

        main_south_road = self.calculate_main_south_road(width, add, divided_width, min_lenght)
        if main_south_road != None:
            self.roads.append(main_south_road)
        main_east_road = self.calculate_main_east_road(width, add, divided_width, min_lenght)
        if main_east_road != None:
            self.roads.append(main_east_road)
        main_north_road = self.calculate_main_north_road(width, add, divided_width, min_lenght)
        if main_north_road != None:
            self.roads.append(main_north_road)
        main_west_road = self.calculate_main_west_road(width, add, divided_width, min_lenght)
        if main_west_road != None:
            self.roads.append(main_west_road)
        
    def calculate_main_south_road(self, width, add, divided_width, min_lenght):
        startz = self.surface_settlement.location[1] + self.surface_settlement.size[1] - width + add - self.surface_settlement.size[1] // 6
        endz = self.surface_settlement.cave_location[2] + self.surface_settlement.cave_size // 2 + width + add
        if abs(startz - endz) < min_lenght:
            return None
        south_road = {
            "start": (
                self.surface_settlement.cave_location[0] + add - divided_width,
                startz
            ),
            "end": (
                self.surface_settlement.cave_location[0] + add + divided_width,
                endz
            ),
            "direction": "south",
            "width": width,
            "value": 0,
            "built": False,
        }
        if not self.calculate_road_value(south_road):
            return None
        return south_road

    def calculate_main_east_road(self, width, add, divided_width, min_lenght):
        startx = self.surface_settlement.location[0] + self.surface_settlement.size[0] - width + add - self.surface_settlement.size[0] // 6
        endx = self.surface_settlement.cave_location[0] + self.surface_settlement.cave_size // 2 + width + add
        if abs(startx - endx) < min_lenght:
            return None
        east_road = {
            "start": (
                startx, 
                self.surface_settlement.cave_location[2] + add - divided_width
            ),
            "end": (
                endx,
                self.surface_settlement.cave_location[2] + add + divided_width
            ),
            "direction": "east",
            "width": width,
            "value": 0,
            "built": False,
        }
        if not self.calculate_road_value(east_road):
            return None
        return east_road
    
    def calculate_main_north_road(self, width, add, divided_width, min_lenght):
        startz = self.surface_settlement.cave_location[2] - self.surface_settlement.cave_size // 2 - width + add
        endz = self.surface_settlement.location[1] + width + add + self.surface_settlement.size[1] // 6
        if abs(startz - endz) < min_lenght:
            return None
        north_road = {
            "start": (
                self.surface_settlement.cave_location[0] + add - divided_width,
                startz
            ),
            "end": (
                self.surface_settlement.cave_location[0] + add + divided_width,
                endz
            ),
            "direction": "north",
            "width": width,
            "value": 0,
            "built": False,
        }
        if not self.calculate_road_value(north_road):
            return None
        return north_road

    def calculate_main_west_road(self, width, add, divided_width, min_lenght):
        startx = self.surface_settlement.cave_location[0] - self.surface_settlement.cave_size // 2 - width + add
        endx = self.surface_settlement.location[0] + width + add + self.surface_settlement.size[0] // 6
        if abs(startx - endx) < min_lenght:
            return None
        west_road = {
            "start": (
                startx,
                self.surface_settlement.cave_location[2] + add - divided_width
            ),
            "end": (
                endx,
                self.surface_settlement.cave_location[2] + add + divided_width
            ),
            "direction": "west",
            "width": width,
            "value": 0,
            "built": False,
        }
        if not self.calculate_road_value(west_road):
            return None
        return west_road

    def calculate_roads_from_spaces(self, spaces, width):
        for space in spaces:
            road = {
                "start": space[0],
                "end": self.get_end_coord(space, width),
                "direction": space[1],
                "width": width,
                "value": 0,
                "built": False,
            }
            if self.calculate_road_value(road):
                self.roads.append(road)

    def get_best_road(self):
        best_road = None
        for road in self.roads:
            if not road["built"]:
                if best_road == None or road["value"] > best_road["value"]:
                    best_road = road

        return best_road

    def calculate_road_value(self, road):
        """
        Gives a value to the road given in parameter.
        return false if the value is too low.
        """
        values = list()
        direction_axis = 0 if road["direction"] == "east" or road["direction"] == "west" else 1
        width_axis = 0 if direction_axis == 1 else 1

        start = road["start"][direction_axis] if road["start"][direction_axis] < road["end"][direction_axis] else road["end"][direction_axis]
        end = road["end"][direction_axis] + 1 if start == road["start"][direction_axis] else road["start"][direction_axis] + 1

        counter = 0
        value = 0
        for d in range(start, end):
            max_y = -99
            for w in range(road["start"][width_axis], road["start"][width_axis] + road["width"]):
                x = w if direction_axis == 1 else d
                z = w if direction_axis == 0 else d
                y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
                block_id = ED.getBlock((x, y, z)).id
                if "water" in block_id:
                    value -= 2
                elif "lava" in block_id:
                    value -= 5
                else:
                    value += 2
                if y > max_y:
                    max_y = y

            tbl_x = road["start"][0] - 10 if width_axis == 0 else d
            tbl_z = road["start"][1] - 10 if width_axis == 1 else d
            tbr_x = road["start"][0] + road["width"] + 10 if width_axis == 0 else d
            tbr_z = road["start"][1] + road["width"] + 10 if width_axis == 1 else d
            if not self.is_out_of_bounds((tbl_x, max_y, tbl_z)) and not self.is_out_of_bounds((tbr_x, max_y, tbr_z)):
                ten_block_left_y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][tbl_x - self.surface_settlement.location[0]][tbl_z - self.surface_settlement.location[1]] - 1
                ten_block_right_y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][tbr_x - self.surface_settlement.location[0]][tbr_z - self.surface_settlement.location[1]] - 1
                if abs(ten_block_left_y - max_y) > 6:
                    value -= 6
                elif abs(ten_block_left_y - max_y) > 3:
                    value -= 3

                if abs(ten_block_right_y - max_y) > 6:
                    value -= 6
                elif abs(ten_block_right_y - max_y) > 3:
                    value -= 3

            if counter == self.ROAD_VALUE_SUB_PART_LENGHT:
                values.append(value)
                counter = 0
                value = 0
            else:
                counter += 1

        if len(values) == 0:
            value = -10000
        else:
            value = int(sum(values) / len(values))
        
        road["value"] = value
        return value > self.MINIMUM_ROAD_VALUE

    def get_end_coord(self, space, width):
        """
        returns the first coordinates which, in the given direction and for the given width, correspond to blocks which are not GROUND BLOCKS.
        """
        direction_axis = 0 if space[1]== "east" or space[1]== "west" else 1
        width_axis = 0 if direction_axis == 1 else 1

        coordinate = space[0][direction_axis]
        end = None

        while end == None:
            for w in range(space[0][width_axis], space[0][width_axis] + width):
                x = w if direction_axis == 1 else coordinate
                z = w if direction_axis == 0 else coordinate
                y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
                if not self.valid_road_position((x, y, z), direction_axis):
                    end = (x if z == w else space[0][width_axis] + width, z if x == w else space[0][width_axis] + width)
                    break
            coordinate += 1 if space[1]== "east" or space[1]== "south" else -1
        return end

    def valid_road_position(self, coord, direction_axis):

        if self.is_out_of_bounds(coord):
            return False

        if self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][coord[0] - self.surface_settlement.location[0]][coord[2] - self.surface_settlement.location[1]] != coord[1] +1:
            return False

        if "air" in ED.getBlock((coord[0], coord[1]-1, coord[2])).id:
            return False

        y = coord[1] +1
        block = ED.getBlock((coord[0], y, coord[2])).id
        while "air" not in block:
            if not any(block_type in block for block_type in GROUND_BLOCKS + DECORATIVE_GROUND_BLOCKS):
                return False
            y += 1
            block = ED.getBlock((coord[0], y, coord[2])).id

        prec_x = coord[0] - 1 if direction_axis == 0 else coord[0]
        prec_z = coord[2] - 1 if direction_axis == 1 else coord[2]
        prec_y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][prec_x - self.surface_settlement.location[0]][prec_z - self.surface_settlement.location[1]] - 1
        if abs(prec_y - coord[1]) > 1:
            return False
        
        return True

    def is_out_of_bounds(self, coord):
        if coord[0] <= STARTX + self.OUT_OF_BOUNDS_MARGIN or coord[0] >= LASTX - self.OUT_OF_BOUNDS_MARGIN or coord[2] <= STARTZ + self.OUT_OF_BOUNDS_MARGIN or coord[2] >= LASTZ - self.OUT_OF_BOUNDS_MARGIN:
            return True
        
        return False

    def roads_cross_or_insufficient_space(self, road1, road2):
        road1_axis = 0 if road1["direction"] == "east" or road1["direction"] == "west" else 1
        road1_width_axis = 0 if road1_axis == 1 else 1
        road2_axis = 0 if road2["direction"] == "east" or road2["direction"] == "west" else 1
        road2_width_axis = 0 if road2_axis == 1 else 1

        if road1_axis == road2_axis:
            if road1["start"][road1_axis] <= road2["end"][road2_axis] + self.MINIMUM_SPACE_BETWEEN_ROADS and road1["end"][road1_axis] >= road2["start"][road2_axis] - self.MINIMUM_SPACE_BETWEEN_ROADS:
                return True

        if road1["start"][road1_axis] >= road2["start"][road2_axis] and road1["start"][road1_axis] <= road2["end"][road2_axis]:
            if road2["start"][road2_width_axis] >= road1["start"][road1_width_axis] and road2["start"][road2_width_axis] <= road1["end"][road1_width_axis]:
                return True

        return False


    def create_road(self, road):
        road["built"] = True

        # delete all not built roads that cross the new road
        for tested_road in self.roads:
            if tested_road["built"]:
                continue
            if self.roads_cross_or_insufficient_space(road, tested_road):
                self.roads.remove(tested_road)

        # x = 0, z = 1
        direction_axis = 0 if road["direction"] == "east" or road["direction"] == "west" else 1
        width_axis = 0 if direction_axis == 1 else 1

        start = road["start"][direction_axis] if road["start"][direction_axis] < road["end"][direction_axis] else road["end"][direction_axis]
        end = road["end"][direction_axis] + 1 if start == road["start"][direction_axis] else road["start"][direction_axis] + 1

        bridge_line_number = 0
        prec_y = None
        water_y = None

        for d in range(start, end):
            road_type = "simple"
            for w in range(road["start"][width_axis], road["start"][width_axis] + road["width"]):
                x = w if direction_axis == 1 else d
                z = w if direction_axis == 0 else d
                y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
                if "water" in ED.getBlock((x, y, z)).id or "lava" in ED.getBlock((x, y, z)).id or "stone_brick_stairs" in ED.getBlock((x, y, z)).id:
                    road_type = "bridge"
                    bridge_line_number += 1
                    water_y = y
                    break
            x = road["start"][0] if direction_axis == 1 else d
            z = road["start"][1] if direction_axis == 0 else d
            y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1 if road_type == "simple" else water_y
            if road_type == "simple":
                if bridge_line_number != 0:
                    self.build_stairs((x, prec_y+1, z), direction_axis, road["width"], False)
                    bridge_line_number = 0
                else:
                    self.simple_road_line((x, z), width_axis, road["width"])
            else:
                if bridge_line_number == 1:
                    self.build_stairs((x, y+1, z), direction_axis, road["width"], True)
                else:
                    self.bridge_road_line((x, y, z), road["direction"], road["width"], bridge_line_number)
            prec_y = y

    def simple_road_line(self, coord, direction_axis, width):
        for w in range(coord[direction_axis], coord[direction_axis] + width):
            x = coord[0] if direction_axis == 1 else w
            z = coord[1] if direction_axis == 0 else w
            y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
            ED.placeBlock((x, y, z), Block("dirt_path"))


    def bridge_road_line(self, coord, road_direction, width, line_number):
        line_axis = 2 if road_direction == "east" or road_direction == "west" else 0
        y = coord[1]
        for w in range(coord[line_axis], coord[line_axis] + width):
            x = coord[0] if line_axis == 2 else w
            z = coord[2] if line_axis == 0 else w
            y_watter_bottom = self.surface_settlement.worldSlice.heightmaps["OCEAN_FLOOR"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
            ED.placeBlock((x, y+1, z), Block("stone_bricks"))
            line_number_tmp = line_number
            if line_number_tmp % 5 == 0:
                x_stairs_prec = x if line_axis == 0 else x - 1
                z_stairs_prec = z if line_axis == 2 else z - 1
                x_stairs_next = x if line_axis == 0 else x + 1
                z_stairs_next = z if line_axis == 2 else z + 1
                ED.placeBlock(
                    (x_stairs_prec, y, z_stairs_prec), 
                    Block(
                        "stone_brick_stairs", 
                        {
                            "facing": "south" if road_direction == "south" or road_direction == "north" else "east", 
                            "half": "top"
                        }
                    )
                )
                ED.placeBlock(
                    (x_stairs_next, y, z_stairs_next), 
                    Block(
                        "stone_brick_stairs", 
                        {
                            "facing": "north" if road_direction == "north" or road_direction == "south" else "west", 
                            "half": "top"
                        }
                    )
                )
                for y_ite in range(y, y_watter_bottom, -1):
                    ED.placeBlock((x, y_ite, z), Block("stone_bricks"))

    def build_stairs(self, coord, direction_axis, width, revert):
        facing = "south" if direction_axis == 1 and revert else "north" if direction_axis == 1 else "east" if revert else "west"
        width_axis = 0 if direction_axis == 1 else 2
        step = -1 if revert else 1
        for w in range(coord[width_axis], coord[width_axis] + width):
            x = coord[0] if width_axis == 2 else w
            z = coord[2] if width_axis == 0 else w
            y = coord[1]
            if self.is_out_of_bounds((x, y, z)):
                continue
            block = ED.getBlock((x, y, z)).id
            while not any(ground_block in block for ground_block in GROUND_BLOCKS):
                ED.placeBlock((x, y, z), Block("stone_brick_stairs", {"facing": facing}))
                y_floor = self.surface_settlement.worldSlice.heightmaps["OCEAN_FLOOR"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
                for y_ite in range(y-1, y_floor, -1):
                    ED.placeBlock((x, y_ite, z), Block("stone_bricks"))
                x = x + step if direction_axis == 0 else x
                z = z + step if direction_axis == 1 else z
                y -= 1
                if self.is_out_of_bounds((x, y, z)):
                    break
                block = ED.getBlock((x, y, z)).id
        