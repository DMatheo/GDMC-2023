from settlements.Settlement import Settlement
from buildings.Small_house import Small_house

from constants import ED, GROUND_BLOCKS, DECORATIVE_GROUND_BLOCKS
from gdpc import geometry as geo
from gdpc import Block

from gdpc.vector_tools import circle

import math
import random

class Surface(Settlement):



    def __init__(self, name, size, cave_location):
        self.ressources = dict()
        self.cave_location = cave_location
        super().__init__(name, self.determine_location(size), size)


    def determine_location(self, size):

        possibles_locations_values = {
            (self.cave_location[0] - size[0], self.cave_location[2] - size[1]): 0,
            (self.cave_location[0] - size[0], self.cave_location[2]): 0,
            (self.cave_location[0], self.cave_location[2] - size[1]): 0,
            (self.cave_location[0], self.cave_location[2]): 0,
        }


        for location in possibles_locations_values.keys():
            for x in range(location[0], location[0] + size[0], 10):
                for z in range(location[1], location[1] + size[1], 10):
                    alt_diff = self.get_area_altitude_difference_with_trees((x, z), (10, 10))
                    water_presence = self.is_water_present((x, z), (10, 10))
                    if alt_diff < 2 and not water_presence:
                        possibles_locations_values[location] += 1

        print(possibles_locations_values)
                
        return max(possibles_locations_values, key=possibles_locations_values.get)

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
        for height in heights:
            for y in height:
                if y < min:
                    min = y
                if y > max:
                    max = y
        return (max - min, max)

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

    def cut_trees_in_area(self, start_coord, size):
        worldSlice = ED.loadWorldSlice(geo.Rect(start_coord, size))
        heights = worldSlice.heightmaps["MOTION_BLOCKING"]
        x, z = start_coord[0], start_coord[1]
        for height in heights:
            for y in height:
                tmpy = y - 1
                tmpblock_id = ED.getBlock((x, tmpy, z)).id
                while not any(block_type in tmpblock_id for block_type in (DECORATIVE_GROUND_BLOCKS + GROUND_BLOCKS)):
                    if tmpblock_id in self.ressources:
                        self.ressources[tmpblock_id] += 1
                    else:
                        self.ressources[tmpblock_id] = 1                        
                    ED.placeBlock((x,tmpy,z), Block("air"))
                    tmpy -= 1
                    tmpblock_id = ED.getBlock((x, tmpy, z)).id
                z += 1
            z = start_coord[1]
            x += 1

    def up_air_col(self, lenght, coord):
        for y in range(coord[1], coord[1] + lenght):
            ED.placeBlock((coord[0], y, coord[2]), Block("air"))

    def create_quarry(self, size):
        x = self.cave_location[0] - size // 2
        z = self.cave_location[2] - size // 2
        max_y = self.get_area_altitude_difference_and_maxy((x, z), (size, size))[1]
        geo.placeCylinder(ED, (self.cave_location), size, max_y - self.cave_location[1], Block("air"))

        circle_coords = circle((self.cave_location[0], self.cave_location[2]), size+2)
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

        #Cut all the trees in the area
        self.cut_trees_in_area(self.location, self.size)

        print("Trees cut.")

        self.create_quarry(20)

        print("Quarry created.")



        #Get the wood_type with the most occurences
        wood_type = "spruce"
        nb_occurences = 0
        for ressource in self.ressources.keys():
            if "log" in ressource and self.ressources[ressource] > nb_occurences:
                nb_occurences = self.ressources[ressource]
                wood_type = ressource.split("log")[0][:-1]

        x_offset = random.randint(0, Small_house.EAST_WEST_FACING_DIMENSIONS[0] + 3)
        z_offset = random.randint(0, Small_house.EAST_WEST_FACING_DIMENSIONS[2] + 3)
        facing = "east"
        for x in range(self.location[0] + x_offset, self.location[0] + self.size[0], Small_house.EAST_WEST_FACING_DIMENSIONS[0] + 10):
            z = self.location[1] + z_offset
            while z < self.location[1] + self.size[1]:
                randx = random.randint(-2, 2) + x
                alt_diff, maxy = self.get_area_altitude_difference_and_maxy((randx, z), (Small_house.EAST_WEST_FACING_DIMENSIONS[0], Small_house.EAST_WEST_FACING_DIMENSIONS[2]))
                water_presence = self.is_water_present((randx, z), (Small_house.EAST_WEST_FACING_DIMENSIONS[0], Small_house.EAST_WEST_FACING_DIMENSIONS[2]))
                if alt_diff < 50 and not water_presence:
                    house = Small_house((randx, maxy, z), wood_type, facing)
                    house.build()
                    self.buildings.append(house)
                    z += house.dimensions[2] + 10
                else:
                    z += 1
            facing = "west" if facing == "east" else "east"

        print("Settling surface settlement done.")