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


def resize_houses(houses, current_loc):
    # Get the current shape of the houses array
    current_shape = houses.shape

    # Check if the current_loc id is within the current shape
    if current_loc[0] < current_shape[0] and current_loc[1] < current_shape[1]:
        print("Current location is within the current shape.")
    else:
        # Calculate the new shape that includes the current_loc id
        new_shape = (max(current_loc[0]+1, current_shape[0]), max(current_loc[1]+1, current_shape[1]))

        # Create a new array with the new shape and copy the values from the original array
        new_houses = np.zeros(new_shape)
        new_houses[:current_shape[0], :current_shape[1]] = houses

        # Update the houses array with the resized array
        houses = new_houses
        print("Houses array resized to contain the current location.")

    return houses


houses = resize_houses(houses, current_loc)
ic(houses)

# houses = np.insert(houses, current_loc, 1)
# houses.resize(new_shape)
# ic(current_loc)
# ic(houses)
