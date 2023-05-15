def place_furniture():
    """
    This function places a bed, a crafting table and a furnace
    in the top middle of the build area.
    """
    mid_x, mid_z = calculate_middle()
    final_radius = min(8, *calculate_world_slice_size())
    ED.placeBlock((mid_x, STARTY + final_radius+1, mid_z), Block(f"birch_door", {"facing": "north"}))
    sign_data = mt.signData(line1="hOi", line2="and this is...", line3="BOB ! or not", line4="UNDERTALE")
    ED.placeBlock(
        (mid_x+1, STARTY + final_radius+1, mid_z), 
        Block(
            f"{getBiomeWoodType()}_sign", 
            {"rotation": 0}, 
            data=sign_data
        )
    )    
    ED.placeBlock(
        (mid_x+2, STARTY + final_radius+1, mid_z), 
        Block(
            f"minecraft:chest", 
            {"facing": "south", "type":"left"}, 
            data='{Items: [\
                        {id:"minecraft:dirt",Count:1b,Slot:0b},\
                        {id: "minecraft:acacia_door",Count:13b,Slot:1b},\
                        {id:"minecraft:iron_bars",Count:64b,Slot:2b},\
                        {id:"minecraft:lantern",Count:3b,Slot:14b},\
                        {id:"minecraft:spruce_fence",Count:1b,Slot:26b}\
                    ]\
            }'
        )
    )
    et.placeContainerBlock(ED, (mid_x+3, STARTY+final_radius+1, mid_z), Block("minecraft:chest"), [((3,1), "wheat")])
    book_data = mt.bookData(
        "This is a book.\nAnd I love it !",
        "My book", 
        "ShinryuSHH", 
        "The story", 
        "blue")
    et.placeLectern(ED, (mid_x+4, STARTY+final_radius+1, mid_z), "north", book_data)


def build_cube_harder_method(radius):
    """
    This function builds a cube of radius radius

    :type radius: int
    :param radius: Radius of the cube
    """

    chosen_wood_type=getBiomeWoodType()
    chosen_wood_type=getBiomeWoodTypeDifferent()
    final_radius = min(radius, *calculate_world_slice_size())
    mid_x, mid_z = calculate_middle()
    geo.placeCuboid(ED, 
                    (mid_x - final_radius, STARTY - final_radius, mid_z - final_radius), 
                    (mid_x + final_radius, STARTY + final_radius, mid_z + final_radius),
                    Block(chosen_wood_type+"_wood")
    )

def mostCommonWoodType(*slice_sizes):
    """
    This function returns the most common wood type in the world slice

    :type slice_sizes: tuple
    :param slice_sizes: The size of the world slice (in X and Z)
    """

    block = Block("minecraft:stone")
    biomes = getBiomeMap(*slice_sizes)
    most_common_biome = biomes["biomeId"].mode()[0]

    if "savanna" in most_common_biome:
        block = Block("minecraft:acacia_wood")
    elif "jungle" in most_common_biome:
        block = Block("minecraft:jungle_wood")
    elif "birch" in most_common_biome:
        block = Block("minecraft:birch_wood")
    elif "dark" in most_common_biome:
        block = Block("minecraft:dark_oak_wood")
    elif "mangrove" in most_common_biome:
        block = Block("minecraft:mangrove_wood")
    elif "warm" in most_common_biome:
        block = Block(f"minecraft:dead_horn_coral_block")
    elif "mushroom_field" in most_common_biome:
        blockName = ["brown_mushroom_block", "red_mushroom_block", "mushroom_stem"][randint(0,2)]
        block = Block(f"minecraft:{blockName}")
    elif most_common_biome == "minecraft:deep_dark":
        block = Block("minecraft:sculk")
    elif most_common_biome == "minecraft:lush_caves":
        block = Block("minecraft:moss_block")
    elif any(b in most_common_biome for b in ["spruce", "taiga", "grove", "tundra", "pine", "snowy_plains"]):
        block = Block("minecraft:spruce_wood")
    elif any(b in most_common_biome for b in ["beach", "desert"]):
        block = Block("minecraft:sandstone")
    elif any(b in most_common_biome for b in ["frozen", "cold", "snowy"]):
        block = Block("minecraft:blue_ice")
    elif most_common_biome == "minecraft:forest" or any(b in most_common_biome for b in ["badlands", "meadow", "swamp", "windswept", "wooded", "plains" ]):
        block = Block("minecraft:oak_wood")
            

    return block