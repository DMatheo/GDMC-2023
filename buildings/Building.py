from gdpc import Block

from constants import ED

# TO DO : needed ressources
class Building:

    def __init__(self, name, coord, dimensions, blocks):
        self.name = name
        self.coord = coord
        self.dimensions = dimensions
        self.blocks = blocks
        self.dimensions = dimensions

    def __str__(self):
        return self.name
    
    def fill_empty_space(self):
        x_start, y_start, z_start = self.coord
        y = y_start - 1
        for x in range(x_start, x_start + self.dimensions[0] + 1):
            for z in range(z_start, z_start + self.dimensions[2] + 1):
                while(y > -64 and ED.getBlock((x, y, z)).id == "minecraft:air"):
                    ED.placeBlock((x, y, z), Block("stone_bricks"))
                    y -= 1
                y = y_start - 1

    def build(self):
        self.fill_empty_space()
        for block in self.blocks:
            x, y, z = self.coord
            relative_x, relative_y, relative_z = block[0]
            x += relative_x
            y += relative_y
            z += relative_z
            ED.placeBlock((x, y, z), Block(block[1], block[2]))
    
    def get_blocks(self):
        """
        Abstract method to be implemented in child classes, returns a list of tuples (relative_coord, block_name, block_states)
        """
        pass