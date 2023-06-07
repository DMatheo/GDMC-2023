from gdpc import Block

from constants import ED, CLIFF_BLOCKS

import random

class Building:

    # Abstract attribute
    DIMENSIONS = None

    # Abstract attribute, must be a tuple (offset, width)
    ENTRY = None

    def __init__(self, name, coord, blocks, facing, settlement):
        self.name = name
        self.coord = coord
        self.settlement = settlement

        if facing not in ['north', 'south', 'east', 'west']:
            raise ValueError("facing must be 'north', 'south', 'east' or 'west'")
            
        self.facing = facing

        new_blocks = []
        if self.facing == 'south':
            for block in blocks:
                new_block = ((block[0][0], block[0][1], self.DIMENSIONS["south"][2] - block[0][2]), block[1], block[2])
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
                new_block = ((self.DIMENSIONS["east"][0] - block[0][2], block[0][1], block[0][0]), block[1], block[2])
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

    def fill_column(self, x, y_start, z, edge_relative_pos=None):
        """
        return false if the column is already filled, true otherwise
        """
        counter = y_start
        block_id = ED.getBlock((x, counter, z)).id
        while not any(block_type in block_id for block_type in ("dirt", "stone", "sand", "terracotta", "grass_block")):
            counter -= 1
            block_id = ED.getBlock((x, counter, z)).id


        height = y_start - counter
        cliff = height > 2

        for y in range(counter, y_start + 1):

            if cliff:
                if y == y_start and random.randint(0,3) != 0:
                    ED.placeBlock((x, y, z), Block(block_id))
                else:
                    ED.placeBlock((x, y, z), Block(random.choices(CLIFF_BLOCKS, weights=(80, 8, 8, 4), k=1)[0]))

            else:
                if block_id == "minecraft:grass_block" and y < y_start:
                    ED.placeBlock((x, y, z), Block("dirt"))
                else:
                    ED.placeBlock((x, y, z), Block(block_id))

        if cliff and edge_relative_pos is not None:
            middle = height // 2
            divided_height = height // edge_relative_pos
            hole_range = divided_height // 2
            if divided_height > 3:
                for y in range(y_start - middle - (hole_range // 2), y_start - middle + (hole_range // 2)):
                    ED.placeBlock((x, y, z), Block("air"))



    def create_natural_lines(self, axis, start_main, end_main, start_secondary, end_secondary, y_start):

        line_number = 1
        while start_secondary < end_secondary:
            for main_axis_details in (start_main - line_number, end_main + line_number):
                while random.randint(0,10) < 8:
                    start_secondary += 1
                while random.randint(0,10) < 8:
                    end_secondary -= 1
                for secondary_axis_details in range(start_secondary, end_secondary):
                    distance_with_start = secondary_axis_details - start_secondary + 1
                    distance_with_end = end_secondary - secondary_axis_details
                    if axis == 'x':
                        self.fill_column(
                            main_axis_details, y_start, 
                            secondary_axis_details, 
                            distance_with_start if distance_with_start < distance_with_end else distance_with_end)
                    elif axis == 'z':
                        self.fill_column(
                            secondary_axis_details, 
                            y_start, main_axis_details, 
                            distance_with_start if distance_with_start < distance_with_end else distance_with_end)
                    else:
                        raise ValueError("axis must be 'x' or 'z'")
            line_number += 1


    def fill_empty_space(self):
        x_start, y_start, z_start = self.coord
        x_start -= 1
        z_start -= 1
        y_start -= 1
        for x in range(x_start, x_start + self.DIMENSIONS[self.facing][0] + 1):
            for z in range(z_start, z_start + self.DIMENSIONS[self.facing][2] + 1):
                self.fill_column(x, y_start, z)

        # make the filling looks more natural
        self.create_natural_lines('x', x_start, x_start + self.DIMENSIONS[self.facing][0], z_start, z_start + self.DIMENSIONS[self.facing][2], y_start)
        self.create_natural_lines('z', z_start, z_start + self.DIMENSIONS[self.facing][2], x_start, x_start + self.DIMENSIONS[self.facing][0], y_start)
        
    def build(self):
        self.fill_empty_space()
        for block in self.blocks:
            x, y, z = self.coord
            relative_x, relative_y, relative_z = block[0]
            x += relative_x
            y += relative_y
            z += relative_z
            if block[1] == "chest":
                ED.placeBlock((x, y, z), Block(block[1], block[2], data={'Items': [{'Slot': '13b', 'id': "apple", 'Count': '1b'}]}))
            else:
                ED.placeBlock((x, y, z), Block(block[1], block[2]))
        self.settlement.buildings.append(self)
    
    def get_blocks(self):
        """
        Abstract method to be implemented in child classes, returns a list of tuples (relative_coord, block_name, block_states)
        """
        pass