#ENUMERATION OF THE TYPE OF ROOMS
from enum import Enum
from utils import generate_random_with_probability, generate_random_height_map
from gdpc import Block
import numpy as np
from constants import ED
from random import randint, random
from gdpc import editor_tools as et
from gdpc import geometry as geo

from gdpc.vector_tools import cylinder

import random

DIRECTION_MAPPING_LIGHTS = {
    "east": {"side": "x_bottom", "pos_1": "south", "pos_2": "west", "pos_3": "north"},
    "west": {"side": "x_top", "pos_1": "south", "pos_2": "east", "pos_3": "north"},
    "north": {"side": "z_bottom", "pos_1": "east", "pos_2": "south", "pos_3": "west"},
    "south": {"side": "z_top", "pos_1": "east", "pos_2": "north", "pos_3": "west"}
}

OFFSETS_LIGHTS = {
    "east": (0, 0, 1),
    "west": (0, 0, -1),
    "north": (1, 0, 0),
    "south": (-1, 0, 0)
}

class RoomType(Enum):
    MARKET = 1
    TAVERN = 2
    INN = 3
    FOUR_SIDED_COVERED = 4
    BARREL_STORAGE = 5
    FORGE = 6
    LIBRARY = 7
    FLOOR_DOWN = -1
    FLOOR_UP = -2
    HALLWAY_X = -3
    HALLWAY_Z = -4
    TREASURE_ROOM = -5
    FLOOR_CENTER = -6

def get_random_room_type(room):
    #All rooms that have a negative value are not supposed to be randomly given to a room.

    room_types = [RoomType.MARKET, RoomType.TAVERN, RoomType.INN, RoomType.BARREL_STORAGE, RoomType.FORGE, RoomType.LIBRARY]
    #all rooms have the same probability of being chosen
    return RoomType.BARREL_STORAGE
    if len(room.get_wall_directions()) == 0:
        return RoomType.FOUR_SIDED_COVERED #May happen in extremely rare cases
    else:
        return random.choice(room_types)


def build_room(room):   
    print(room.get_room_type())
    #Treasure room
    if len(room.get_neighbours()) == 0 and room.get_room_type() == RoomType.FLOOR_CENTER:
        print("Meowzie, my friend")
        room.set_room_type(RoomType.TREASURE_ROOM)
        initiate_treasure_room(room)
        return
    else:
        if room.get_room_type() is None:
            room.set_room_type(get_random_room_type(room))
        match room.get_room_type():
            case RoomType.TREASURE_ROOM:
                print("Impossible")
                return
            case RoomType.FLOOR_CENTER:
                initiate_floor_center(room)
                return
            case RoomType.FLOOR_DOWN:
                initiate_stair_down(room)
                return
            case RoomType.FLOOR_UP:
                initiate_stair_up(room)
                return
            case RoomType.MARKET:
                #TODO
                return
            case RoomType.TAVERN:
                #TODO
                return
            case RoomType.INN:
                #TODO
                return
            case RoomType.FOUR_SIDED_COVERED:
                #TODO
                return
            case RoomType.BARREL_STORAGE:
                initiate_barrel_storage(room)
                return
            case RoomType.FORGE:
                #TODO
                return
            case _:
                pass
    #Floor down
    if room.get_room_type() == RoomType.FLOOR_DOWN:
        initiate_stair_down(room)
        return

    #Floor up
    if room.get_room_type() == RoomType.FLOOR_UP:
        initiate_stair_up(room)
        return

