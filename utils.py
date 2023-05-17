from constants import ED

# RESSOURCES_CONVERSION = {
#     "planks": {"log": 0.25},
#     "stick": {"log": 0.125},
#     "wooden_slab": {"log": 0.125},
#     "wooden_stairs": {"log": 0.375},
#     "wooden_door": {"log": 0.5},
#     "wooden_fence": {"log": 0.42},
#     "wooden_fence_gate": {"log": 1},
#     "wooden_pressure_plate": {"log": 0.5},
#     "wooden_trapdoor": {"log": 0.75},
#     "wooden_button": {"log": 0.25},
#     "wooden_sign": {"log": 0.55},
#     "crafting_table": {"log": 1},
#     "chest": {"log": 2},

#     "paper": {"sugar_cane": 1},
#     "book": {"sugar_cane": 3, "leather": 1},
#     "bookshelf": {"log": 1.5, "leather": 3, "sugar_cane": 9},

#     "torch": {"coal": 0.25, "log": 0.031},
#     "ladder": {"log": 0.3},

#     "furnace": {"cobblestone": 8},
#     #TO CONTINUE
# }


# def process_needed_ressources(needed_ressources):
#     processed_needed_ressources = {}
#     for ressource in needed_ressources:
#         quantity = needed_ressources[ressource]
#         break
#     #TO CONTINUE

def get_building_at(coord_start, coord_end):

    startx, starty, startz = coord_start
    maxx, maxy, maxz = coord_start
    blocks = ""
    # needed_ressources = {}

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


def str_to_file(string, file_name):

    with open(file_name, 'w') as f:

        f.write(string)