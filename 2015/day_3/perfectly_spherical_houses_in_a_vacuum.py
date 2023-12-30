"""
How many houses receive at least one present?

examples:

> delivers presents to 2 houses: one at the starting location, and one to the east.

^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.

^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

import numpy as np
from icecream import ic


datafiles = [
    "input.txt",
    ]
datafile = datafiles[0]


def get_data():
    with open(datafile, "r") as f:
        data = f.read()
    return data


directions = "^>v<"  # get_data()
# ic(directions)

houses = np.ones((1, 1))
current_loc = [0, 0]

# ic(houses)
shape = np.shape(houses)
ic(np.shape(houses))


def update_current_loc(dir):
    if dir == ">":
        current_loc[1] += 1
    if dir == "<":
        current_loc[1] -= 1
    if dir == "^":
        current_loc[0] -= 1
    if dir == "v":
        current_loc[0] += 1
    return current_loc


# for dir in directions:
dir = directions[0]
current_loc = update_current_loc(dir)
ic(current_loc)
# houses = np.insert(houses, current_loc, 1)

# TODO: check if new dims exceed shape:


# houses.resize(new_shape)

# ic(current_loc)
# ic(houses)
