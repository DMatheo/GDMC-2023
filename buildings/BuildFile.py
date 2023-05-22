import random
from buildings.Building import Building

from constants import FLOWERS

# add random flowers, random mossy and cracked stone, random leaves disposition, wood used = wood near the sawmill
class BuildFile(Building):

    def __init__(self, filename, coord, facing):
        file_string = open((filename + ".txt"), 'r').read()
        dimension_string = file_string.split("\n")[0]
        dimension = eval(dimension_string.split(" : ")[1])
        
        file_string = file_string.replace("\n", "")
        file_string = file_string.replace(dimension_string, "", 1)
        blocks = eval(file_string)

        super().__init__(filename, coord, dimension, blocks, facing)

    def __str__(self):
        return f'{self.wood_type} {self.name}'

    def get_blocks(self):
        return self.blocks