def place_lamp_at(coord, direction, width):
    if direction is None:
        raise ValueError("No direction given")
    x, y, z = coord
    facing_direction_dict = DIRECTION_MAPPING_LIGHTS[direction]
    #We place a stair that acts like the side of the lamp
    ED.placeBlock(coord, Block("sandstone_stairs", {"facing": facing_direction_dict["pos_1"], "half": "top"}))
    #We place the lamp
    for i in range(1, width+1):
        if direction == "east":
            ED.placeBlock((x, y, z + i), Block("netherrack"))
            ED.placeBlock((x, y + 1, z + i), Block("fire"))
            ED.placeBlock((x, y - 1, z + i), Block("sandstone_slab", {"type": "top"}))
            ED.placeBlock((x + 1, y, z + i), Block("sandstone_stairs", {"facing": facing_direction_dict["pos_2"], "half": "top"}))
        elif direction == "west":
            ED.placeBlock((x, y, z + i), Block("netherrack"))
            ED.placeBlock((x, y + 1, z + i), Block("fire"))
            ED.placeBlock((x, y - 1, z + i), Block("sandstone_slab", {"type": "top"}))
            ED.placeBlock((x - 1, y, z + i), Block("sandstone_stairs", {"facing": facing_direction_dict["pos_2"], "half": "top"}))
        elif direction == "north":
            ED.placeBlock((x + i, y, z), Block("netherrack"))
            ED.placeBlock((x + i, y + 1, z), Block("fire"))
            ED.placeBlock((x + i, y - 1, z), Block("sandstone_slab", {"type": "top"}))
            ED.placeBlock((x + i, y, z - 1), Block("sandstone_stairs", {"facing": facing_direction_dict["pos_2"], "half": "top"}))
        elif direction == "south":
            ED.placeBlock((x + i, y, z), Block("netherrack"))
            ED.placeBlock((x + i, y + 1, z), Block("fire"))
            ED.placeBlock((x + i, y - 1, z), Block("sandstone_slab", {"type": "top"}))
            ED.placeBlock((x + i, y, z + 1), Block("sandstone_stairs", {"facing": facing_direction_dict["pos_2"], "half": "top"}))
    
    #We finish by putting a stair with pos 3
    if direction == "east" or direction == "west":
        ED.placeBlock((x, y, z + width + 1), Block("sandstone_stairs", {"facing": facing_direction_dict["pos_3"], "half": "top"}))
    elif direction == "north" or direction == "south":
        ED.placeBlock((x + width + 1, y, z), Block("sandstone_stairs", {"facing": facing_direction_dict["pos_3"], "half": "top"}))

def initiate_floor_center(room):
    #We want a fountain or an altar in the center of the room
    chosen_room = random.choice(["fountain", "altar"])
    if chosen_room == "fountain":
        build_fountain(room)
    elif chosen_room == "altar":
        build_altar(room)

