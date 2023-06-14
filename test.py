import math

from gdpc.vector_tools import cuboid3D, Box, circle

def find_circle_coordinates(external_coordinates):
    # Find center and radius of the circle
    x_coordinates, y_coordinates = zip(*external_coordinates)
    center_x = sum(x_coordinates) / len(x_coordinates)
    center_y = sum(y_coordinates) / len(y_coordinates)
    radius = math.sqrt((x_coordinates[0] - center_x)**2 + (y_coordinates[0] - center_y)**2)

    # Find all the coordinates within the circle
    circle_coordinates = []
    min_x = math.floor(center_x - radius)
    max_x = math.ceil(center_x + radius)
    min_y = math.floor(center_y - radius)
    max_y = math.ceil(center_y + radius)

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x - center_x)**2 + (y - center_y)**2 <= radius**2:
                circle_coordinates.append((x, y))

    return circle_coordinates

mycircle = list(circle((10, 10), 10, False))
print(mycircle)
print(find_circle_coordinates(mycircle))