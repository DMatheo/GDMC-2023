from constants import ED
import random
import math
import numpy as np

from scipy.ndimage import distance_transform_edt

def get_best_starting_point(heightmap: np.ndarray) -> tuple:
    """
    Returns the best starting point for a building, given a heightmap.
    The best starting point is the one that is the furthest away from the nearest null value and from the outside of the array.

    :param heightmap(np.ndarray): The heightmap to use.
    :return: The best starting point for a building.
    :rtype: tuple
    """

    # Convert dataframe to binary mask
    mask = np.where(heightmap == None, 0, 1)

    # Calculate the distance transform
    dist_transform = distance_transform_edt(mask)

    # Initialize variables
    best_distance = -1
    best_coordinates = (-1, -1)

    # Iterate through the cells of the dataframe
    for row in range(heightmap.shape[0]):
        for col in range(heightmap.shape[1]):
            # Check if the current cell is a null value
            if heightmap[row, col] is None:
                continue
            
            # Calculate distance to the nearest null value using the distance transform
            dist_null = dist_transform[row, col]
            
            # Calculate distance to the border
            dist_border = min(row, heightmap.shape[0] - 1 - row, col, heightmap.shape[1] - 1 - col)
            
            # Calculate combined distance
            combined_dist = dist_null + dist_border
            
            # Update best distance and coordinates if necessary
            if combined_dist > best_distance:
                best_distance = combined_dist
                best_coordinates = (row, col)
    
    return best_coordinates

def get_building_at(coord_start:tuple, coord_end:tuple) -> str:
    """
    Returns a string representing the building at the given coordinates.

    :param coord_start(tuple): The starting coordinates of the building.
    :param coord_end(tuple): The ending coordinates of the building.
    :return: A string representing the building at the given coordinates.
    :rtype: str
    """
    startx, starty, startz = coord_start
    maxx, maxy, maxz = coord_start
    blocks = ""

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
    return f"Dimensions : ({maxx - startx}, {maxy - starty}, {maxz - startz})\n\n" + blocks

def generate_random_with_probability(target_probability:float, total_samples:int, max_probability:float) -> float:
    """
    Generates a random probability with the given probability. (The goal is to have a probability close to the one given but still random)

    :param target_probability(float): The probability of the target outcome.
    :param total_samples(int): The number of samples to generate.
    :param max_probability(float): The maximum probability.
    :return: The probability of the target outcome.
    :rtype: float
    """

    # Compute the probability of the other outcome
    other_probability = (1 - target_probability) / (1 - target_probability + target_probability)

    # Create a list of choices with the desired probabilities
    choices = [True] * int(target_probability * total_samples) + [False] * int(other_probability * total_samples)

    # Generate a random sample
    random_sample = random.choices(choices, k=total_samples)
    
    probability = sum(random_sample) / total_samples
    if probability > max_probability:
        probability = max_probability
    return probability


def str_to_file(string:str, file_name:str):
    """
    Writes a string to a file.

    :param string(str): The string to write.
    :param file_name(str): The name of the file to write to.
    """

    with open(file_name, 'w') as f:

        f.write(string)

def generate_random_height_map(width:int, max_height:int, frequency:float=0.5, amplitude:float=1.0, random_seed:int=None, seed:int=0) -> list:
    """
    Generates a random height map using a variant of the sin²(x) function.

    :param width(int): The width of the height map.
    :param max_height(int): The maximum height of the height map.
    :param frequency(float): The frequency of the sin²(x) function.
    :param amplitude(float): The amplitude of the sin²(x) function.
    :param random_seed(int): The random seed to use.
    :param seed(int): The seed to use.
    :return: The generated height map.
    :rtype: list
    """

    height_map = [[0] * width for _ in range(width)]

    if random_seed is not None:
        random.seed(random_seed)

    if seed == 0:
        seed = random.randint(0, 1000)

    for z in range(width):
        for x in range(width):
            height_value = math.sin(x+seed * frequency) + math.sin(z+seed * frequency)
            height_value = (height_value + 2) / 4  # Scale to [0, 1]
            height_map[z][x] = int(height_value * max_height + random.randint(-1, 1))

    return height_map