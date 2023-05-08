from gdpc import Block

from constants import ED

# TO DO : needed ressources
class Building:

    def __init__(self, name, coord, dimensions, blocks, facing):
        self.name = name
        self.coord = coord

        if facing not in ['north', 'south', 'east', 'west']:
            raise ValueError("facing must be 'north', 'south', 'east' or 'west'")
        self.facing = facing

        if self.facing == 'east' or self.facing == 'west':
            self.dimensions = (dimensions[2], dimensions[1], dimensions[0])
        else:
            self.dimensions = dimensions

        new_blocks = []
        if self.facing == 'south':
            for block in blocks:
                new_block = ((block[0][0], block[0][1], self.dimensions[2] - block[0][2]), block[1], block[2])
                if 'hinge' in block[2]:
                    if block[2]['hinge'] == 'left':
                        new_block[2]['hinge'] = 'right'
                    elif block[2]['hinge'] == 'right':
                        new_block[2]['hinge'] = 'left'
                if 'facing' in block[2]:
                    if block[2]['facing'] == 'south':
                        new_block[2]['facing'] = 'north'
                    elif block[2]['facing'] == 'north':
                        new_block[2]['facing'] = 'south'
                new_blocks.append(new_block)
        elif self.facing == 'west':
            for block in blocks:
                new_block = ((block[0][2], block[0][1], block[0][0]), block[1], block[2])
                if 'hinge' in block[2]:
                    if block[2]['hinge'] == 'left':
                        new_block[2]['hinge'] = 'right'
                    elif block[2]['hinge'] == 'right':
                        new_block[2]['hinge'] = 'left'
                if 'facing' in block[2]:
                    if block[2]['facing'] == 'south':
                        new_block[2]['facing'] = 'east'
                    elif block[2]['facing'] == 'north':
                        new_block[2]['facing'] = 'west'
                    elif block[2]['facing'] == 'west':
                        new_block[2]['facing'] = 'north'
                    elif block[2]['facing'] == 'east':
                        new_block[2]['facing'] = 'south'
                new_blocks.append(new_block)
        elif self.facing == 'east':
            for block in blocks:
                new_block = ((self.dimensions[0] - block[0][2], block[0][1], block[0][0]), block[1], block[2])
                if 'facing' in block[2]:
                    if block[2]['facing'] == 'south':
                        new_block[2]['facing'] = 'west'
                    elif block[2]['facing'] == 'north':
                        new_block[2]['facing'] = 'east'
                    elif block[2]['facing'] == 'west':
                        new_block[2]['facing'] = 'north'
                    elif block[2]['facing'] == 'east':
                        new_block[2]['facing'] = 'south'
                new_blocks.append(new_block)
        else:
            new_blocks = blocks

        self.blocks = list(new_blocks)
        

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