from settlements.Settlement import Settlement

from gdpc import geometry as geo

from gdpc.vector_tools import cuboid3D, Box

from gdpc import Block

from constants import ED
from utils import generate_random_with_probability

from buildings.Room_Buildings import build_room, RoomType, place_lamp_at


import math
import random 
class Underground(Settlement):

    def __init__(self, name:str, surface:object, rooms_width : int, rooms_walls_width : int, walls_width:int, floors_height:int, nbfloors:int):
        """Initialisation of the Underground class

        Args:
            name (str): Name of the settlement
            surface (object): Surface object
            width (int): width of walls
            height (int): height of floor levels
            floors (int): number of floors
        """

        self.ressources = dict()
        self.cave_location = surface.cave_location
        super().__init__(name, surface.location, surface.size)
        self.rooms_width = rooms_width
        self.rooms_walls_width = rooms_walls_width
        self.walls_width = walls_width
        self.height = floors_height
        self.nbfloors = nbfloors
        self.floors = []
        self.entities = []

    def settle(self):

        #Pyramid creation
        self.create_pyramid()
    
    def create_pyramid(self):
        """
        Create a pyramid
        """

        base = self.cave_location
        floor_down_rooms = {}

        print("Creating pyramid...")
        for step in range(0,self.nbfloors+1):
            floor = Floor(self.nbfloors - step, rooms_width=self.rooms_width, rooms_walls_width=self.rooms_walls_width, height=self.height)
            self.floors.append(floor)
            floor_level = self.nbfloors - step
            print("Creating floor " + str(floor_level) + "...")
            #Create the floor
            #We create the points

            #X
            lowest_x = base[0] - math.ceil((self.rooms_width-1)/2) - (self.rooms_width * floor_level) - (self.rooms_walls_width * floor_level) - self.walls_width
            highest_x = base[0] + math.floor((self.rooms_width-1)/2) + (self.rooms_width * floor_level) + (self.rooms_walls_width * floor_level) + self.walls_width
            
            #Y
            lowest_y = base[1] - (self.height) * step - (self.walls_width) * step # Y
            highest_y = base[1] - (self.height) * step - (self.walls_width) * step # Y

            #Z 
            lowest_z = base[2] - math.ceil((self.rooms_width-1)/2) - (self.rooms_width * floor_level) - (self.rooms_walls_width * floor_level) - self.walls_width
            highest_z = base[2] + math.floor((self.rooms_width-1)/2) + (self.rooms_width * floor_level) + (self.rooms_walls_width * floor_level) + self.walls_width

            lowest_floor_point = (lowest_x, lowest_y+1, lowest_z)
            highest_floor_point = (highest_x, highest_y+self.height, highest_z)
            lowest_ground_point = (lowest_x, lowest_y - self.walls_width + 1, lowest_z)
            highest_ground_point = (highest_x, highest_y, highest_z)

            if step != 0:
                #We take the top ground for later
                lowest_top_ground_point = (lowest_x, lowest_y, lowest_z)
                highest_top_ground_point = (highest_x, highest_y, highest_z)
                floor.set_ground(cuboid3D(lowest_top_ground_point, highest_top_ground_point))

                #We make the ground
                self.entities.append(cuboid3D(lowest_ground_point, highest_ground_point))
                geo.placeCuboid(ED, lowest_ground_point, highest_ground_point, Block("red_sandstone"))

                #We make the floor (walls and air)
                floor_coordinates = cuboid3D(lowest_floor_point, highest_floor_point)

                #We append separately because of a bug in the cuboid3D function
                self.entities.append(cuboid3D(lowest_floor_point, highest_floor_point))

                lowest_air_point = (lowest_floor_point[0] + self.walls_width, lowest_floor_point[1], lowest_floor_point[2] + self.walls_width)
                highest_air_point = (highest_floor_point[0] - self.walls_width, highest_floor_point[1], highest_floor_point[2] - self.walls_width)
                
                floor.set_starting_point(lowest_air_point)
                floor.set_space(cuboid3D(lowest_air_point, highest_air_point))
                floor.set_walls(iter(set(floor_coordinates) - set(floor.get_space())))

                geo.placeCuboid(ED, lowest_floor_point, highest_floor_point, Block("sandstone"))

                #We construct the rooms for the floor (only the shell ; no furniture yet)
                floor.construct_rooms()

                #We define the room that will hold some kind of structure to go to the lower floor
                down_room = floor.define_floor_down_room()
                if down_room is not None:
                    floor_down_rooms[step] = down_room.get_index()
            else:
                #We make the first ceiling
                ground = cuboid3D(lowest_ground_point, highest_ground_point)
                floor.set_ground(ground)
                self.entities.append(ground)
                geo.placeCuboid(ED, lowest_ground_point, highest_ground_point, Block("red_sandstone"))
            
            print("Floor " + str(floor_level) + " created.")
        
        #We setup the rooms that are used as a way to go to another floor
        self.setup_up_rooms(floor_down_rooms)

        #We build all the rooms inside the floors
        self.build_all_floors_rooms()

        #We decompose and vegetate the floors
        self.decompose_and_vegetate_floors()
        print("Pyramid created.")
    
    def decompose_and_vegetate_floors(self):
        """
        Decompose and vegetate all the floors
        """
        probability_of_decomposition = 0.12
        probability_of_vegetation = 0.09

        for entities in self.entities:
            #First, we define a level of decomposition.
            level_of_decomposition = generate_random_with_probability(0.475, 30, probability_of_decomposition)
            for coordinates in entities:
                if random.random() < level_of_decomposition:
                    ED.placeBlock(coordinates, Block("air"))

        VEGETATION_BLOCKS = ["water", "grass", "podzol", "coarse_dirt", "dirt", "mycelium", "dripstone_block", "sand", "moss_block", "dirt_path"]
        for floor in self.floors:
            ground = floor.get_ground()
            level_of_vegetation = generate_random_with_probability(0.2, 30, probability_of_vegetation)
            for coordinates in ground:
                if random.random() < level_of_vegetation:
                    ED.placeBlock(coordinates, Block(random.choice(VEGETATION_BLOCKS)))



    def setup_up_rooms(self, floor_down_rooms):
        for step, index in floor_down_rooms.items():
            if step >= len(self.floors)-2:
                continue
            index_x = index[0] - 1
            index_z = index[1] - 1
            self.floors[step+1].rooms[index_x][index_z].set_room_type(RoomType.FLOOR_UP)

    def build_all_floors_rooms(self):
        """
        Build all the rooms in the pyramid
        """
        for floor in self.floors:
            floor.build_rooms()
        
