"""
A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper
plus 6 square feet of slack, for a total of 58 square feet.

A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper
plus 1 square foot of slack, for a total of 43 square feet.
"""

from icecream import ic


datafiles = [
    "input.txt",
    ]
datafile = datafiles[0]


def get_data():
    with open(datafile, "r") as f:
        data = f.read()
    data = data.split("\n")

    dim = []
    for d in data:
        i = d.split('x')
        i = [int(ii) for ii in i]
        dim.append({'l': i[0], 'w': i[1], 'h': i[2]})

    return dim


def get_surface_area(present):
    l = present['l']
    w = present['w']
    h = present['h']
    surface_area = 2 * l * w + 2 * w * h + 2 * h * l
    return surface_area


def get_smallest_side_area(present):
    min_items = min(present.items(), key=lambda x: x[1])
    second_min_items = min((item
                            for item in present.items()
                            if item != min_items),
                            key=lambda x: x[1]
                            )
    smallest_side_area = min_items[1] * second_min_items[1]
    return smallest_side_area


# present = {'h': 30, 'l': 20, 'w': 29}
dim = get_data()
# ic(dim)
total = 0
for present in dim:
    surface_area = get_surface_area(present)
    smallest_side_area = get_smallest_side_area(present)
    # ic(smallest_side_area)
    total += surface_area + smallest_side_area

ic(total)
