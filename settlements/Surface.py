from settlements.Settlement import Settlement
from buildings.Small_house import Small_house

from constants import ED
from gdpc import geometry as geo
from gdpc import Block



import random

class Surface(Settlement):

    def __init__(self, name, location, size):
        super().__init__(name, location, size)
        self.ressources = dict()


    def get_area_altitude_difference_and_maxy(self, start_coord, size):
        worldSlice = ED.loadWorldSlice(geo.Rect(start_coord, size))
        heights = worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
        min = 256
        max = 0
        for height in heights:
            for y in height:
                if y < min:
                    min = y
                if y > max:
                    max = y
        return (max - min, max)
                

    def cut_trees_in_area(self, start_coord, size):
        worldSlice = ED.loadWorldSlice(geo.Rect(start_coord, size))
        heights = worldSlice.heightmaps["MOTION_BLOCKING"]
        x, z = start_coord[0], start_coord[1]
        for height in heights:
            for y in height:
                tmpy = y - 1
                tmpblock_id = ED.getBlock((x, tmpy, z)).id
                while not any(block_type in tmpblock_id for block_type in ("dirt", "stone", "sand", "terracotta", "grass", "water")):
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

    def settle(self):
        self.cut_trees_in_area(self.location, self.size)
        print(self.ressources)
        for x in range(self.location[0], self.location[0] + self.size[0], 20):
            for z in range(self.location[1], self.location[1] + self.size[1], 20):
                alt_diff, maxy = self.get_area_altitude_difference_and_maxy((x, z), (Small_house.NORTH_SOUTH_FACING_DIMENSIONS[0], Small_house.NORTH_SOUTH_FACING_DIMENSIONS[2]))
                if alt_diff < 2:
                    house = Small_house((x, maxy, z), random.choice(("oak", "jungle", "acacia", "spruce")), random.choice(("north", "south", "east", "west")))
                    house.build()
                    z += Small_house.NORTH_SOUTH_FACING_DIMENSIONS[2]