class Floor():
    def __init__(self, floor:int, rooms_width:int, rooms_walls_width:int, height:int):
        self.floor = floor
        self.rooms_width = rooms_width
        self.rooms_walls_width = rooms_walls_width
        self.height = height
        self.starting_point = None
        self.ground = None
        self.walls = None
        self.space = None
        self.rooms = []
        print("Floor created")

    def construct_rooms(self):
        """
        Create rooms in the floor
        """
        print("Creating rooms...")
        if (self.space != None):

            self.rooms = []
            width_of_air = int(math.sqrt(len(self.space)/self.height))
            width_of_rooms = self.rooms_width + self.rooms_walls_width

            if self.floor == 0:
                center_of_floor = 0
            else:
                center_of_floor = int((width_of_air - self.rooms_width) / 2) 

            for a in range(0, width_of_air, width_of_rooms):
                self.rooms.append([])
                for b in range(0, width_of_air, width_of_rooms):
                    start_point_room = (self.starting_point[0]+a, self.starting_point[1], self.starting_point[2]+b)
                    end_point_room = (self.starting_point[0]+a+self.rooms_width-1, self.starting_point[1]+self.height-1, self.starting_point[2]+b+self.rooms_width-1)
                    room_in_center_on_x = a == center_of_floor
                    room_in_center_on_z = b == center_of_floor
                    print("Stats d'une room en particulier")
                    print(center_of_floor)
                    print(a)
                    print(b)
                    print(room_in_center_on_x)
                    print(room_in_center_on_z)
                    room = Room(self.rooms_width, self.height, cuboid3D(start_point_room, end_point_room), start_point_room, room_in_center_on_x, room_in_center_on_z)
                    index_x = int(a/width_of_rooms)
                    index_z = int(b/width_of_rooms)
                    room.set_index(index_x, index_z)
                    self.rooms[index_x].append(room)
        for roomlist in self.rooms:
            for room in roomlist:
                room.clear()
        
        self.add_neighbours()
        self.clear_walls()
        self.setup_corridors()
        print("Rooms created.")
    
    def set_starting_point(self, starting_point:tuple):
        self.starting_point = starting_point

    def set_ground(self, ground:object):
        self.ground = ground

    def get_ground(self):
        return self.ground

    def set_walls(self, walls:object):
        self.walls = walls
    
    def set_space(self, space:object):
        self.space = set(space)
    
    def get_space(self):
        return self.space

    def define_floor_down_room(self):
        #We don't want to take rooms that are in the middle of the floor
        available = []
        middle = self.floor
        for i in range(1, len(self.rooms)-1):
            if i == middle:
                continue
            row = self.rooms[1:len(self.rooms)-1][i-1]
            available.extend(row[1:middle])
            available.extend(row[middle+1:len(row)-1])
        if len(available) > 1:
            down_room = random.choice(available)
            down_room.set_room_type(RoomType.FLOOR_DOWN)
            return down_room
        else:
            return None

    def add_neighbours(self):
        for x in range(len(self.rooms)):
            for z in range(len(self.rooms[x])):
                room = self.rooms[x][z]
                if x > 0:
                    room.add_neighbour("west", self.rooms[x-1][z])
                if x < len(self.rooms)-1:
                    room.add_neighbour("east", self.rooms[x+1][z])
                if z > 0:
                    room.add_neighbour("north", self.rooms[x][z-1])
                if z < len(self.rooms[x])-1:
                    room.add_neighbour("south", self.rooms[x][z+1])

    def clear_walls(self):
        path = [self.rooms[0][0]]
        visiteds = set()
        while len(visiteds) < len([room for roomlist in self.rooms for room in roomlist]):
                room = path[-1]
                visiteds.add(room)
                #get a random neighbour, if it has not been visited, add it to the path, else, choose another neighbour
                neighbours = room.get_neighbours()
                random.shuffle(neighbours)
                while len(neighbours) > 0 and (neighbours[0][1] in path or neighbours[0][1] in visiteds):
                    neighbours.pop(0)
                if len(neighbours) > 0:
                    path.append(neighbours[0][1])
                    self.clear_wall_at_direction(room.get_pos(), neighbours[0][0])
                else:
                    path.pop()
                
    def setup_corridors(self):
        if self.floor != 0:
            aisle_x_starting_point = self.rooms[len(self.rooms)//2][0].pos
            aisle_x_ending_point = list(self.rooms[len(self.rooms)//2][len(self.rooms[0])-1].pos)

            aisle_x_ending_point[0] += self.rooms_width - 1
            aisle_x_ending_point[1] += self.height - 1
            aisle_x_ending_point[2] += self.rooms_width - 1

            aisle_z_starting_point = self.rooms[0][len(self.rooms[0])//2].pos
            aisle_z_ending_point = list(self.rooms[len(self.rooms)-1][len(self.rooms[0])//2].pos)
            aisle_z_ending_point[0] += self.rooms_width - 1
            aisle_z_ending_point[1] += self.height - 1
            aisle_z_ending_point[2] += self.rooms_width - 1

            geo.placeCuboid(ED, aisle_x_starting_point, aisle_x_ending_point, Block("air"))
            geo.placeCuboid(ED, aisle_z_starting_point, aisle_z_ending_point, Block("air"))

            #Now, we add some kind of lamps at where the walls were at, in the hallways
            #The goal is to loop through the width of the air, and place a lamp every width of room + ceil(width of wall of room / 2)
            width_of_air = int(math.sqrt(len(self.space)/self.height))

            for offset in range(self.rooms_width - 1, width_of_air-self.rooms_width, self.rooms_width + self.rooms_walls_width):
                pos_x_top = (aisle_x_starting_point[0] + self.rooms_width - 1, aisle_x_starting_point[1] + self.height - 2, aisle_x_starting_point[2] + offset)
                pos_x_bot = (aisle_x_starting_point[0], aisle_x_starting_point[1] + self.height - 2, aisle_x_starting_point[2] + offset)
                pos_z_left = (aisle_z_starting_point[0] + offset, aisle_z_starting_point[1] + self.height - 2, aisle_z_starting_point[2] )
                pos_z_right = (aisle_z_starting_point[0] + offset, aisle_z_starting_point[1] + self.height - 2, aisle_z_starting_point[2] + self.rooms_width - 1)
                
                width_of_lamp = self.rooms_walls_width

                place_lamp_at(pos_x_top, "west", width_of_lamp)
                place_lamp_at(pos_x_bot, "east", width_of_lamp)
                place_lamp_at(pos_z_left, "south", width_of_lamp)
                place_lamp_at(pos_z_right, "north", width_of_lamp)
            
            #We finish off by placing 4 sandstone blocks at the middle because of the stairs
            middle_x = aisle_x_starting_point[0]
            middle_y = aisle_x_starting_point[1] + self.height - 2
            middle_z = aisle_x_starting_point[2] + (self.floor * (self.rooms_width + self.rooms_walls_width))
            ED.placeBlock((middle_x, middle_y, middle_z), Block("sandstone"))
            ED.placeBlock((middle_x + self.rooms_width - 1, middle_y, middle_z), Block("sandstone"))
            ED.placeBlock((middle_x, middle_y, middle_z + self.rooms_width - 1), Block("sandstone"))
            ED.placeBlock((middle_x + self.rooms_width - 1, middle_y, middle_z + self.rooms_width - 1), Block("sandstone"))


    def clear_wall_at_direction(self, pos:tuple, direction:str):
        match direction:
            case "east":
                x_loop = self.rooms_width
                z_loop = self.rooms_width/2
            case "south":
                x_loop = self.rooms_width/2
                z_loop = self.rooms_width
            case "west":
                x_loop = -self.rooms_walls_width
                z_loop = self.rooms_width/2
            case "north":
                x_loop = self.rooms_width/2
                z_loop = -self.rooms_walls_width

        starting_point = (pos[0] + x_loop, pos[1], pos[2] + z_loop)
        for x in range(0, self.rooms_walls_width):
            for y in range(self.height-1):
                z_start = -1 if (x_loop%1 != 0) or (z_loop%1 != 0) else -2
                for z in range(z_start, 2):
                    if direction == "north" or direction == "south":
                        x_offset = z
                        z_offset = x
                    else :
                        x_offset = x
                        z_offset = z
                    ED.placeBlock((int(starting_point[0]+x_offset), starting_point[1]+y, int(starting_point[2]+z_offset)), Block("air"))

    def build_rooms(self):
        for line in self.rooms:
            for room in line:
                room.build()

class Room:

    def __init__(self, width, height, blocks, starting_point, room_in_center_on_x = False, room_in_center_on_z = False):
        #Values for the room
        self.width = width
        self.height = height
        self.blocks = set(blocks)
        self.pos = starting_point
        self.is_centered_x = room_in_center_on_x
        self.is_centered_z = room_in_center_on_z

        #Values for later
        self.neighbours = {"north": None, "east": None, "south": None, "west": None}
        self.index = None
        self.builded = False
        self.holded_room = None
        if self.is_centered_x and self.is_centered_z:
            self.holded_room = RoomType.FLOOR_CENTER
        elif self.is_centered_x:
            self.holded_room = RoomType.HALLWAY_X
        elif self.is_centered_z:
            self.holded_room = RoomType.HALLWAY_Z

    def clear(self):
        for pos in self.blocks:
            ED.placeBlock(pos, Block("air"))

    def set_pos(self, pos:tuple):
        self.pos = pos
    
    def set_index(self, a,b):
        self.index = (a,b)
    
    def get_pos(self):
        return self.pos
    
    def get_index(self):
        return self.index

    def get_blocks(self):
        return self.blocks
    
    def add_neighbour(self, direction:str, room):
        self.neighbours[direction] = room

    def get_neighbours(self):
        return [(k,v) for k,v in self.neighbours.items() if v != None]
    
    def get_wall_directions(self):
        return [k for k,v in self.neighbours.items() if v == None]

    def set_room_type(self, room_type:RoomType):
        self.holded_room = room_type

    def get_room_type(self):
        return self.holded_room

    def build(self):
        if not self.builded:
            build_room(self)
            self.builded = True