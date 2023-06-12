from constants import ED
import random
import math

def get_building_at(coord_start, coord_end):

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

def generate_random_with_probability(target_probability, total_samples, max_probability):
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


def str_to_file(string, file_name):

    with open(file_name, 'w') as f:

        f.write(string)

def generate_random_height_map(width, max_height, frequency=0.5, amplitude=1.0, random_seed=None, seed=0):
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