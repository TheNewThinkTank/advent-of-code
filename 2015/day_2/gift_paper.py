
from functools import reduce
from operator import mul

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


def get_2_smallest_dims(present):
    min_items = min(present.items(), key=lambda x: x[1])
    second_min_items = min((item
                            for item in present.items()
                            if item != min_items),
                            key=lambda x: x[1]
                            )
    return min_items, second_min_items


def get_smallest_side_area(present):
    min_items, second_min_items = get_2_smallest_dims(present)
    smallest_side_area = min_items[1] * second_min_items[1]
    return smallest_side_area


def get_ribbon(present):
    min_items, second_min_items = get_2_smallest_dims(present)
    wrap = min_items[1] + min_items[1] + second_min_items[1] + second_min_items[1]
    bow = reduce(mul, present.values())
    # ic(wrap)
    # ic(bow)
    return wrap + bow


# present = {'h': 30, 'l': 20, 'w': 29}
dim = get_data()
# ic(dim)
total_wrapping_paper = 0
total_ribbon = 0
for present in dim:
    surface_area = get_surface_area(present)
    smallest_side_area = get_smallest_side_area(present)
    # ic(smallest_side_area)
    total_wrapping_paper += surface_area + smallest_side_area
    total_ribbon += get_ribbon(present)

ic(total_wrapping_paper)
ic(total_ribbon)
