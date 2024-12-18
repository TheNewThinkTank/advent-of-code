"""
How many houses receive at least one present?

examples:

> delivers presents to 2 houses: one at the starting location, and one to the east.

^>v< delivers presents to 4 houses in a square,
including twice to the house at his starting/ending location.

^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

from icecream import ic
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_all_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore

datafiles = [
    "input.txt",
    ]
datafile = get_full_path("2015", "day_3", datafiles[0])
directions = get_all_data(datafile)  # "^>v<"
# ic(directions)


def get_new_loc(dir, current_loc):
    new_loc = current_loc
    if dir == ">":
        new_loc = (current_loc[0], current_loc[1] + 1)
    if dir == "<":
        new_loc = (current_loc[0], current_loc[1] - 1)
    if dir == "^":
        new_loc = (current_loc[0] - 1, current_loc[1])
    if dir == "v":
        new_loc = (current_loc[0] + 1, current_loc[1])
    return new_loc


current_loc = (0, 0)
locations = []
locations.append(current_loc)

# part 1
# for dir in directions:
#     new_loc = get_new_loc(dir, current_loc)
#     current_loc = new_loc
#     locations.append(new_loc)
# total_houses = len(set(locations))
# ic(total_houses)

# part 2
santa_dir = directions[::2]
robo_dir = directions[1::2]

for dir in santa_dir:
    new_loc = get_new_loc(dir, current_loc)
    current_loc = new_loc
    locations.append(new_loc)

current_loc = (0, 0)
for dir in robo_dir:
    new_loc = get_new_loc(dir, current_loc)
    current_loc = new_loc
    locations.append(new_loc)

total_houses = len(set(locations))
ic(total_houses)
