from constants import ED, GROUND_BLOCKS, STARTX, STARTZ, LASTX, LASTZ

from gdpc import Block

import random


class Road_builder():

    MINIMUM_SPACE_BETWEEN_ROADS = 30

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
        self.calculate_road_value(south_road)
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
        self.calculate_road_value(east_road)
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
        self.calculate_road_value(north_road)
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
        self.calculate_road_value(west_road)
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
            self.calculate_road_value(road)
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
        """
        road["value"] = random.randint(0, 100)

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
                print(coordinate, x, y, z)
                if not self.valid_road_position((x, y, z)):
                    end = (x if z == w else space[0][width_axis] + width, z if x == w else space[0][width_axis] + width)
                    break
            coordinate += 1 if space[1]== "east" or space[1]== "south" else -1
        return end

    def valid_road_position(self, coord):

        print("testing", coord)
        print("testing inf to starx", coord[0] < STARTX + 1, coord[0], STARTX + 1)
        print("testing sup to lastx", coord[0] > LASTX - 1, coord[0], LASTX - 1)
        print("testing inf to startz", coord[2] < STARTZ + 1, coord[2], STARTZ + 1)
        print("testing sup to lastz", coord[2] > LASTZ - 1, coord[2], LASTZ - 1)

        if coord[0] <= STARTX + 30 or coord[0] >= LASTX - 30 or coord[2] <= STARTZ + 30 or coord[2] >= LASTZ - 30:
            return False

        print("not out of bounds")

        if "air" not in ED.getBlock((coord[0], coord[1] +1, coord[2])).id:
            return False

        print("not under a block")

        if not any(block in ED.getBlock((coord[0], coord[1], coord[2])).id for block in GROUND_BLOCKS):
            return False
        
        print("valid ground")

        return True

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

        for d in range(start, end):
            road_line_function = None
            for w in range(road["start"][width_axis], road["start"][width_axis] + road["width"]):
                x = road["start"][0] if direction_axis == 1 else d
                z = road["start"][1] if direction_axis == 0 else d
                y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
                if "water" in ED.getBlock((x, y, z)).id or "lava" in ED.getBlock((x, y, z)).id:
                    road_line_function = self.bridge_road_line
                    break
            if road_line_function == None:
                road_line_function = self.simple_road_line
            road_line_function((x, z), width_axis, road["width"])


    def simple_road_line(self, coord, direction_axis, width):
        for w in range(coord[direction_axis], coord[direction_axis] + width):
            x = coord[0] if direction_axis == 1 else w
            z = coord[1] if direction_axis == 0 else w
            y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
            ED.placeBlock((x, y, z), Block("dirt_path"))


    def bridge_road_line(self, coord, direction_axis, width):
        for w in range(coord[direction_axis], coord[direction_axis] + width):
            x = coord[0] if direction_axis == 1 else w
            z = coord[1] if direction_axis == 0 else w
            y = self.surface_settlement.worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"][x - self.surface_settlement.location[0]][z - self.surface_settlement.location[1]] - 1
            block = ED.getBlock((x, y, z)).id
            while "water" in block or "lava" in block:
                y += 1
                block = ED.getBlock(position=(x, y, z)).id
            ED.placeBlock((x, y, z), Block("stone_bricks"))

    def suspended_bridge_road_line(self, coord, direction_axis, width, y):
        for w in range(coord[direction_axis], coord[direction_axis] + width):
            x = coord[0] if direction_axis == 1 else w
            z = coord[1] if direction_axis == 0 else w
            ED.placeBlock((x, y, z), Block("campfire", {"lit": "false"}))