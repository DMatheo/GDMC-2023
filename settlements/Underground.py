from settlements.Settlement import Settlement

from gdpc import geometry as geo

from gdpc.vector_tools import cuboid3D, Box, circle

from gdpc import Block

from constants import ED
from utils import generate_random_with_probability, generate_random_height_map, find_circle_coordinates

from buildings.Room_Buildings import build_room, RoomType, place_lamp_at


import math
import random 
class Underground(Settlement):
    """
    Underground settlement class

    :param name(str): Name of the settlement
    :param surface(object): Surface object
    :param rooms_width(int): width of rooms
    :param rooms_walls_width(int): width of rooms walls
    :param walls_width(int): width of the external shell of the pyramid
    :param floors_height(int): height of floor levels
    :param nbfloors(int): number of floors
    """

    def __init__(self, name:str, surface:object, rooms_width : int, rooms_walls_width : int, walls_width:int, floors_height:int, nbfloors:int):
        """
        Initialisation of the Underground class
        Minimum values allowed : 4 rooms_width, 1 rooms_walls_width, 1 walls_width, 4 floors_height, 1 nbfloors
        Please change the number of floors with caution, the algorithm is not optimized for a large number of floors, and the complexity grows factorially with the number of floors

        :param name(str): Name of the settlement
        :param surface(object): Surface object
        :param rooms_width(int): width of rooms
        :param rooms_walls_width(int): width of rooms walls
        :param walls_width(int): width of the external shell of the pyramid
        :param floors_height(int): height of floor levels
        :param nbfloors(int): number of floors
        """

        self.__surface = surface
        self.ressources = dict()
        self.cave_location = surface.cave_location
        pyr_x = self.cave_location[0] + random.randint(-surface.cave_size//3, surface.cave_size//3)
        pyr_z = self.cave_location[2] + random.randint(-surface.cave_size//3, surface.cave_size//3)
        self.pyramid_location = (pyr_x, surface.cave_location[1], pyr_z)
        super().__init__(name, surface.location, surface.size)
        self.rooms_width = rooms_width
        self.rooms_walls_width = rooms_walls_width
        self.walls_width = walls_width
        self.height = floors_height
        self.nbfloors = nbfloors
        self.floors = []
        self.entities = []

        if rooms_width < 4 :
            print("rooms_width must be greater than 4")
            print("rooms_width set to 4")
            rooms_width = 4
        if rooms_walls_width < 1 :
            print("rooms_walls_width must be greater than 1")
            print("rooms_walls_width set to 1")
            rooms_walls_width = 1
        if walls_width < 1 :
            print("walls_width must be greater than 1")
            print("walls_width set to 1")
            walls_width = 1
        if floors_height < 4 :
            print("floors_height must be greater than 4")
            print("floors_height set to 4")
            floors_height = 4
        if nbfloors < 1 :
            print("nbfloors must be greater than 1")
            print("nbfloors set to 1")
            nbfloors = 1


    def settle(self):
        """
        Start the underground settlement
        """

        #Pyramid creation
        self.create_pyramid()
        self.clear_top()

    def clear_top(self):
        """
        Clear the top of the pyramid using a reversed modified sin² function's heightmap
        """

        map = generate_random_height_map(self.__surface.cave_size*2, self.walls_width+(self.rooms_width//2))
        middle_coordinates = (self.cave_location[0], self.cave_location[2])
        start_circle = list(circle(middle_coordinates, self.__surface.cave_size, False))
        #Get the insides of the circle by hand, because of a bug in the circle object
        start_circle = find_circle_coordinates(start_circle)
        start_coordinates = (middle_coordinates[0] - self.__surface.cave_size//2 - 1, middle_coordinates[1] - self.__surface.cave_size//2 - 1)

        for x,z in start_circle:
            index_x = x - start_coordinates[0]
            index_z = z - start_coordinates[1]
            for y in range(map[index_x][index_z]):
                ED.placeBlock((x, self.cave_location[1]-y, z), Block("air"))
    
    def create_pyramid(self):
        """
        Create a pyramid
        """

        base = self.pyramid_location
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

            #We get the lowest and highest points of the ground and the floor
            lowest_floor_point = (lowest_x, lowest_y+1, lowest_z)
            highest_floor_point = (highest_x, highest_y+self.height, highest_z)
            lowest_ground_point = (lowest_x, lowest_y - self.walls_width + 1, lowest_z)
            highest_ground_point = (highest_x, highest_y, highest_z)
            
            #We take care of the special case of the first floor created, which has to be the top of the pyramid
            if step != 0:
                #We take the top ground for later
                lowest_top_ground_point = (lowest_x, lowest_y, lowest_z)
                highest_top_ground_point = (highest_x, highest_y, highest_z)
                floor.set_ground(cuboid3D(lowest_top_ground_point, highest_top_ground_point))

                #We make the ground
                self.entities.append(cuboid3D(lowest_ground_point, highest_ground_point))
                geo.placeCuboid(ED, lowest_ground_point, highest_ground_point, list([Block("red_sandstone")]*4 + [Block("copper_block")]))

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
                geo.placeCuboid(ED, lowest_ground_point, highest_ground_point, list([Block("red_sandstone")]*4 + [Block("copper_block")]))
            
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



    def setup_up_rooms(self, floor_down_rooms: dict):
        """
        Setup the rooms that are used as a way to go to another floor
        
        :param floor_down_rooms(dict): The rooms that are used as a way to go to another floor
        """

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
    """
    A floor of the pyramid

    :param floor(int): The floor number
    :param rooms_width(int): The width of the rooms
    :param rooms_walls_width(int): The width of the walls of the rooms
    :param height(int): The height of the floor
    """

    def __init__(self, floor:int, rooms_width:int, rooms_walls_width:int, height:int):
        """
        Constructor of the floor
        
        :param floor(int): The floor number
        :param rooms_width(int): The width of the rooms
        :param rooms_walls_width(int): The width of the walls of the rooms
        :param height(int): The height of the floor
        """
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
                    #We calculate the start and end point of the room in order to get the cuboid
                    #We also calculate if it is a room in the center of the floor, needed later
                    start_point_room = (self.starting_point[0]+a, self.starting_point[1], self.starting_point[2]+b)
                    end_point_room = (self.starting_point[0]+a+self.rooms_width-1, self.starting_point[1]+self.height-1, self.starting_point[2]+b+self.rooms_width-1)
                    room_in_center_on_x = a == center_of_floor
                    room_in_center_on_z = b == center_of_floor
                    room = Room(self.rooms_width, self.height, cuboid3D(start_point_room, end_point_room), start_point_room, room_in_center_on_x, room_in_center_on_z)
                    index_x = int(a/width_of_rooms)
                    index_z = int(b/width_of_rooms)
                    room.set_index(index_x, index_z)
                    self.rooms[index_x].append(room)
        
        #We now clear all rooms in order to have a clean floor
        for roomlist in self.rooms:
            for room in roomlist:
                room.clear()
        
        #We now add the neighbours of each room
        self.add_neighbours()
        #We now create the path between the rooms
        self.clear_walls()
        #Finally, we setup the corridors in the middle x and z axis
        self.setup_corridors()

        print("Rooms created.")
    
    def set_starting_point(self, starting_point:tuple):
        """
        Set the starting point of the floor
        
        :param starting_point(tuple): The starting point of the floor
        """

        self.starting_point = starting_point

    def set_ground(self, ground:object):
        """
        Set the ground of the floor
        
        :param ground(object): The ground of the floor
        """

        self.ground = ground

    def get_ground(self) -> object:
        """
        Get the ground of the floor
        
        :return: The ground of the floor
        """

        return self.ground

    def set_walls(self, walls:object):
        """
        Set the walls of the floor
        
        :param walls(object): The walls of the floor
        """

        self.walls = walls
    
    def set_space(self, space:tuple):
        """
        Set the space of the floor
        
        :param space(tuple): The space of the floor
        """

        self.space = set(space)
    
    def get_space(self) -> set:
        """
        Get the space of the floor
        
        :return: The space of the floor
        """

        return self.space

    def define_floor_down_room(self) -> object:
        """
        Define the room where the player will go down
        This room can't be the middle of the floor or at the sides of the floor
        
        :return: The room where the player will go down
        """
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
        """
        Add the neighbours of each room with the cardinal points
        """

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
        """
        Clear the walls between the rooms using a variant of the DFS algorithm
        """

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
        """
        Setup the corridors in the middle x and z axis
        """

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
        """
        Clear the wall at the given direction
        
        :param pos(tuple): The position of the room
        :param direction(str): The direction of the wall to clear
        """

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
        """
        Build the rooms
        """

        for line in self.rooms:
            for room in line:
                room.build()

class Room:
    """
    A room
    
    :param width(int): The width of the room
    :param height(int): The height of the room
    :param blocks(set): The blocks taking up the room
    :param starting_point(tuple): The starting point of the room
    :param room_in_center_on_x(bool): If the room is centered on the x axis
    :param room_in_center_on_z(bool): If the room is centered on the z axis
    """

    def __init__(self, width:int, height:int, blocks:tuple, starting_point:tuple, room_in_center_on_x : bool = False, room_in_center_on_z : bool = False):
        """
        Room initialization
        
        :param width(int): The width of the room
        :param height(int): The height of the room
        :param blocks(tuple): The blocks taking up the room
        :param starting_point(tuple): The starting point of the room
        :param room_in_center_on_x(bool): If the room is centered on the x axis
        :param room_in_center_on_z(bool): If the room is centered on the z axis
        """

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
        """
        Clear the room with air blocks
        """

        for pos in self.blocks:
            ED.placeBlock(pos, Block("air"))

    def set_pos(self, pos:tuple):
        """
        Set the position of the room
        
        :param pos(tuple): The position of the room
        """

        self.pos = pos
    
    def set_index(self, a:int,b:int):
        """
        Set the index of the room (in the rooms array of the floor)

        :param a(int): The first index
        :param b(int): The second index
        """

        self.index = (a,b)
    
    def get_pos(self) -> tuple:
        """
        Returns the position of the room
        
        :return: The position of the room (x,y,z)
        """
        return self.pos
    
    def get_index(self) -> tuple:
        """ 
        Returns the index of the room
        
        :return: The index of the room (a,b)
        """
        return self.index

    def get_blocks(self) -> set:
        """
        Returns the blocks of the room
        
        :return: The blocks taking up the room
        """

        return self.blocks
    
    def add_neighbour(self, direction:str, room:object):
        """
        Add a neighbour in a cardinal direction
        
        :param direction(str): Cardinal direction in which the room is
        :param room(object): The room at the cardinal direction
        """

        self.neighbours[direction] = room

    def get_neighbours(self) -> list:
        """
        Returns a list of all the neighbours, without the cardinal direction not taken
        
        :return: A list of all the neighbours
        """
        return [(k,v) for k,v in self.neighbours.items() if v != None]
    
    def get_wall_directions(self) -> list:
        """
        Returns a list of all the cardinal directions not taken

        :return: A list of all the cardinal directions not taken
        """

        return [k for k,v in self.neighbours.items() if v == None]

    def set_room_type(self, room_type:RoomType):
        """
        Set the room type

        :param room_type(RoomType): The room type
        """

        self.holded_room = room_type

    def get_room_type(self) -> RoomType:
        """
        Returns the room type

        :return: The room type
        """
        
        return self.holded_room

    def build(self):
        """
        Build the room
        """

        if not self.builded:
            build_room(self)
            self.builded = True