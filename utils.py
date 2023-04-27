from constants import ED

def get_building_at(coord_start, coord_end):
    startx, starty, startz = coord_start
    res = ""
    for x in range(coord_start[0], coord_end[0]):
        for y in range(coord_start[1], coord_end[1]):
            for z in range(coord_start[2], coord_end[2]):
                block = ED.getBlock((x, y, z))
                if block.id[10:] != "air":
                    res += f"(({x - startx}, {y - starty}, {z - startz}), '{block.id[10:]}', {block.states}),\n"""
    return res

def str_to_file(string, file_name):
    with open(file_name, 'w') as f:
        f.write(string)