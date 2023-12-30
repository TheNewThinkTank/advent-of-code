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


directions = get_data()
# ic(directions)

houses = np.zeros((1, 1))
ic(houses)

for idx, direction in enumerate(directions):
    if direction == ">":
        houses = np.append(houses, 1)
    if direction == "<":
        houses = np.insert(houses, idx - 1, 1)

ic(houses)
