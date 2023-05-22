from gdpc import Block

from constants import ED

import random

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

    def fill_column(self, x, y_start, z):
        counter = y_start
        block_id = ED.getBlock((x, counter, z)).id
        while not any(block_type in block_id for block_type in ("dirt", "stone", "sand", "terracotta", "grass_block")):
            counter -= 1
            block_id = ED.getBlock((x, counter, z)).id
        for y in range(counter, y_start + 1):
            ED.placeBlock((x, y, z), Block(block_id))

    
    def fill_empty_space(self):
        x_start, y_start, z_start = self.coord
        x_start -= 1
        z_start -= 1
        y_start -= 1
        for x in range(x_start, x_start + self.dimensions[0] + 1):
            for z in range(z_start, z_start + self.dimensions[2] + 1):
                self.fill_column(x, y_start, z)

        # make the filling looks more natural
        for x_details in (x_start -1, x_start + self.dimensions[0] + 1):
            z_details_start = z_start
            z_details_end = z_start + self.dimensions[2]
            while random.randint(0,10) < 8:
                z_details_start += 1
            while random.randint(0,10) < 8:
                z_details_end -= 1
            for z_details in range(z_details_start, z_details_end):
                self.fill_column(x_details, y_start, z_details)

        for z_details in (z_start -1, z_start + self.dimensions[2] + 1):
            x_details_start = x_start
            x_details_end = x_start + self.dimensions[0]
            while random.randint(0,10) < 8:
                x_details_start += 1
            while random.randint(0,10) < 8:
                x_details_end -= 1
            for x_details in range(x_details_start, x_details_end):
                self.fill_column(x_details, y_start, z_details)
        

        

    def build(self):
        #self.fill_empty_space()
        for block in self.blocks:
            x, y, z = self.coord
            relative_x, relative_y, relative_z = block[0]
            x += relative_x
            y += relative_y
            z += relative_z
            print(x, y, z)
            ED.placeBlock((x, y, z), Block(block[1], block[2]))
        ED.flushBuffer()
    def get_blocks(self):
        """
        Abstract method to be implemented in child classes, returns a list of tuples (relative_coord, block_name, block_states)
        """
        pass

    def get_dimensions(self):
        return self.dimensions

# Building functions

#Buildings

def get_building_at(ED, coord_start, coord_end):

    startx, starty, startz = coord_start
    maxx, maxy, maxz = coord_start
    blocks = ""
    # needed_ressources = {}

    for x in range(coord_start[0], coord_end[0]):

        for y in range(coord_start[1], coord_end[1]):

            for z in range(coord_start[2], coord_end[2]):

                block = ED.getBlock((x, y, z))
                block_name = block.id[10:]

                if block_name != "air":
                    if x > maxx:
                        maxx = x
                    if y > maxy:
                        maxy = y
                    if z > maxz:
                        maxz = z
                    blocks += f"(({x - startx}, {y - starty}, {z - startz}), '{block.id[10:]}', {block.states}),\n"""
                    # if block_name not in needed_ressources:
                    #     needed_ressources[block_name] = 1
                    # else :
                    #     needed_ressources[block_name] += 1
    text_file = open("miaou.txt", "w")
    
    text_file.write(f"Dimensions : ({maxx - startx}, {maxy - starty}, {maxz - startz})\n\n" + blocks)
    
    text_file.close()
    return f"Dimensions : ({maxx - startx}, {maxy - starty}, {maxz - startz})\n\n" + blocks