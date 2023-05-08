import random
from buildings.Building import Building

from constants import FLOWERS

# add random flowers, random mossy and cracked stone, random leaves disposition, wood used = wood near the sawmill
class Small_house(Building):

    def __init__(self, coord, wood_type, facing):
        self.wood_type = wood_type
        super().__init__("Small_house", coord, (15, 13, 12), self.get_blocks(), facing)

    def __str__(self):
        return f'{self.wood_type} {self.name}'
        
    def get_blocks(self):
        return (
            (
                ((0, 0, 3), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '2', 'persistent': 'true'}),
                ((0, 0, 4), 'stone_brick_wall', {
                    'east': 'tall', 'waterlogged': 'false', 'south': 'none', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((0, 0, 7), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((0, 0, 8), 'stone_brick_wall', {
                    'east': 'tall', 'waterlogged': 'false', 'south': 'none', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((0, 1, 4), f'{self.wood_type}_log', {'axis': 'x'}),
                ((0, 1, 5), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((0, 1, 6), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((0, 1, 7), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((0, 1, 8), f'{self.wood_type}_log', {'axis': 'x'}),
                ((0, 2, 3), f'{self.wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((0, 2, 4), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((0, 2, 5), 'grass_block', {'snowy': 'false'}),
                ((0, 2, 6), 'grass_block', {'snowy': 'false'}),
                ((0, 2, 7), 'grass_block', {'snowy': 'false'}),
                ((0, 2, 8), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((0, 2, 9), f'{self.wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((0, 3, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((0, 3, 4), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((0, 3, 5), f'{random.choice(FLOWERS)}', {}),
                ((0, 3, 6), f'{random.choice(FLOWERS)}', {}),
                ((0, 3, 7), f'{random.choice(FLOWERS)}', {}),
                ((0, 3, 8), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((0, 3, 9), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((0, 4, 4), f'{self.wood_type}_planks', {}),
                ((0, 4, 8), f'{self.wood_type}_planks', {}),
                ((0, 5, 4), f'{self.wood_type}_planks', {}),
                ((0, 5, 8), f'{self.wood_type}_planks', {}),
                ((0, 6, 4), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((0, 6, 5), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((0, 6, 7), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((0, 6, 8), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((0, 7, 5), f'{self.wood_type}_planks', {}),
                ((0, 7, 7), f'{self.wood_type}_planks', {}),
                ((0, 8, 5), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((0, 8, 6), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((0, 8, 7), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((0, 9, 6), f'{self.wood_type}_planks', {}),
                ((1, 0, 2), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '2', 'persistent': 'true'}),
                ((1, 0, 3), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((1, 0, 4), f'{self.wood_type}_log', {'axis': 'y'}),
                ((1, 0, 5), 'stone_bricks', {}),
                ((1, 0, 6), 'stone_bricks', {}),
                ((1, 0, 7), 'stone_bricks', {}),
                ((1, 0, 8), f'{self.wood_type}_log', {'axis': 'y'}),
                ((1, 1, 3), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((1, 1, 4), f'{self.wood_type}_log', {'axis': 'y'}),
                ((1, 1, 5), f'{self.wood_type}_log', {'axis': 'z'}),
                ((1, 1, 6), f'{self.wood_type}_log', {'axis': 'z'}),
                ((1, 1, 7), f'{self.wood_type}_log', {'axis': 'z'}),
                ((1, 1, 8), f'{self.wood_type}_log', {'axis': 'y'}),
                ((1, 2, 4), f'{self.wood_type}_log', {'axis': 'y'}),
                ((1, 2, 5), 'white_wool', {}),
                ((1, 2, 6), 'white_wool', {}),
                ((1, 2, 7), 'white_wool', {}),
                ((1, 2, 8), f'{self.wood_type}_log', {'axis': 'y'}),
                ((1, 3, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((1, 3, 4), f'{self.wood_type}_log', {'axis': 'y'}),
                ((1, 3, 5), 'white_wool', {}),
                ((1, 3, 6), 'glass_pane', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((1, 3, 7), 'white_wool', {}),
                ((1, 3, 8), f'{self.wood_type}_log', {'axis': 'y'}),
                ((1, 3, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((1, 4, 4), 'cut_copper', {}),
                ((1, 4, 5), 'white_wool', {}),
                ((1, 4, 6), 'glass_pane', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((1, 4, 7), 'white_wool', {}),
                ((1, 4, 8), 'cut_copper', {}),
                ((1, 5, 4), 'cut_copper', {}),
                ((1, 5, 5), 'white_wool', {}),
                ((1, 5, 6), 'glass_pane', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((1, 5, 7), 'white_wool', {}),
                ((1, 5, 8), 'cut_copper', {}),
                ((1, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((1, 6, 5), 'white_wool', {}),
                ((1, 6, 6), 'white_wool', {}),
                ((1, 6, 7), 'white_wool', {}),
                ((1, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((1, 7, 5), 'cut_copper', {}),
                ((1, 7, 6), 'white_wool', {}),
                ((1, 7, 7), 'cut_copper', {}),
                ((1, 8, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((1, 8, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((1, 9, 6), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((2, 0, 2), 'stone_bricks', {}),
                ((2, 0, 3), 'stone_bricks', {}),
                ((2, 0, 4), 'stone_bricks', {}),
                ((2, 0, 8), 'stone_bricks', {}),
                ((2, 1, 2), 'stone_brick_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((2, 1, 3), 'stone_bricks', {}),
                ((2, 1, 4), f'{self.wood_type}_log', {'axis': 'x'}),
                ((2, 1, 5), f'{self.wood_type}_planks', {}),
                ((2, 1, 6), f'{self.wood_type}_planks', {}),
                ((2, 1, 7), f'{self.wood_type}_planks', {}),
                ((2, 1, 8), f'{self.wood_type}_log', {'axis': 'x'}),
                ((2, 2, 3), f'{self.wood_type}_planks', {}),
                ((2, 2, 4), 'white_wool', {}),
                ((2, 2, 7), 'lectern', {'has_book': 'false',
                                        'powered': 'false', 'facing': 'north'}),
                ((2, 2, 8), 'white_wool', {}),
                ((2, 3, 2), 'wall_torch', {'facing': 'north'}),
                ((2, 3, 3), f'{self.wood_type}_planks', {}),
                ((2, 3, 4), 'white_wool', {}),
                ((2, 3, 8), 'white_wool', {}),
                ((2, 3, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((2, 4, 3), f'{self.wood_type}_planks', {}),
                ((2, 4, 4), 'cut_copper', {}),
                ((2, 4, 5), f'{self.wood_type}_wall_sign', {
                    'waterlogged': 'false', 'facing': 'east'}),
                ((2, 4, 8), 'cut_copper', {}),
                ((2, 5, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((2, 5, 4), 'cut_copper', {}),
                ((2, 5, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((2, 5, 8), 'cut_copper', {}),
                ((2, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((2, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((2, 6, 6), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((2, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((2, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((2, 7, 5), 'cut_copper', {}),
                ((2, 7, 6), 'white_wool', {}),
                ((2, 7, 7), 'cut_copper', {}),
                ((2, 8, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((2, 8, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((2, 9, 6), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((3, 0, 2), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((3, 0, 4), 'stone_bricks', {}),
                ((3, 0, 8), 'stone_bricks', {}),
                ((3, 1, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((3, 1, 4), f'{self.wood_type}_planks', {}),
                ((3, 1, 5), f'{self.wood_type}_planks', {}),
                ((3, 1, 6), f'{self.wood_type}_planks', {}),
                ((3, 1, 7), f'{self.wood_type}_planks', {}),
                ((3, 1, 8), f'{self.wood_type}_log', {'axis': 'x'}),
                ((3, 2, 4), f'{self.wood_type}_door', {'hinge': 'right', 'half': 'lower',
                                         'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((3, 2, 7), 'bookshelf', {}),
                ((3, 2, 8), 'white_wool', {}),
                ((3, 3, 4), f'{self.wood_type}_door', {'hinge': 'right', 'half': 'upper',
                                         'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((3, 3, 8), 'white_wool', {}),
                ((3, 3, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((3, 4, 4), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((3, 4, 8), 'cut_copper', {}),
                ((3, 5, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((3, 5, 4), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((3, 5, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((3, 5, 8), 'cut_copper', {}),
                ((3, 6, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((3, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_right', 'facing': 'east'}),
                ((3, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((3, 6, 6), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((3, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((3, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((3, 7, 5), 'cut_copper', {}),
                ((3, 7, 6), 'white_wool', {}),
                ((3, 7, 7), 'cut_copper', {}),
                ((3, 8, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((3, 8, 6), 'white_wool', {}),
                ((3, 8, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((3, 9, 6), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((4, 0, 2), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((4, 0, 4), 'stone_bricks', {}),
                ((4, 0, 8), 'stone_bricks', {}),
                ((4, 0, 9), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '3', 'persistent': 'true'}),
                ((4, 1, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((4, 1, 4), f'{self.wood_type}_planks', {}),
                ((4, 1, 5), f'{self.wood_type}_planks', {}),
                ((4, 1, 6), f'{self.wood_type}_planks', {}),
                ((4, 1, 7), f'{self.wood_type}_planks', {}),
                ((4, 1, 8), f'{self.wood_type}_log', {'axis': 'x'}),
                ((4, 2, 4), f'{self.wood_type}_door', {'hinge': 'left', 'half': 'lower',
                                         'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((4, 2, 7), 'bookshelf', {}),
                ((4, 2, 8), 'white_wool', {}),
                ((4, 3, 4), f'{self.wood_type}_door', {'hinge': 'left', 'half': 'upper',
                                         'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((4, 3, 7), 'bookshelf', {}),
                ((4, 3, 8), 'white_wool', {}),
                ((4, 3, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((4, 4, 4), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((4, 4, 7), 'bookshelf', {}),
                ((4, 4, 8), 'cut_copper', {}),
                ((4, 4, 9), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((4, 5, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((4, 5, 4), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((4, 5, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((4, 5, 8), 'cut_copper', {}),
                ((4, 6, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((4, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_right', 'facing': 'south'}),
                ((4, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((4, 6, 6), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((4, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((4, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((4, 7, 5), 'cut_copper', {}),
                ((4, 7, 6), 'lantern', {
                    'waterlogged': 'false', 'hanging': 'true'}),
                ((4, 7, 7), 'cut_copper', {}),
                ((4, 8, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((4, 8, 6), 'white_wool', {}),
                ((4, 8, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((4, 9, 6), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((5, 0, 2), 'stone_bricks', {}),
                ((5, 0, 3), 'stone_bricks', {}),
                ((5, 0, 4), 'stone_bricks', {}),
                ((5, 0, 8), 'stone_bricks', {}),
                ((5, 0, 9), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '2', 'persistent': 'true'}),
                ((5, 0, 10), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((5, 1, 2), 'stone_brick_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((5, 1, 3), 'stone_bricks', {}),
                ((5, 1, 4), f'{self.wood_type}_log', {'axis': 'x'}),
                ((5, 1, 5), f'{self.wood_type}_planks', {}),
                ((5, 1, 6), f'{self.wood_type}_planks', {}),
                ((5, 1, 7), f'{self.wood_type}_planks', {}),
                ((5, 1, 8), f'{self.wood_type}_log', {'axis': 'x'}),
                ((5, 1, 9), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((5, 2, 1), f'{self.wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((5, 2, 3), f'{self.wood_type}_planks', {}),
                ((5, 2, 4), 'white_wool', {}),
                ((5, 2, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((5, 2, 8), 'white_wool', {}),
                ((5, 2, 11), f'{self.wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((5, 3, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((5, 3, 2), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((5, 3, 3), f'{self.wood_type}_planks', {}),
                ((5, 3, 4), 'white_wool', {}),
                ((5, 3, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((5, 3, 8), 'white_wool', {}),
                ((5, 3, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((5, 3, 10), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((5, 3, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((5, 4, 3), f'{self.wood_type}_planks', {}),
                ((5, 4, 4), 'cut_copper', {}),
                ((5, 4, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((5, 4, 8), 'cut_copper', {}),
                ((5, 4, 9), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((5, 5, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((5, 5, 4), 'cut_copper', {}),
                ((5, 5, 8), 'cut_copper', {}),
                ((5, 5, 9), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((5, 6, 4), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((5, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((5, 6, 6), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((5, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((5, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((5, 7, 5), 'cut_copper', {}),
                ((5, 7, 6), 'white_wool', {}),
                ((5, 7, 7), 'cut_copper', {}),
                ((5, 8, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((5, 8, 6), 'white_wool', {}),
                ((5, 8, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((5, 9, 6), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((6, 0, 1), 'stone_brick_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((6, 0, 2), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 0, 3), 'stone_bricks', {}),
                ((6, 0, 4), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 0, 8), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 0, 9), 'stone_bricks', {}),
                ((6, 0, 10), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 0, 11), 'stone_brick_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'none', 'north': 'tall', 'west': 'none', 'up': 'true'}),
                ((6, 1, 0), f'{self.wood_type}_button', {'face': 'wall',
                                           'powered': 'false', 'facing': 'north'}),
                ((6, 1, 1), f'{self.wood_type}_log', {'axis': 'z'}),
                ((6, 1, 2), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 1, 3), f'{self.wood_type}_log', {'axis': 'z'}),
                ((6, 1, 4), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 1, 5), f'{self.wood_type}_planks', {}),
                ((6, 1, 6), f'{self.wood_type}_planks', {}),
                ((6, 1, 7), f'{self.wood_type}_planks', {}),
                ((6, 1, 8), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 1, 9), f'{self.wood_type}_log', {'axis': 'z'}),
                ((6, 1, 10), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 1, 11), f'{self.wood_type}_log', {'axis': 'z'}),
                ((6, 1, 12), f'{self.wood_type}_button', {
                    'face': 'wall', 'powered': 'false', 'facing': 'south'}),
                ((6, 2, 1), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((6, 2, 2), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 2, 3), 'white_wool', {}),
                ((6, 2, 4), 'white_wool', {}),
                ((6, 2, 5), 'white_wool', {}),
                ((6, 2, 6), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((6, 2, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((6, 2, 8), 'white_wool', {}),
                ((6, 2, 9), 'white_wool', {}),
                ((6, 2, 10), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 2, 11), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((6, 3, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((6, 3, 2), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 3, 3), 'white_wool', {}),
                ((6, 3, 4), 'white_wool', {}),
                ((6, 3, 5), 'white_wool', {}),
                ((6, 3, 6), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((6, 3, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((6, 3, 8), 'white_wool', {}),
                ((6, 3, 9), 'white_wool', {}),
                ((6, 3, 10), f'{self.wood_type}_log', {'axis': 'y'}),
                ((6, 3, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((6, 4, 1), f'{self.wood_type}_planks', {}),
                ((6, 4, 2), 'cut_copper', {}),
                ((6, 4, 3), 'cut_copper', {}),
                ((6, 4, 4), 'cut_copper', {}),
                ((6, 4, 5), 'white_wool', {}),
                ((6, 4, 6), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((6, 4, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((6, 4, 8), 'cut_copper', {}),
                ((6, 4, 9), 'cut_copper', {}),
                ((6, 4, 10), 'cut_copper', {}),
                ((6, 4, 11), f'{self.wood_type}_planks', {}),
                ((6, 5, 1), f'{self.wood_type}_planks', {}),
                ((6, 5, 2), 'cut_copper', {}),
                ((6, 5, 3), 'cut_copper', {}),
                ((6, 5, 4), 'cut_copper', {}),
                ((6, 5, 5), 'white_wool', {}),
                ((6, 5, 6), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((6, 5, 7), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((6, 5, 8), 'cut_copper', {}),
                ((6, 5, 9), 'cut_copper', {}),
                ((6, 5, 10), 'cut_copper', {}),
                ((6, 5, 11), f'{self.wood_type}_planks', {}),
                ((6, 6, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((6, 6, 2), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((6, 6, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((6, 6, 4), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((6, 6, 5), 'cut_copper', {}),
                ((6, 6, 6), 'cut_copper', {}),
                ((6, 6, 7), 'cut_copper', {}),
                ((6, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_right', 'facing': 'north'}),
                ((6, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((6, 6, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((6, 6, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((6, 7, 4), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((6, 7, 5), 'cut_copper', {}),
                ((6, 7, 6), 'white_wool', {}),
                ((6, 7, 7), 'cut_copper', {}),
                ((6, 7, 8), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((6, 8, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((6, 8, 7), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((6, 9, 6), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((7, 0, 2), 'stone_bricks', {}),
                ((7, 0, 10), 'stone_bricks', {}),
                ((7, 1, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((7, 1, 2), f'{self.wood_type}_log', {'axis': 'x'}),
                ((7, 1, 3), f'{self.wood_type}_planks', {}),
                ((7, 1, 4), f'{self.wood_type}_planks', {}),
                ((7, 1, 5), f'{self.wood_type}_planks', {}),
                ((7, 1, 6), f'{self.wood_type}_planks', {}),
                ((7, 1, 7), f'{self.wood_type}_planks', {}),
                ((7, 1, 8), f'{self.wood_type}_planks', {}),
                ((7, 1, 9), f'{self.wood_type}_planks', {}),
                ((7, 1, 10), f'{self.wood_type}_log', {'axis': 'x'}),
                ((7, 1, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((7, 2, 0), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((7, 2, 1), 'grass_block', {'snowy': 'false'}),
                ((7, 2, 2), 'white_wool', {}),
                ((7, 2, 3), 'black_bed', {'part': 'head',
                                          'facing': 'west', 'occupied': 'false'}),
                ((7, 2, 5), 'white_wool', {}),
                ((7, 2, 8), 'furnace', {'lit': 'false', 'facing': 'east'}),
                ((7, 2, 9), 'furnace', {'lit': 'false', 'facing': 'east'}),
                ((7, 2, 10), 'white_wool', {}),
                ((7, 2, 11), 'grass_block', {'snowy': 'false'}),
                ((7, 2, 12), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((7, 3, 1), f'{random.choice(FLOWERS)}', {}),
                ((7, 3, 2), 'white_wool', {}),
                ((7, 3, 3), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((7, 3, 5), 'white_wool', {}),
                ((7, 3, 8), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'tall', 'up': 'true'}),
                ((7, 3, 9), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'tall', 'west': 'tall', 'up': 'true'}),
                ((7, 3, 10), 'white_wool', {}),
                ((7, 3, 11), f'{random.choice(FLOWERS)}', {}),
                ((7, 4, 2), 'white_wool', {}),
                ((7, 4, 3), 'lantern', {
                    'waterlogged': 'false', 'hanging': 'false'}),
                ((7, 4, 4), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((7, 4, 5), 'white_wool', {}),
                ((7, 4, 8), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'tall', 'up': 'true'}),
                ((7, 4, 9), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'tall', 'west': 'tall', 'up': 'true'}),
                ((7, 4, 10), 'white_wool', {}),
                ((7, 5, 2), 'white_wool', {}),
                ((7, 5, 5), 'white_wool', {}),
                ((7, 5, 8), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'tall', 'up': 'true'}),
                ((7, 5, 9), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'tall', 'west': 'tall', 'up': 'true'}),
                ((7, 5, 10), 'white_wool', {}),
                ((7, 6, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((7, 6, 2), 'white_wool', {}),
                ((7, 6, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((7, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((7, 6, 5), 'white_wool', {}),
                ((7, 6, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((7, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((7, 6, 8), 'cut_copper', {}),
                ((7, 6, 9), 'cut_copper', {}),
                ((7, 6, 10), 'white_wool', {}),
                ((7, 6, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((7, 7, 1), f'{self.wood_type}_planks', {}),
                ((7, 7, 2), 'cut_copper', {}),
                ((7, 7, 3), 'cut_copper', {}),
                ((7, 7, 4), 'cut_copper', {}),
                ((7, 7, 5), 'cut_copper', {}),
                ((7, 7, 6), 'white_wool', {}),
                ((7, 7, 7), 'cut_copper', {}),
                ((7, 7, 8), 'cut_copper', {}),
                ((7, 7, 9), 'cut_copper', {}),
                ((7, 7, 10), 'cut_copper', {}),
                ((7, 7, 11), f'{self.wood_type}_planks', {}),
                ((7, 8, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 8, 2), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 8, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 8, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 8, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_right', 'facing': 'east'}),
                ((7, 8, 7), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((7, 8, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 8, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 8, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 8, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 9, 6), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 0, 2), 'stone_bricks', {}),
                ((8, 0, 10), 'stone_bricks', {}),
                ((8, 1, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((8, 1, 2), f'{self.wood_type}_log', {'axis': 'x'}),
                ((8, 1, 3), f'{self.wood_type}_planks', {}),
                ((8, 1, 4), f'{self.wood_type}_planks', {}),
                ((8, 1, 5), f'{self.wood_type}_planks', {}),
                ((8, 1, 6), f'{self.wood_type}_planks', {}),
                ((8, 1, 7), f'{self.wood_type}_planks', {}),
                ((8, 1, 8), f'{self.wood_type}_planks', {}),
                ((8, 1, 9), f'{self.wood_type}_planks', {}),
                ((8, 1, 10), f'{self.wood_type}_log', {'axis': 'x'}),
                ((8, 1, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((8, 2, 0), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((8, 2, 1), 'grass_block', {'snowy': 'false'}),
                ((8, 2, 2), 'white_wool', {}),
                ((8, 2, 3), 'black_bed', {'part': 'foot',
                                          'facing': 'west', 'occupied': 'false'}),
                ((8, 2, 5), f'{self.wood_type}_door', {'hinge': 'left', 'half': 'lower',
                                         'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((8, 2, 10), 'white_wool', {}),
                ((8, 2, 11), 'grass_block', {'snowy': 'false'}),
                ((8, 2, 12), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((8, 3, 1), f'{random.choice(FLOWERS)}', {}),
                ((8, 3, 2), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((8, 3, 5), f'{self.wood_type}_door', {'hinge': 'left', 'half': 'upper',
                                         'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((8, 3, 10), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((8, 3, 11), f'{random.choice(FLOWERS)}', {}),
                ((8, 4, 2), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((8, 4, 5), 'white_wool', {}),
                ((8, 4, 6), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((8, 4, 10), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((8, 5, 2), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((8, 5, 5), 'white_wool', {}),
                ((8, 5, 6), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((8, 5, 10), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((8, 6, 2), 'white_wool', {}),
                ((8, 6, 3), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((8, 6, 4), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((8, 6, 5), 'white_wool', {}),
                ((8, 6, 6), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((8, 6, 7), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((8, 6, 8), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((8, 6, 9), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((8, 6, 10), 'white_wool', {}),
                ((8, 7, 2), 'white_wool', {}),
                ((8, 7, 3), 'white_wool', {}),
                ((8, 7, 4), 'lantern', {
                    'waterlogged': 'false', 'hanging': 'true'}),
                ((8, 7, 5), 'white_wool', {}),
                ((8, 7, 6), 'white_wool', {}),
                ((8, 7, 7), 'white_wool', {}),
                ((8, 7, 8), 'lantern', {
                    'waterlogged': 'false', 'hanging': 'true'}),
                ((8, 7, 9), 'white_wool', {}),
                ((8, 7, 10), 'white_wool', {}),
                ((8, 8, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((8, 8, 4), 'white_wool', {}),
                ((8, 8, 8), 'white_wool', {}),
                ((8, 8, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((8, 9, 1), f'{self.wood_type}_planks', {}),
                ((8, 9, 2), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 9, 3), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 9, 4), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 9, 5), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 9, 6), 'diorite', {}),
                ((8, 9, 7), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 9, 8), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 9, 9), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 9, 10), f'{self.wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 9, 11), f'{self.wood_type}_planks', {}),
                ((8, 10, 6), 'diorite', {}),
                ((8, 11, 6), 'diorite_wall', {'east': 'none', 'waterlogged': 'false',
                                              'south': 'none', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((8, 12, 6), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((9, 0, 1), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((9, 0, 2), 'stone_bricks', {}),
                ((9, 0, 10), 'stone_bricks', {}),
                ((9, 1, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((9, 1, 2), f'{self.wood_type}_log', {'axis': 'x'}),
                ((9, 1, 3), f'{self.wood_type}_planks', {}),
                ((9, 1, 4), f'{self.wood_type}_planks', {}),
                ((9, 1, 5), f'{self.wood_type}_planks', {}),
                ((9, 1, 6), f'{self.wood_type}_planks', {}),
                ((9, 1, 7), f'{self.wood_type}_planks', {}),
                ((9, 1, 8), f'{self.wood_type}_planks', {}),
                ((9, 1, 9), f'{self.wood_type}_planks', {}),
                ((9, 1, 10), f'{self.wood_type}_log', {'axis': 'x'}),
                ((9, 1, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((9, 2, 0), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((9, 2, 1), 'grass_block', {'snowy': 'false'}),
                ((9, 2, 2), 'white_wool', {}),
                ((9, 2, 3), 'bookshelf', {}),
                ((9, 2, 4), 'bookshelf', {}),
                ((9, 2, 5), 'white_wool', {}),
                ((9, 2, 9), 'smooth_stone_slab', {
                    'waterlogged': 'false', 'type': 'double'}),
                ((9, 2, 10), 'white_wool', {}),
                ((9, 2, 11), 'grass_block', {'snowy': 'false'}),
                ((9, 2, 12), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((9, 3, 1), f'{random.choice(FLOWERS)}', {}),
                ((9, 3, 2), 'white_wool', {}),
                ((9, 3, 3), 'bookshelf', {}),
                ((9, 3, 4), 'bookshelf', {}),
                ((9, 3, 5), 'white_wool', {}),
                ((9, 3, 10), 'white_wool', {}),
                ((9, 3, 11), f'{random.choice(FLOWERS)}', {}),
                ((9, 4, 2), 'white_wool', {}),
                ((9, 4, 3), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((9, 4, 4), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((9, 4, 5), 'white_wool', {}),
                ((9, 4, 6), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((9, 4, 8), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((9, 4, 9), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((9, 4, 10), 'white_wool', {}),
                ((9, 5, 2), 'white_wool', {}),
                ((9, 5, 5), 'white_wool', {}),
                ((9, 5, 6), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((9, 5, 8), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((9, 5, 9), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((9, 5, 10), 'white_wool', {}),
                ((9, 6, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((9, 6, 2), 'white_wool', {}),
                ((9, 6, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((9, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((9, 6, 5), 'white_wool', {}),
                ((9, 6, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((9, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((9, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((9, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((9, 6, 10), 'white_wool', {}),
                ((9, 6, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((9, 7, 1), f'{self.wood_type}_planks', {}),
                ((9, 7, 2), 'cut_copper', {}),
                ((9, 7, 3), 'cut_copper', {}),
                ((9, 7, 4), 'cut_copper', {}),
                ((9, 7, 5), 'diorite', {}),
                ((9, 7, 6), 'cut_copper', {}),
                ((9, 7, 7), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((9, 7, 8), 'cut_copper', {}),
                ((9, 7, 9), 'cut_copper', {}),
                ((9, 7, 10), 'cut_copper', {}),
                ((9, 7, 11), f'{self.wood_type}_planks', {}),
                ((9, 8, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((9, 8, 2), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((9, 8, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((9, 8, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((9, 8, 5), 'diorite', {}),
                ((9, 8, 6), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((9, 8, 7), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((9, 8, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((9, 8, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((9, 8, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((9, 8, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((9, 9, 5), 'diorite', {}),
                ((9, 9, 6), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((9, 10, 5), 'diorite', {}),
                ((9, 11, 5), 'diorite', {}),
                ((9, 12, 5), 'diorite_wall', {'east': 'none', 'waterlogged': 'false',
                                              'south': 'none', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((9, 13, 5), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((10, 0, 0), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((10, 0, 1), 'stone_brick_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((10, 0, 2), f'{self.wood_type}_log', {'axis': 'y'}),
                ((10, 0, 3), 'stone_bricks', {}),
                ((10, 0, 4), 'stone_bricks', {}),
                ((10, 0, 5), 'stone_bricks', {}),
                ((10, 0, 6), 'stone_bricks', {}),
                ((10, 0, 7), 'stone_bricks', {}),
                ((10, 0, 8), 'stone_bricks', {}),
                ((10, 0, 9), 'stone_bricks', {}),
                ((10, 0, 10), f'{self.wood_type}_log', {'axis': 'y'}),
                ((10, 0, 11), 'stone_brick_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'none', 'north': 'tall', 'west': 'none', 'up': 'true'}),
                ((10, 1, 0), f'{self.wood_type}_button', {
                    'face': 'wall', 'powered': 'false', 'facing': 'north'}),
                ((10, 1, 1), f'{self.wood_type}_log', {'axis': 'z'}),
                ((10, 1, 2), f'{self.wood_type}_log', {'axis': 'y'}),
                ((10, 1, 3), f'{self.wood_type}_log', {'axis': 'z'}),
                ((10, 1, 4), f'{self.wood_type}_log', {'axis': 'z'}),
                ((10, 1, 5), f'{self.wood_type}_log', {'axis': 'z'}),
                ((10, 1, 6), f'{self.wood_type}_log', {'axis': 'z'}),
                ((10, 1, 7), f'{self.wood_type}_planks', {}),
                ((10, 1, 8), f'{self.wood_type}_planks', {}),
                ((10, 1, 9), f'{self.wood_type}_log', {'axis': 'z'}),
                ((10, 1, 10), f'{self.wood_type}_log', {'axis': 'y'}),
                ((10, 1, 11), f'{self.wood_type}_log', {'axis': 'z'}),
                ((10, 1, 12), f'{self.wood_type}_button', {
                    'face': 'wall', 'powered': 'false', 'facing': 'south'}),
                ((10, 2, 1), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((10, 2, 2), f'{self.wood_type}_log', {'axis': 'y'}),
                ((10, 2, 3), 'white_wool', {}),
                ((10, 2, 4), 'white_wool', {}),
                ((10, 2, 5), 'white_wool', {}),
                ((10, 2, 6), 'white_wool', {}),
                ((10, 2, 7), f'{self.wood_type}_door', {'hinge': 'right', 'half': 'lower',
                                          'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((10, 2, 8), f'{self.wood_type}_door', {'hinge': 'left', 'half': 'lower',
                                          'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((10, 2, 9), 'white_wool', {}),
                ((10, 2, 10), f'{self.wood_type}_log', {'axis': 'y'}),
                ((10, 2, 11), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((10, 3, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 3, 2), f'{self.wood_type}_log', {'axis': 'y'}),
                ((10, 3, 3), 'white_wool', {}),
                ((10, 3, 4), 'white_wool', {}),
                ((10, 3, 5), 'white_wool', {}),
                ((10, 3, 6), 'white_wool', {}),
                ((10, 3, 7), f'{self.wood_type}_door', {'hinge': 'right', 'half': 'upper',
                                          'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((10, 3, 8), f'{self.wood_type}_door', {'hinge': 'left', 'half': 'upper',
                                          'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((10, 3, 9), 'white_wool', {}),
                ((10, 3, 10), f'{self.wood_type}_log', {'axis': 'y'}),
                ((10, 3, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 4, 1), f'{self.wood_type}_planks', {}),
                ((10, 4, 2), 'cut_copper', {}),
                ((10, 4, 3), 'cut_copper', {}),
                ((10, 4, 4), 'cut_copper', {}),
                ((10, 4, 5), 'cut_copper', {}),
                ((10, 4, 6), 'cut_copper', {}),
                ((10, 4, 7), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((10, 4, 8), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((10, 4, 9), 'cut_copper', {}),
                ((10, 4, 10), 'cut_copper', {}),
                ((10, 4, 11), f'{self.wood_type}_planks', {}),
                ((10, 5, 1), f'{self.wood_type}_planks', {}),
                ((10, 5, 2), 'cut_copper', {}),
                ((10, 5, 3), 'cut_copper', {}),
                ((10, 5, 4), 'cut_copper', {}),
                ((10, 5, 5), 'cut_copper', {}),
                ((10, 5, 6), 'cut_copper', {}),
                ((10, 5, 7), 'cut_copper', {}),
                ((10, 5, 8), 'cut_copper', {}),
                ((10, 5, 9), 'cut_copper', {}),
                ((10, 5, 10), 'cut_copper', {}),
                ((10, 5, 11), f'{self.wood_type}_planks', {}),
                ((10, 6, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 2), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 6, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 7, 6), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((11, 0, 2), 'stone_bricks', {}),
                ((11, 0, 3), 'stone_bricks', {}),
                ((11, 0, 4), 'stone_bricks', {}),
                ((11, 0, 5), 'stone_bricks', {}),
                ((11, 0, 6), 'stone_bricks', {}),
                ((11, 0, 7), 'stone_bricks', {}),
                ((11, 0, 8), 'stone_bricks', {}),
                ((11, 0, 9), 'stone_bricks', {}),
                ((11, 0, 10), 'stone_bricks', {}),
                ((11, 0, 11), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((11, 1, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_left', 'facing': 'north'}),
                ((11, 1, 4), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 1, 5), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 1, 6), f'{self.wood_type}_planks', {}),
                ((11, 1, 7), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 1, 8), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 1, 9), f'{self.wood_type}_planks', {}),
                ((11, 1, 10), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((11, 2, 1), f'{self.wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((11, 2, 6), f'{self.wood_type}_planks', {}),
                ((11, 2, 9), f'{self.wood_type}_planks', {}),
                ((11, 2, 11), f'{self.wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((11, 3, 1), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 3, 2), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 3, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 3, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 3, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 3, 6), f'{self.wood_type}_planks', {}),
                ((11, 3, 9), f'{self.wood_type}_planks', {}),
                ((11, 3, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 3, 11), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 4, 2), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((11, 4, 3), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((11, 4, 4), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((11, 4, 5), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((11, 4, 6), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((11, 4, 7), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((11, 4, 8), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((11, 4, 9), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((11, 5, 7), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((11, 5, 8), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((12, 0, 2), 'stone_bricks', {}),
                ((12, 0, 3), 'stone_bricks', {}),
                ((12, 0, 4), 'stone_bricks', {}),
                ((12, 0, 5), 'stone_bricks', {}),
                ((12, 0, 6), 'stone_bricks', {}),
                ((12, 0, 7), 'stone_bricks', {}),
                ((12, 0, 8), 'stone_bricks', {}),
                ((12, 0, 9), 'stone_bricks', {}),
                ((12, 0, 10), 'stone_bricks', {}),
                ((12, 0, 11), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((12, 1, 3), f'{self.wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((12, 1, 4), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'false'}),
                ((12, 2, 4), f'{self.wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((12, 4, 2), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((12, 4, 3), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((12, 4, 4), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((12, 4, 5), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((13, 0, 2), 'stone_bricks', {}),
                ((13, 0, 3), 'stone_bricks', {}),
                ((13, 0, 4), 'stone_bricks', {}),
                ((13, 0, 5), 'stone_bricks', {}),
                ((13, 0, 6), 'stone_bricks', {}),
                ((13, 0, 7), 'stone_bricks', {}),
                ((13, 0, 8), 'stone_bricks', {}),
                ((13, 0, 9), 'stone_bricks', {}),
                ((13, 0, 10), 'stone_bricks', {}),
                ((13, 4, 2), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((13, 4, 3), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((13, 4, 4), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((13, 4, 5), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((14, 0, 2), 'stone_bricks', {}),
                ((14, 0, 3), 'stone_bricks', {}),
                ((14, 0, 4), 'stone_bricks', {}),
                ((14, 0, 5), 'stone_bricks', {}),
                ((14, 0, 6), 'stone_bricks', {}),
                ((14, 0, 7), 'stone_brick_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((14, 0, 8), 'stone_brick_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((14, 0, 9), 'stone_bricks', {}),
                ((14, 0, 10), 'stone_bricks', {}),
                ((14, 1, 2), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'false', 'west': 'false'}),
                ((14, 1, 3), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((14, 1, 4), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((14, 1, 5), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'false', 'north': 'true', 'west': 'false'}),
                ((14, 2, 2), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'false', 'west': 'false'}),
                ((14, 2, 3), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((14, 2, 4), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((14, 2, 5), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'false', 'north': 'true', 'west': 'false'}),
                ((14, 3, 1), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((14, 3, 2), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'false', 'west': 'false'}),
                ((14, 3, 3), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((14, 3, 4), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((14, 3, 5), f'{self.wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'false', 'north': 'true', 'west': 'false'}),
                ((14, 4, 2), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((14, 4, 3), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((14, 4, 4), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((14, 4, 5), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((15, 0, 3), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((15, 0, 4), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((15, 0, 5), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((15, 1, 4), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((15, 2, 2), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((15, 3, 2), f'{self.wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
            )
        )
