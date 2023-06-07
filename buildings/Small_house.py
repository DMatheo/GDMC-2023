import random
from buildings.Building import Building

from constants import FLOWERS

class Small_house(Building):

    DIMENSIONS = {
        'north': (16, 13, 14),
        'south': (16, 13, 14),
        'east': (15, 13, 16),
        'west': (15, 13, 16)
    }

    ENTRY = (4,2)

    def __init__(self, coord, facing, settlement):
        super().__init__("Small_house", coord, self.get_blocks(settlement.wood_type), facing, settlement)

    def get_blocks(self, wood_type):
        return (
            (
                ((0, 2, 6), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((0, 2, 7), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((0, 2, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'true'}),

                ((1, 0, 4), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '2', 'persistent': 'true'}),
                ((1, 0, 5), 'stone_brick_wall', {
                    'east': 'tall', 'waterlogged': 'false', 'south': 'none', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((1, 0, 8), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((1, 0, 9), 'stone_brick_wall', {
                    'east': 'tall', 'waterlogged': 'false', 'south': 'none', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((1, 1, 5), f'{wood_type}_log', {'axis': 'x'}),
                ((1, 1, 6), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((1, 1, 7), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((1, 1, 8), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((1, 1, 9), f'{wood_type}_log', {'axis': 'x'}),
                ((1, 2, 4), f'{wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((1, 2, 5), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((1, 2, 6), 'grass_block', {'snowy': 'false'}),
                ((1, 2, 7), 'grass_block', {'snowy': 'false'}),
                ((1, 2, 8), 'grass_block', {'snowy': 'false'}),
                ((1, 2, 9), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((1, 2, 10), f'{wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((1, 3, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((1, 3, 5), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((1, 3, 6), f'{random.choice(FLOWERS)}', {}),
                ((1, 3, 7), f'{random.choice(FLOWERS)}', {}),
                ((1, 3, 8), f'{random.choice(FLOWERS)}', {}),
                ((1, 3, 9), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((1, 3, 10), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((1, 4, 5), f'{wood_type}_planks', {}),
                ((1, 4, 9), f'{wood_type}_planks', {}),
                ((1, 5, 5), f'{wood_type}_planks', {}),
                ((1, 5, 9), f'{wood_type}_planks', {}),
                ((1, 6, 5), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((1, 6, 6), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((1, 6, 8), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((1, 6, 9), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((1, 7, 6), f'{wood_type}_planks', {}),
                ((1, 7, 8), f'{wood_type}_planks', {}),
                ((1, 8, 6), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((1, 8, 7), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((1, 8, 8), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((1, 9, 7), f'{wood_type}_planks', {}),
                ((2, 0, 3), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '2', 'persistent': 'true'}),
                ((2, 0, 4), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((2, 0, 5), f'{wood_type}_log', {'axis': 'y'}),
                ((2, 0, 6), 'stone_bricks', {}),
                ((2, 0, 7), 'stone_bricks', {}),
                ((2, 0, 8), 'stone_bricks', {}),
                ((2, 0, 9), f'{wood_type}_log', {'axis': 'y'}),
                ((2, 1, 4), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((2, 1, 5), f'{wood_type}_log', {'axis': 'y'}),
                ((2, 1, 6), f'{wood_type}_log', {'axis': 'z'}),
                ((2, 1, 7), f'{wood_type}_log', {'axis': 'z'}),
                ((2, 1, 8), f'{wood_type}_log', {'axis': 'z'}),
                ((2, 1, 9), f'{wood_type}_log', {'axis': 'y'}),
                ((2, 2, 5), f'{wood_type}_log', {'axis': 'y'}),
                ((2, 2, 6), 'white_wool', {}),
                ((2, 2, 7), 'white_wool', {}),
                ((2, 2, 8), 'white_wool', {}),
                ((2, 2, 9), f'{wood_type}_log', {'axis': 'y'}),
                ((2, 3, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((2, 3, 5), f'{wood_type}_log', {'axis': 'y'}),
                ((2, 3, 6), 'white_wool', {}),
                ((2, 3, 7), 'glass_pane', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((2, 3, 8), 'white_wool', {}),
                ((2, 3, 9), f'{wood_type}_log', {'axis': 'y'}),
                ((2, 3, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((2, 4, 5), 'cut_copper', {}),
                ((2, 4, 6), 'white_wool', {}),
                ((2, 4, 7), 'glass_pane', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((2, 4, 8), 'white_wool', {}),
                ((2, 4, 9), 'cut_copper', {}),
                ((2, 5, 5), 'cut_copper', {}),
                ((2, 5, 6), 'white_wool', {}),
                ((2, 5, 7), 'glass_pane', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((2, 5, 8), 'white_wool', {}),
                ((2, 5, 9), 'cut_copper', {}),
                ((2, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((2, 6, 6), 'white_wool', {}),
                ((2, 6, 7), 'white_wool', {}),
                ((2, 6, 8), 'white_wool', {}),
                ((2, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((2, 7, 6), 'cut_copper', {}),
                ((2, 7, 7), 'white_wool', {}),
                ((2, 7, 8), 'cut_copper', {}),
                ((2, 8, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((2, 8, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((2, 9, 7), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((3, 0, 3), 'stone_bricks', {}),
                ((3, 0, 4), 'stone_bricks', {}),
                ((3, 0, 5), 'stone_bricks', {}),
                ((3, 0, 9), 'stone_bricks', {}),
                ((3, 1, 3), 'stone_brick_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((3, 1, 4), 'stone_bricks', {}),
                ((3, 1, 5), f'{wood_type}_log', {'axis': 'x'}),
                ((3, 1, 6), f'{wood_type}_planks', {}),
                ((3, 1, 7), f'{wood_type}_planks', {}),
                ((3, 1, 8), f'{wood_type}_planks', {}),
                ((3, 1, 9), f'{wood_type}_log', {'axis': 'x'}),
                ((3, 2, 4), f'{wood_type}_planks', {}),
                ((3, 2, 5), 'white_wool', {}),
                ((3, 2, 8), 'lectern', {'has_book': 'false',
                                        'powered': 'false', 'facing': 'north'}),
                ((3, 2, 9), 'white_wool', {}),
                ((3, 3, 3), 'wall_torch', {'facing': 'north'}),
                ((3, 3, 4), f'{wood_type}_planks', {}),
                ((3, 3, 5), 'white_wool', {}),
                ((3, 3, 9), 'white_wool', {}),
                ((3, 3, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((3, 4, 4), f'{wood_type}_planks', {}),
                ((3, 4, 5), 'cut_copper', {}),
                ((3, 4, 6), f'{wood_type}_wall_sign', {
                    'waterlogged': 'false', 'facing': 'east'}),
                ((3, 4, 9), 'cut_copper', {}),
                ((3, 5, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((3, 5, 5), 'cut_copper', {}),
                ((3, 5, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((3, 5, 9), 'cut_copper', {}),
                ((3, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((3, 6, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((3, 6, 7), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((3, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((3, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((3, 7, 6), 'cut_copper', {}),
                ((3, 7, 7), 'white_wool', {}),
                ((3, 7, 8), 'cut_copper', {}),
                ((3, 8, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((3, 8, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((3, 9, 7), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((4, 0, 3), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((4, 0, 5), 'stone_bricks', {}),
                ((4, 0, 9), 'stone_bricks', {}),
                ((4, 1, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((4, 1, 5), f'{wood_type}_planks', {}),
                ((4, 1, 6), f'{wood_type}_planks', {}),
                ((4, 1, 7), f'{wood_type}_planks', {}),
                ((4, 1, 8), f'{wood_type}_planks', {}),
                ((4, 1, 9), f'{wood_type}_log', {'axis': 'x'}),
                ((4, 2, 5), f'{wood_type}_door', {'hinge': 'right', 'half': 'lower',
                                         'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((4, 2, 8), 'bookshelf', {}),
                ((4, 2, 9), 'white_wool', {}),
                ((4, 3, 5), f'{wood_type}_door', {'hinge': 'right', 'half': 'upper',
                                         'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((4, 3, 9), 'white_wool', {}),
                ((4, 3, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((4, 4, 5), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((4, 4, 9), 'cut_copper', {}),
                ((4, 5, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((4, 5, 5), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((4, 5, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((4, 5, 9), 'cut_copper', {}),
                ((4, 6, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((4, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_right', 'facing': 'east'}),
                ((4, 6, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((4, 6, 7), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((4, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((4, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((4, 7, 6), 'cut_copper', {}),
                ((4, 7, 7), 'white_wool', {}),
                ((4, 7, 8), 'cut_copper', {}),
                ((4, 8, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((4, 8, 7), 'white_wool', {}),
                ((4, 8, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((4, 9, 7), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((5, 0, 3), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((5, 0, 5), 'stone_bricks', {}),
                ((5, 0, 9), 'stone_bricks', {}),
                ((5, 0, 10), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '3', 'persistent': 'true'}),
                ((5, 1, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((5, 1, 5), f'{wood_type}_planks', {}),
                ((5, 1, 6), f'{wood_type}_planks', {}),
                ((5, 1, 7), f'{wood_type}_planks', {}),
                ((5, 1, 8), f'{wood_type}_planks', {}),
                ((5, 1, 9), f'{wood_type}_log', {'axis': 'x'}),
                ((5, 2, 5), f'{wood_type}_door', {'hinge': 'left', 'half': 'lower',
                                         'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((5, 2, 8), 'bookshelf', {}),
                ((5, 2, 9), 'white_wool', {}),
                ((5, 3, 5), f'{wood_type}_door', {'hinge': 'left', 'half': 'upper',
                                         'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((5, 3, 8), 'bookshelf', {}),
                ((5, 3, 9), 'white_wool', {}),
                ((5, 3, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((5, 4, 5), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((5, 4, 8), 'bookshelf', {}),
                ((5, 4, 9), 'cut_copper', {}),
                ((5, 4, 10), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((5, 5, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((5, 5, 5), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((5, 5, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((5, 5, 9), 'cut_copper', {}),
                ((5, 6, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((5, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_right', 'facing': 'south'}),
                ((5, 6, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((5, 6, 7), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((5, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((5, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((5, 7, 6), 'cut_copper', {}),
                ((5, 7, 7), 'lantern', {
                    'waterlogged': 'false', 'hanging': 'true'}),
                ((5, 7, 8), 'cut_copper', {}),
                ((5, 8, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((5, 8, 7), 'white_wool', {}),
                ((5, 8, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((5, 9, 7), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((6, 0, 3), 'stone_bricks', {}),
                ((6, 0, 4), 'stone_bricks', {}),
                ((6, 0, 5), 'stone_bricks', {}),
                ((6, 0, 9), 'stone_bricks', {}),
                ((6, 0, 10), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '2', 'persistent': 'true'}),
                ((6, 0, 11), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((6, 1, 3), 'stone_brick_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((6, 1, 4), 'stone_bricks', {}),
                ((6, 1, 5), f'{wood_type}_log', {'axis': 'x'}),
                ((6, 1, 6), f'{wood_type}_planks', {}),
                ((6, 1, 7), f'{wood_type}_planks', {}),
                ((6, 1, 8), f'{wood_type}_planks', {}),
                ((6, 1, 9), f'{wood_type}_log', {'axis': 'x'}),
                ((6, 1, 10), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((6, 2, 2), f'{wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((6, 2, 4), f'{wood_type}_planks', {}),
                ((6, 2, 5), 'white_wool', {}),
                ((6, 2, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((6, 2, 9), 'white_wool', {}),
                ((6, 2, 12), f'{wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((6, 3, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((6, 3, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((6, 3, 4), f'{wood_type}_planks', {}),
                ((6, 3, 5), 'white_wool', {}),
                ((6, 3, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((6, 3, 9), 'white_wool', {}),
                ((6, 3, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((6, 3, 11), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((6, 3, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((6, 4, 4), f'{wood_type}_planks', {}),
                ((6, 4, 5), 'cut_copper', {}),
                ((6, 4, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((6, 4, 9), 'cut_copper', {}),
                ((6, 4, 10), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((6, 5, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((6, 5, 5), 'cut_copper', {}),
                ((6, 5, 9), 'cut_copper', {}),
                ((6, 5, 10), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((6, 6, 5), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((6, 6, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((6, 6, 7), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((6, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((6, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((6, 7, 6), 'cut_copper', {}),
                ((6, 7, 7), 'white_wool', {}),
                ((6, 7, 8), 'cut_copper', {}),
                ((6, 8, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((6, 8, 7), 'white_wool', {}),
                ((6, 8, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((6, 9, 7), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((7, 0, 2), 'stone_brick_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((7, 0, 3), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 0, 4), 'stone_bricks', {}),
                ((7, 0, 5), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 0, 9), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 0, 10), 'stone_bricks', {}),
                ((7, 0, 11), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 0, 12), 'stone_brick_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'none', 'north': 'tall', 'west': 'none', 'up': 'true'}),
                ((7, 1, 1), f'{wood_type}_button', {'face': 'wall',
                                           'powered': 'false', 'facing': 'north'}),
                ((7, 1, 2), f'{wood_type}_log', {'axis': 'z'}),
                ((7, 1, 3), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 1, 4), f'{wood_type}_log', {'axis': 'z'}),
                ((7, 1, 5), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 1, 6), f'{wood_type}_planks', {}),
                ((7, 1, 7), f'{wood_type}_planks', {}),
                ((7, 1, 8), f'{wood_type}_planks', {}),
                ((7, 1, 9), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 1, 10), f'{wood_type}_log', {'axis': 'z'}),
                ((7, 1, 11), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 1, 12), f'{wood_type}_log', {'axis': 'z'}),
                ((7, 1, 13), f'{wood_type}_button', {
                    'face': 'wall', 'powered': 'false', 'facing': 'south'}),
                ((7, 2, 2), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((7, 2, 3), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 2, 4), 'white_wool', {}),
                ((7, 2, 5), 'white_wool', {}),
                ((7, 2, 6), 'white_wool', {}),
                ((7, 2, 7), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((7, 2, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((7, 2, 9), 'white_wool', {}),
                ((7, 2, 10), 'white_wool', {}),
                ((7, 2, 11), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 2, 12), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((7, 3, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((7, 3, 3), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 3, 4), 'white_wool', {}),
                ((7, 3, 5), 'white_wool', {}),
                ((7, 3, 6), 'white_wool', {}),
                ((7, 3, 7), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((7, 3, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((7, 3, 9), 'white_wool', {}),
                ((7, 3, 10), 'white_wool', {}),
                ((7, 3, 11), f'{wood_type}_log', {'axis': 'y'}),
                ((7, 3, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((7, 4, 2), f'{wood_type}_planks', {}),
                ((7, 4, 3), 'cut_copper', {}),
                ((7, 4, 4), 'cut_copper', {}),
                ((7, 4, 5), 'cut_copper', {}),
                ((7, 4, 6), 'white_wool', {}),
                ((7, 4, 7), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((7, 4, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((7, 4, 9), 'cut_copper', {}),
                ((7, 4, 10), 'cut_copper', {}),
                ((7, 4, 11), 'cut_copper', {}),
                ((7, 4, 12), f'{wood_type}_planks', {}),
                ((7, 5, 2), f'{wood_type}_planks', {}),
                ((7, 5, 3), 'cut_copper', {}),
                ((7, 5, 4), 'cut_copper', {}),
                ((7, 5, 5), 'cut_copper', {}),
                ((7, 5, 6), 'white_wool', {}),
                ((7, 5, 7), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((7, 5, 8), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((7, 5, 9), 'cut_copper', {}),
                ((7, 5, 10), 'cut_copper', {}),
                ((7, 5, 11), 'cut_copper', {}),
                ((7, 5, 12), f'{wood_type}_planks', {}),
                ((7, 6, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 6, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 6, 5), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((7, 6, 6), 'cut_copper', {}),
                ((7, 6, 7), 'cut_copper', {}),
                ((7, 6, 8), 'cut_copper', {}),
                ((7, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_right', 'facing': 'north'}),
                ((7, 6, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 6, 11), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 6, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((7, 7, 5), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((7, 7, 6), 'cut_copper', {}),
                ((7, 7, 7), 'white_wool', {}),
                ((7, 7, 8), 'cut_copper', {}),
                ((7, 7, 9), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((7, 8, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((7, 8, 8), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((7, 9, 7), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((8, 0, 3), 'stone_bricks', {}),
                ((8, 0, 11), 'stone_bricks', {}),
                ((8, 1, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((8, 1, 3), f'{wood_type}_log', {'axis': 'x'}),
                ((8, 1, 4), f'{wood_type}_planks', {}),
                ((8, 1, 5), f'{wood_type}_planks', {}),
                ((8, 1, 6), f'{wood_type}_planks', {}),
                ((8, 1, 7), f'{wood_type}_planks', {}),
                ((8, 1, 8), f'{wood_type}_planks', {}),
                ((8, 1, 9), f'{wood_type}_planks', {}),
                ((8, 1, 10), f'{wood_type}_planks', {}),
                ((8, 1, 11), f'{wood_type}_log', {'axis': 'x'}),
                ((8, 1, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((8, 2, 1), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((8, 2, 2), 'grass_block', {'snowy': 'false'}),
                ((8, 2, 3), 'white_wool', {}),
                ((8, 2, 4), 'black_bed', {'part': 'head',
                                          'facing': 'west', 'occupied': 'false'}),
                ((8, 2, 6), 'white_wool', {}),
                ((8, 2, 9), 'furnace', {'lit': 'false', 'facing': 'east'}),
                ((8, 2, 10), 'furnace', {'lit': 'false', 'facing': 'east'}),
                ((8, 2, 11), 'white_wool', {}),
                ((8, 2, 12), 'grass_block', {'snowy': 'false'}),
                ((8, 2, 13), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((8, 3, 2), f'{random.choice(FLOWERS)}', {}),
                ((8, 3, 3), 'white_wool', {}),
                ((8, 3, 4), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((8, 3, 6), 'white_wool', {}),
                ((8, 3, 9), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'tall', 'up': 'true'}),
                ((8, 3, 10), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'tall', 'west': 'tall', 'up': 'true'}),
                ((8, 3, 11), 'white_wool', {}),
                ((8, 3, 12), f'{random.choice(FLOWERS)}', {}),
                ((8, 4, 3), 'white_wool', {}),
                ((8, 4, 4), 'lantern', {
                    'waterlogged': 'false', 'hanging': 'false'}),
                ((8, 4, 5), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((8, 4, 6), 'white_wool', {}),
                ((8, 4, 9), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'tall', 'up': 'true'}),
                ((8, 4, 10), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'tall', 'west': 'tall', 'up': 'true'}),
                ((8, 4, 11), 'white_wool', {}),
                ((8, 5, 3), 'white_wool', {}),
                ((8, 5, 6), 'white_wool', {}),
                ((8, 5, 9), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'tall', 'up': 'true'}),
                ((8, 5, 10), 'cobblestone_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'tall', 'west': 'tall', 'up': 'true'}),
                ((8, 5, 11), 'white_wool', {}),
                ((8, 6, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((8, 6, 3), 'white_wool', {}),
                ((8, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((8, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((8, 6, 6), 'white_wool', {}),
                ((8, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((8, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((8, 6, 9), 'cut_copper', {}),
                ((8, 6, 10), 'cut_copper', {}),
                ((8, 6, 11), 'white_wool', {}),
                ((8, 6, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'west'}),
                ((8, 7, 2), f'{wood_type}_planks', {}),
                ((8, 7, 3), 'cut_copper', {}),
                ((8, 7, 4), 'cut_copper', {}),
                ((8, 7, 5), 'cut_copper', {}),
                ((8, 7, 6), 'cut_copper', {}),
                ((8, 7, 7), 'white_wool', {}),
                ((8, 7, 8), 'cut_copper', {}),
                ((8, 7, 9), 'cut_copper', {}),
                ((8, 7, 10), 'cut_copper', {}),
                ((8, 7, 11), 'cut_copper', {}),
                ((8, 7, 12), f'{wood_type}_planks', {}),
                ((8, 8, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((8, 8, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((8, 8, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((8, 8, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((8, 8, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_right', 'facing': 'east'}),
                ((8, 8, 8), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((8, 8, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((8, 8, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((8, 8, 11), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((8, 8, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'east'}),
                ((8, 9, 7), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((9, 0, 3), 'stone_bricks', {}),
                ((9, 0, 11), 'stone_bricks', {}),
                ((9, 1, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((9, 1, 3), f'{wood_type}_log', {'axis': 'x'}),
                ((9, 1, 4), f'{wood_type}_planks', {}),
                ((9, 1, 5), f'{wood_type}_planks', {}),
                ((9, 1, 6), f'{wood_type}_planks', {}),
                ((9, 1, 7), f'{wood_type}_planks', {}),
                ((9, 1, 8), f'{wood_type}_planks', {}),
                ((9, 1, 9), f'{wood_type}_planks', {}),
                ((9, 1, 10), f'{wood_type}_planks', {}),
                ((9, 1, 11), f'{wood_type}_log', {'axis': 'x'}),
                ((9, 1, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((9, 2, 1), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((9, 2, 2), 'grass_block', {'snowy': 'false'}),
                ((9, 2, 3), 'white_wool', {}),
                ((9, 2, 4), 'black_bed', {'part': 'foot',
                                          'facing': 'west', 'occupied': 'false'}),
                ((9, 2, 6), f'{wood_type}_door', {'hinge': 'left', 'half': 'lower',
                                         'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((9, 2, 11), 'white_wool', {}),
                ((9, 2, 12), 'grass_block', {'snowy': 'false'}),
                ((9, 2, 13), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((9, 3, 2), f'{random.choice(FLOWERS)}', {}),
                ((9, 3, 3), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((9, 3, 6), f'{wood_type}_door', {'hinge': 'left', 'half': 'upper',
                                         'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((9, 3, 11), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((9, 3, 12), f'{random.choice(FLOWERS)}', {}),
                ((9, 4, 3), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((9, 4, 6), 'white_wool', {}),
                ((9, 4, 7), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((9, 4, 11), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((9, 5, 3), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((9, 5, 6), 'white_wool', {}),
                ((9, 5, 7), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((9, 5, 11), 'glass_pane', {
                    'east': 'true', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'true'}),
                ((9, 6, 3), 'white_wool', {}),
                ((9, 6, 4), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((9, 6, 5), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((9, 6, 6), 'white_wool', {}),
                ((9, 6, 7), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((9, 6, 8), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((9, 6, 9), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((9, 6, 10), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'north', 'open': 'false'}),
                ((9, 6, 11), 'white_wool', {}),
                ((9, 7, 3), 'white_wool', {}),
                ((9, 7, 4), 'white_wool', {}),
                ((9, 7, 5), 'lantern', {
                    'waterlogged': 'false', 'hanging': 'true'}),
                ((9, 7, 6), 'white_wool', {}),
                ((9, 7, 7), 'white_wool', {}),
                ((9, 7, 8), 'white_wool', {}),
                ((9, 7, 9), 'lantern', {
                    'waterlogged': 'false', 'hanging': 'true'}),
                ((9, 7, 10), 'white_wool', {}),
                ((9, 7, 11), 'white_wool', {}),
                ((9, 8, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((9, 8, 5), 'white_wool', {}),
                ((9, 8, 9), 'white_wool', {}),
                ((9, 8, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((9, 9, 2), f'{wood_type}_planks', {}),
                ((9, 9, 3), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((9, 9, 4), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((9, 9, 5), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((9, 9, 6), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((9, 9, 7), 'diorite', {}),
                ((9, 9, 8), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((9, 9, 9), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((9, 9, 10), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((9, 9, 11), f'{wood_type}_slab', {
                    'waterlogged': 'false', 'type': 'bottom'}),
                ((9, 9, 12), f'{wood_type}_planks', {}),
                ((9, 10, 7), 'diorite', {}),
                ((9, 11, 7), 'diorite_wall', {'east': 'none', 'waterlogged': 'false',
                                              'south': 'none', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((9, 12, 7), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((10, 0, 2), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((10, 0, 3), 'stone_bricks', {}),
                ((10, 0, 11), 'stone_bricks', {}),
                ((10, 1, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((10, 1, 3), f'{wood_type}_log', {'axis': 'x'}),
                ((10, 1, 4), f'{wood_type}_planks', {}),
                ((10, 1, 5), f'{wood_type}_planks', {}),
                ((10, 1, 6), f'{wood_type}_planks', {}),
                ((10, 1, 7), f'{wood_type}_planks', {}),
                ((10, 1, 8), f'{wood_type}_planks', {}),
                ((10, 1, 9), f'{wood_type}_planks', {}),
                ((10, 1, 10), f'{wood_type}_planks', {}),
                ((10, 1, 11), f'{wood_type}_log', {'axis': 'x'}),
                ((10, 1, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((10, 2, 1), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'north', 'open': 'true'}),
                ((10, 2, 2), 'grass_block', {'snowy': 'false'}),
                ((10, 2, 3), 'white_wool', {}),
                ((10, 2, 4), 'bookshelf', {}),
                ((10, 2, 5), 'bookshelf', {}),
                ((10, 2, 6), 'white_wool', {}),
                ((10, 2, 10), 'smooth_stone_slab', {
                    'waterlogged': 'false', 'type': 'double'}),
                ((10, 2, 11), 'white_wool', {}),
                ((10, 2, 12), 'grass_block', {'snowy': 'false'}),
                ((10, 2, 13), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'true'}),
                ((10, 3, 2), f'{random.choice(FLOWERS)}', {}),
                ((10, 3, 3), 'white_wool', {}),
                ((10, 3, 4), 'bookshelf', {}),
                ((10, 3, 5), 'bookshelf', {}),
                ((10, 3, 6), 'white_wool', {}),
                ((10, 3, 11), 'white_wool', {}),
                ((10, 3, 12), f'{random.choice(FLOWERS)}', {}),
                ((10, 4, 3), 'white_wool', {}),
                ((10, 4, 4), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((10, 4, 5), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((10, 4, 6), 'white_wool', {}),
                ((10, 4, 7), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((10, 4, 9), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((10, 4, 10), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((10, 4, 11), 'white_wool', {}),
                ((10, 5, 3), 'white_wool', {}),
                ((10, 5, 6), 'white_wool', {}),
                ((10, 5, 7), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((10, 5, 9), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((10, 5, 10), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((10, 5, 11), 'white_wool', {}),
                ((10, 6, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 6, 3), 'white_wool', {}),
                ((10, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 6, 6), 'white_wool', {}),
                ((10, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 6, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 6, 11), 'white_wool', {}),
                ((10, 6, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((10, 7, 2), f'{wood_type}_planks', {}),
                ((10, 7, 3), 'cut_copper', {}),
                ((10, 7, 4), 'cut_copper', {}),
                ((10, 7, 5), 'cut_copper', {}),
                ((10, 7, 6), 'diorite', {}),
                ((10, 7, 7), 'cut_copper', {}),
                ((10, 7, 8), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((10, 7, 9), 'cut_copper', {}),
                ((10, 7, 10), 'cut_copper', {}),
                ((10, 7, 11), 'cut_copper', {}),
                ((10, 7, 12), f'{wood_type}_planks', {}),
                ((10, 8, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 8, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 8, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 8, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 8, 6), 'diorite', {}),
                ((10, 8, 7), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((10, 8, 8), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((10, 8, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 8, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 8, 11), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 8, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((10, 9, 6), 'diorite', {}),
                ((10, 9, 7), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((10, 10, 6), 'diorite', {}),
                ((10, 11, 6), 'diorite', {}),
                ((10, 12, 6), 'diorite_wall', {'east': 'none', 'waterlogged': 'false',
                                              'south': 'none', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((10, 13, 6), 'iron_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'false'}),
                ((11, 0, 1), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((11, 0, 2), 'stone_brick_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'tall', 'north': 'none', 'west': 'none', 'up': 'true'}),
                ((11, 0, 3), f'{wood_type}_log', {'axis': 'y'}),
                ((11, 0, 4), 'stone_bricks', {}),
                ((11, 0, 5), 'stone_bricks', {}),
                ((11, 0, 6), 'stone_bricks', {}),
                ((11, 0, 7), 'stone_bricks', {}),
                ((11, 0, 8), 'stone_bricks', {}),
                ((11, 0, 9), 'stone_bricks', {}),
                ((11, 0, 10), 'stone_bricks', {}),
                ((11, 0, 11), f'{wood_type}_log', {'axis': 'y'}),
                ((11, 0, 12), 'stone_brick_wall', {
                    'east': 'none', 'waterlogged': 'false', 'south': 'none', 'north': 'tall', 'west': 'none', 'up': 'true'}),
                ((11, 1, 1), f'{wood_type}_button', {
                    'face': 'wall', 'powered': 'false', 'facing': 'north'}),
                ((11, 1, 2), f'{wood_type}_log', {'axis': 'z'}),
                ((11, 1, 3), f'{wood_type}_log', {'axis': 'y'}),
                ((11, 1, 4), f'{wood_type}_log', {'axis': 'z'}),
                ((11, 1, 5), f'{wood_type}_log', {'axis': 'z'}),
                ((11, 1, 6), f'{wood_type}_log', {'axis': 'z'}),
                ((11, 1, 7), f'{wood_type}_log', {'axis': 'z'}),
                ((11, 1, 8), f'{wood_type}_planks', {}),
                ((11, 1, 9), f'{wood_type}_planks', {}),
                ((11, 1, 10), f'{wood_type}_log', {'axis': 'z'}),
                ((11, 1, 11), f'{wood_type}_log', {'axis': 'y'}),
                ((11, 1, 12), f'{wood_type}_log', {'axis': 'z'}),
                ((11, 1, 13), f'{wood_type}_button', {
                    'face': 'wall', 'powered': 'false', 'facing': 'south'}),
                ((11, 2, 2), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((11, 2, 3), f'{wood_type}_log', {'axis': 'y'}),
                ((11, 2, 4), 'white_wool', {}),
                ((11, 2, 5), 'white_wool', {}),
                ((11, 2, 6), 'white_wool', {}),
                ((11, 2, 7), 'white_wool', {}),
                ((11, 2, 8), f'{wood_type}_door', {'hinge': 'right', 'half': 'lower',
                                          'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((11, 2, 9), f'{wood_type}_door', {'hinge': 'left', 'half': 'lower',
                                          'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((11, 2, 10), 'white_wool', {}),
                ((11, 2, 11), f'{wood_type}_log', {'axis': 'y'}),
                ((11, 2, 12), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'east', 'open': 'true'}),
                ((11, 3, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((11, 3, 3), f'{wood_type}_log', {'axis': 'y'}),
                ((11, 3, 4), 'white_wool', {}),
                ((11, 3, 5), 'white_wool', {}),
                ((11, 3, 6), 'white_wool', {}),
                ((11, 3, 7), 'white_wool', {}),
                ((11, 3, 8), f'{wood_type}_door', {'hinge': 'right', 'half': 'upper',
                                          'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((11, 3, 9), f'{wood_type}_door', {'hinge': 'left', 'half': 'upper',
                                          'powered': 'false', 'facing': 'west', 'open': 'false'}),
                ((11, 3, 10), 'white_wool', {}),
                ((11, 3, 11), f'{wood_type}_log', {'axis': 'y'}),
                ((11, 3, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'east'}),
                ((11, 4, 2), f'{wood_type}_planks', {}),
                ((11, 4, 3), 'cut_copper', {}),
                ((11, 4, 4), 'cut_copper', {}),
                ((11, 4, 5), 'cut_copper', {}),
                ((11, 4, 6), 'cut_copper', {}),
                ((11, 4, 7), 'cut_copper', {}),
                ((11, 4, 8), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((11, 4, 9), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'top', 'powered': 'false', 'facing': 'west', 'open': 'true'}),
                ((11, 4, 10), 'cut_copper', {}),
                ((11, 4, 11), 'cut_copper', {}),
                ((11, 4, 12), f'{wood_type}_planks', {}),
                ((11, 5, 2), f'{wood_type}_planks', {}),
                ((11, 5, 3), 'cut_copper', {}),
                ((11, 5, 4), 'cut_copper', {}),
                ((11, 5, 5), 'cut_copper', {}),
                ((11, 5, 6), 'cut_copper', {}),
                ((11, 5, 7), 'cut_copper', {}),
                ((11, 5, 8), 'cut_copper', {}),
                ((11, 5, 9), 'cut_copper', {}),
                ((11, 5, 10), 'cut_copper', {}),
                ((11, 5, 11), 'cut_copper', {}),
                ((11, 5, 12), f'{wood_type}_planks', {}),
                ((11, 6, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 7), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 8), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 9), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 10), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 11), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 6, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((11, 7, 7), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((12, 0, 3), 'stone_bricks', {}),
                ((12, 0, 4), 'stone_bricks', {}),
                ((12, 0, 5), 'stone_bricks', {}),
                ((12, 0, 6), 'stone_bricks', {}),
                ((12, 0, 7), 'stone_bricks', {}),
                ((12, 0, 8), 'stone_bricks', {}),
                ((12, 0, 9), 'stone_bricks', {}),
                ((12, 0, 10), 'stone_bricks', {}),
                ((12, 0, 11), 'stone_bricks', {}),
                ((12, 0, 12), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((12, 1, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'inner_left', 'facing': 'north'}),
                ((12, 1, 5), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 1, 6), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 1, 7), f'{wood_type}_planks', {}),
                ((12, 1, 8), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 1, 9), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 1, 10), f'{wood_type}_planks', {}),
                ((12, 1, 11), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '1', 'persistent': 'true'}),
                ((12, 2, 2), f'{wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((12, 2, 7), f'{wood_type}_planks', {}),
                ((12, 2, 10), f'{wood_type}_planks', {}),
                ((12, 2, 12), f'{wood_type}_slab', {
                 'waterlogged': 'false', 'type': 'top'}),
                ((12, 3, 2), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 3, 3), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 3, 4), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 3, 5), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 3, 6), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 3, 7), f'{wood_type}_planks', {}),
                ((12, 3, 10), f'{wood_type}_planks', {}),
                ((12, 3, 11), 'cut_copper_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 3, 12), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((12, 4, 3), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((12, 4, 4), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((12, 4, 5), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((12, 4, 6), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((12, 4, 7), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((12, 4, 8), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'north'}),
                ((12, 4, 9), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'top', 'shape': 'straight', 'facing': 'south'}),
                ((12, 4, 10), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((12, 5, 8), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'south'}),
                ((12, 5, 9), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((13, 0, 3), 'stone_bricks', {}),
                ((13, 0, 4), 'stone_bricks', {}),
                ((13, 0, 5), 'stone_bricks', {}),
                ((13, 0, 6), 'stone_bricks', {}),
                ((13, 0, 7), 'stone_bricks', {}),
                ((13, 0, 8), 'stone_bricks', {}),
                ((13, 0, 9), 'stone_bricks', {}),
                ((13, 0, 10), 'stone_bricks', {}),
                ((13, 0, 11), 'stone_bricks', {}),
                ((13, 0, 12), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((13, 1, 4), f'{wood_type}_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'north'}),
                ((13, 1, 5), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'false', 'north': 'false', 'west': 'false'}),
                ((13, 2, 5), f'{wood_type}_trapdoor', {
                    'waterlogged': 'false', 'half': 'bottom', 'powered': 'false', 'facing': 'south', 'open': 'false'}),
                ((13, 4, 3), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((13, 4, 4), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((13, 4, 5), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((13, 4, 6), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((14, 0, 3), 'stone_bricks', {}),
                ((14, 0, 4), 'stone_bricks', {}),
                ((14, 0, 5), 'stone_bricks', {}),
                ((14, 0, 6), 'stone_bricks', {}),
                ((14, 0, 7), 'stone_bricks', {}),
                ((14, 0, 8), 'stone_bricks', {}),
                ((14, 0, 9), 'stone_bricks', {}),
                ((14, 0, 10), 'stone_bricks', {}),
                ((14, 0, 11), 'stone_bricks', {}),
                ((14, 4, 3), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((14, 4, 4), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((14, 4, 5), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((14, 4, 6), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((15, 0, 3), 'stone_bricks', {}),
                ((15, 0, 4), 'stone_bricks', {}),
                ((15, 0, 5), 'stone_bricks', {}),
                ((15, 0, 6), 'stone_bricks', {}),
                ((15, 0, 7), 'stone_bricks', {}),
                ((15, 0, 8), 'stone_brick_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((15, 0, 9), 'stone_brick_stairs', {
                    'waterlogged': 'false', 'half': 'bottom', 'shape': 'straight', 'facing': 'west'}),
                ((15, 0, 10), 'stone_bricks', {}),
                ((15, 0, 11), 'stone_bricks', {}),
                ((15, 1, 3), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'false', 'west': 'false'}),
                ((15, 1, 4), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((15, 1, 5), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((15, 1, 6), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'false', 'north': 'true', 'west': 'false'}),
                ((15, 2, 3), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'false', 'west': 'false'}),
                ((15, 2, 4), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((15, 2, 5), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((15, 2, 6), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'false', 'north': 'true', 'west': 'false'}),
                ((15, 3, 2), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((15, 3, 3), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'false', 'west': 'false'}),
                ((15, 3, 4), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((15, 3, 5), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'true', 'north': 'true', 'west': 'false'}),
                ((15, 3, 6), f'{wood_type}_fence', {
                    'east': 'false', 'waterlogged': 'false', 'south': 'false', 'north': 'true', 'west': 'false'}),
                ((15, 4, 3), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((15, 4, 4), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((15, 4, 5), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((15, 4, 6), 'campfire', {
                    'waterlogged': 'false', 'signal_fire': 'false', 'lit': 'false', 'facing': 'west'}),
                ((16, 0, 4), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((16, 0, 5), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((16, 0, 6), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((16, 1, 5), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((16, 2, 3), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
                ((16, 3, 3), f'{wood_type}_leaves', {
                    'waterlogged': 'false', 'distance': '7', 'persistent': 'true'}),
            )
        )
