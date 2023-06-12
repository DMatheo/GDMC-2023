from settlements.Settlement import Settlement
from buildings.Small_house import Small_house
from settlements.Farm_builder import Farm_builder
from settlements.Road_builder import Road_builder
from settlements.Building_builder import Building_builder

from constants import ED, GROUND_BLOCKS, DECORATIVE_GROUND_BLOCKS, STARTX, STARTZ, LASTX, LASTZ
from gdpc import geometry as geo
from gdpc import Block

from gdpc.vector_tools import circle

import math
import random

class Surface(Settlement):

    MAX_ALTITUDE_DIFFERENCE = 8

    def __init__(self, name, cave_location, cave_size, location, size):
        self.cave_location = cave_location
        self.cave_size = cave_size
        self.location = location
        self.size = size
        super().__init__(name, location, size)

        #Cut all the trees in the area
        self.wood_type = self.cut_trees_in_area(self.location, self.size)
        print("Trees cut.")

        # get worldSlice without trees
        self.worldSlice = ED.loadWorldSlice(geo.Rect(self.location, self.size))

    def get_area_altitude_difference_with_trees(self, start_coord, size):
        worldSlice = ED.loadWorldSlice(geo.Rect(start_coord, size))
        heights = worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
        x, z = start_coord[0], start_coord[1]
        min = 900
        max = -900
        for height in heights:
            for y in height:
                tmpy = y - 1
                tmpblock_id = ED.getBlock((x, tmpy, z)).id
                while not any(block_type in tmpblock_id for block_type in (DECORATIVE_GROUND_BLOCKS + GROUND_BLOCKS)):
                    tmpy -= 1
                    tmpblock_id = ED.getBlock((x, tmpy, z)).id
                tmpy += 1

                if tmpy < min:
                    min = tmpy
                if tmpy > max:
                    max = tmpy
                z += 1
            z = start_coord[1]
            x += 1
        return max - min

    def get_area_altitude_difference_and_maxy(self, start_coord, size):
        worldSlice = ED.loadWorldSlice(geo.Rect(start_coord, size))
        heights = worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
        min = 900
        max = -900
        side_mins = {
            "north": 900,
            "south": 900,
            "west": 900,
            "east": 900
        }
        x, z = start_coord[0], start_coord[1]
        max_x, max_z = start_coord[0] + size[0], start_coord[1] + size[1]
        for height in heights:
            for y in height:
                if y < min:
                    min = y
                if y > max:
                    max = y
                if x == start_coord[0] and y < side_mins["east"]:
                    side_mins["east"] = y
                elif x == max_x - 1 and y < side_mins["west"]:
                    side_mins["west"] = y
                elif z == start_coord[1] and y < side_mins["south"]:
                    side_mins["south"] = y
                elif z == max_z - 1 and y < side_mins["north"]:
                    side_mins["north"] = y
                z += 1
            z = start_coord[1]
            x += 1
        for side in side_mins.keys():
            side_mins[side] = side_mins[side] - min
        return (max - min, max, side_mins)

    def is_water_present(self, start_coord, size):
        worldSlice = ED.loadWorldSlice(geo.Rect(start_coord, size))
        heights = worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
        x, z = start_coord[0], start_coord[1]
        for height in heights:
            for y in height:
                if "water" in ED.getBlock(position=(x, y - 1, z)).id:
                    return True
                z += 1
            z = start_coord[1]
            x += 1
        return False

    def is_practicable(self, start_coord, size):
        return not self.is_water_present(start_coord, size) and self.get_area_altitude_difference_and_maxy(start_coord, size)[0] < self.MAX_ALTITUDE_DIFFERENCE

    def cut_trees_in_area(self, start_coord, size):
        ressources = dict()
        worldSlice = ED.loadWorldSlice(geo.Rect(start_coord, size))
        heights = worldSlice.heightmaps["MOTION_BLOCKING"]
        x, z = start_coord[0], start_coord[1]
        for height in heights:
            for y in height:
                wood_type = ED.getBlock((x, y, z)).id
                tmpy = y - 1
                tmpblock_id = ED.getBlock((x, tmpy, z)).id
                while not any(block_type in tmpblock_id for block_type in (DECORATIVE_GROUND_BLOCKS + GROUND_BLOCKS)):
                    if tmpblock_id in ressources:
                        ressources[tmpblock_id] += 1
                    else:
                        ressources[tmpblock_id] = 1                        
                    ED.placeBlock((x,tmpy,z), Block("air"))
                    tmpy -= 1
                    tmpblock_id = ED.getBlock((x, tmpy, z)).id
                z += 1
            z = start_coord[1]
            x += 1

        # Get the wood_type with the most occurences
        wood_type = "spruce"
        nb_occurences = 0
        for ressource in ressources.keys():
            if "log" in ressource and ressources[ressource] > nb_occurences:
                nb_occurences = ressources[ressource]
                wood_type = ressource.split("log")[0][:-1]
        return wood_type

    def up_air_col(self, lenght, coord):
        for y in range(coord[1], coord[1] + lenght):
            ED.placeBlock((coord[0], y, coord[2]), Block("air"))

    def create_quarry(self):
        x = self.cave_location[0] - self.cave_size // 2
        z = self.cave_location[2] - self.cave_size // 2
        max_y = self.get_area_altitude_difference_and_maxy((x, z), (self.cave_size, self.cave_size))[1]
        geo.placeCylinder(ED, (self.cave_location), self.cave_size, max_y - self.cave_location[1], Block("air"))

        circle_coords = circle((self.cave_location[0], self.cave_location[2]), self.cave_size+2)
        angles = dict()
        for coord in circle_coords:
            x, z = coord[0], coord[1]
            dx = x - self.cave_location[0]
            dz = z - self.cave_location[2]
            angle = math.atan2(dz, dx)
            angles[coord] = angle

        
        sorted_circle_coords = sorted(angles, key=angles.get)

        y = max_y
        if len(sorted_circle_coords) != 0:
            while y > self.cave_location[1]:
                for coord in sorted_circle_coords:
                    self.up_air_col(6, (coord[0], y, coord[1]))
                    y -= 1
                    if y == self.cave_location[1]:
                        break
    
    def settle(self):

        print("Settling surface settlement...")

        self.create_quarry()

        print("Quarry created.")

        road_builder = Road_builder(self)
        road_builder.calculate_main_roads()
        road = road_builder.get_best_road()
        road_builder.create_road(road)

        print("Main road created.")

        farm_builder = Farm_builder(self)
        farm_builder.create_farm(road)

        print("Farm created.")

        builder = Building_builder(self)

        # Buildings along farm road
        available_spaces = builder.place_buildings_along_road(road)
        road_builder.calculate_roads_from_spaces(available_spaces, width=2)

        # One street (road + buildings in both sides) by iteration
        while any(not road["built"] for road in road_builder.roads):

            road = road_builder.get_best_road()
            road_builder.create_road(road)

            available_spaces = builder.place_buildings_along_road(road)
            road_builder.calculate_roads_from_spaces(available_spaces, width=2)

            print("Street created.")
        
        print("Settling surface settlement done.")