def initiate_barrel_storage(room):
    heightmap = generate_random_height_map(width = room.width, max_height = room.height//2)
    start = room.get_pos()
    LOOTS_IN_BARRELS = {"dirt":0.85, "iron_ingot":0.08, "gold_ingot":0.02, "diamond":0.0025, "emerald":0.0025, "coal":0.03, "redstone":0.0025, "lapis_lazuli":0.0025, "quartz":0.005, "obsidian":0.00499, "netherite_ingot":0.00001}
    
        
    for x in range(len(heightmap)):
        for z in range(len(heightmap[x])):
            for y in range(heightmap[x][z]):
                chest_content = []
                # From the chest, you can get diamonds, emeralds, gold, even diamond tools, or EVEN a beacon
                for i in range(0, 9):
                    for j in range(0, 3):
                        #We add a bit of randomness to the chest content (meaning that the chest can have empty slots)
                        if random.random() < 0.55:
                            chest_content.append(((i, j), np.random.choice(list(LOOTS_IN_BARRELS.keys()), p=list(LOOTS_IN_BARRELS.values()))))
                et.placeContainerBlock(ED, (start[0]+x, start[1]+y, start[2]+z), Block("minecraft:barrel", {"facing":"up"}), chest_content)

    
def build_fountain(room):
    print(room)
    print(room.width)
    pos = room.pos
    fountain_base = cylinder((pos[0] + room.width // 2 - 1, pos[1]-1, pos[2] + room.width // 2 - 1), room.width-1, 1, hollow=True)
    print(fountain_base)
    for coord in fountain_base:
        print(coord)
        ED.placeBlock(coord, Block("quartz_block"))

def build_altar(room):
    #Using black glazed terractora's pattern
    print(room)
    print(room.width)
    pos = room.pos
    room_even_offset = int(room.width % 2 == 0)*2
    altar_base = cylinder((pos[0] + room.width // 2, pos[1]-1, pos[2] + room.width // 2), 2 + room_even_offset, 1, hollow=True)
    print(altar_base)
    for coord in altar_base:
        print(coord)
        ED.placeBlock(coord, Block("black_glazed_terracotta"))
    

def initiate_stair_down(room):
    starting_pos = list(room.pos)
    starting_pos[0] += room.width // 2 - 1
    starting_pos[1] -= 1
    starting_pos[2] += room.width // 2 - 1
    print(starting_pos)
    
    hole_2x2_offset = int(room.width % 2 == 0)
    ending_pos = starting_pos
    ending_pos[0] -= hole_2x2_offset
    ending_pos[2] -= hole_2x2_offset
    #I want to place ladders going down from the center of the room
    #I need to know the width of the room
    width = room.width

    geo.placeCuboid(ED, starting_pos, ending_pos, Block("air"))
    print("MEOWOJSOJOJ")
    for i in range(0, int(width%2 == 0)+3):
        for j in range(0, int(width%2 == 0)+3):
            #First, the corners
            if i == 0 and j == 0:
                ED.placeBlock((starting_pos[0] + i, starting_pos[1], starting_pos[2] + j), Block("sandstone_stairs", {"facing": "north", "shape": "inner_right"}))
            elif i == 0 and j == int(width%2 == 0)+2:
                ED.placeBlock((starting_pos[0] + i, starting_pos[1], starting_pos[2] + j), Block("sandstone_stairs", {"facing": "west", "shape": "inner_right"}))
            elif i == int(width%2 == 0)+2 and j == 0:
                ED.placeBlock((starting_pos[0] + i, starting_pos[1], starting_pos[2] + j), Block("sandstone_stairs", {"facing": "east", "shape": "inner_right"}))
            elif i == int(width%2 == 0)+2 and j == int(width%2 == 0)+2:
                ED.placeBlock((starting_pos[0] + i, starting_pos[1], starting_pos[2] + j), Block("sandstone_stairs", {"facing": "south", "shape": "inner_right"}))
            #Then, the sides
            elif i == 0:
                ED.placeBlock((starting_pos[0] + i, starting_pos[1], starting_pos[2] + j), Block("sandstone_stairs", {"facing": "west"}))
            elif i == int(width%2 == 0)+2:
                ED.placeBlock((starting_pos[0] + i, starting_pos[1], starting_pos[2] + j), Block("sandstone_stairs", {"facing": "east"}))
            elif j == 0:
                ED.placeBlock((starting_pos[0] + i, starting_pos[1], starting_pos[2] + j), Block("sandstone_stairs", {"facing": "north"}))
            elif j == int(width%2 == 0)+2:
                ED.placeBlock((starting_pos[0] + i, starting_pos[1], starting_pos[2] + j), Block("sandstone_stairs", {"facing": "south"}))
            #Finally, the center
            else:
                ED.placeBlock((starting_pos[0] + i, starting_pos[1], starting_pos[2] + j), Block("air"))
    ED.flushBuffer()


def initiate_stair_up(room):
    starting_pos = list(room.pos)
    starting_pos[0] += room.width // 2 - int(room.width % 2 == 0)
    starting_pos[2] += room.width // 2 - int(room.width % 2 == 0)
    width = room.width
    y = 0
    print("UWAAAAAAAAAAAAH")
    while ED.getBlock((starting_pos[0], starting_pos[1] + y, starting_pos[2] - 1)).id != "minecraft:sandstone_stairs":
        for i in range(0, int(width%2 == 0)+1):
            ED.runCommand(f"setblock {starting_pos[0] + i} {starting_pos[1] + y} {starting_pos[2]} minecraft:ladder[facing=south]")
            #ED.placeBlock((starting_pos[0], starting_pos[1] + y, starting_pos[2] + i), Block("ladder", {"facing": "north"}))
            if width % 2 == 0:
                ED.runCommand(f"setblock {starting_pos[0] + i} {starting_pos[1] + y} {starting_pos[2] + 1} minecraft:ladder[facing=north]")
                #ED.placeBlock((starting_pos[0] + 1, starting_pos[1] + y, starting_pos[2] + i), Block("ladder", {"facing": "south"}))
        y+=1

def initiate_treasure_room(room):
    heightmap = generate_random_height_map(width = room.width, max_height = room.height)
    start = room.get_pos()
    TREASURE_BLOCKS = {"gold_block" : 0.85, "lapis_block" : 0.08, "emerald_block" : 0.05, "diamond_block" : 0.02}
    
        
    for x in range(len(heightmap)):
        for z in range(len(heightmap[x])):
            for y in range(heightmap[x][z]):
                chosen_block = np.random.choice(list(TREASURE_BLOCKS.keys()), p=list(TREASURE_BLOCKS.values()))
                ED.placeBlock((start[0]+x, start[1]+y, start[2]+z), Block(chosen_block))
    
    chest_coord_x = start[0] + randint(0, room.width-1)
    chest_coord_y = start[1]
    chest_coord_z = start[2] + randint(0, room.height-1)
    chest_content = []
    # From the chest, you can get diamonds, emeralds, gold, even diamond tools, or EVEN a beacon
    CHEST_POSSIBLE_CONTENTS = {"gold_ingot" : 0.5, "diamond" : 0.17, "emerald" : 0.17, "diamond_pickaxe" : 0.03, "diamond_sword" : 0.03, "diamond_axe" : 0.03, "diamond_shovel" : 0.03, "diamond_hoe" : 0.03, "beacon" : 0.01}
    for i in range(0, 9):
        for j in range(0, 3):
            #We add a bit of randomness to the chest content (meaning that the chest can have empty slots)
            if random.random() < 0.65:
                chest_content.append(((i, j), np.random.choice(list(CHEST_POSSIBLE_CONTENTS.keys()), p=list(CHEST_POSSIBLE_CONTENTS.values()))))
    et.placeContainerBlock(ED, (chest_coord_x, chest_coord_y, chest_coord_z), Block("minecraft:chest"), chest_content)