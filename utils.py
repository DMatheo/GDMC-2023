from math import ceil

from itertools import groupby
from operator import itemgetter

#Mathematical functions
def apply_heightmap(row, heightmap_dict):
    """
    This function returns the row if the block is below the heightmap, else it returns None

    :type row: pd.Series
    :param row: The row to check
    """

    x, y, z, name = row 
    if heightmap_dict[x][z] > y:
        return row
    return None

def get_largest_sequence(list_of_y):
    """
    This function returns the largest sequence of numbers in a list of numbers
    Credits to 
    https://stackoverflow.com/questions/60965915/python-program-program-to-find-largest-sequence-in-a-given-list-of-numbers

    :type list_of_y: pd.Series
    :param list_of_y: List of Y coordinates
    """
    new_l = []
    for k, g in groupby(enumerate(list_of_y), lambda ix : ix[0] - ix[1]):
        new_l.append(list(map(itemgetter(1), g)))
    return max(new_l, key=lambda x: len(x))

def calculate_world_slice_size(STARTX, LASTX, STARTZ, LASTZ):
    """
    Calculates the size in X and in Z.   

    :rtype: tuple
    :return: A tuple with the size in X and in Z 
    """
    return (abs(STARTX-LASTX), abs(STARTZ-LASTZ))

def calculate_middle(STARTX, LASTX, STARTZ, LASTZ):
    """
    Gets the middle point in x and z.

    :rtype: tuple
    :return: A tuple with the middle point in x and z
    """
    return ( ceil((STARTX+LASTX)/2), ceil((STARTZ + LASTZ)/2) )
