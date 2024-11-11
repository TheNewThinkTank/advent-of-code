
import numpy as np
# from pprint import pprint as pp
import string
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore

datafiles = [
    "input.txt",
    "sample.txt",
    ]
datafile = get_full_path("2022", "day_12", datafiles[1])
lines = get_data(datafile)


def make_grid():
    grid = []
    for row in lines:
        row_heights = []
        for height in row:
            row_heights.append(height)
        grid.append(row_heights)
    return np.array(grid)


def update_grid(grid):
    height_values = {letter: i + 1 for i, letter in enumerate(string.ascii_lowercase)}
    start_and_end_values = {"S": 1, "E": 26}
    elevation = height_values | start_and_end_values
    height_map = np.zeros(grid.shape).astype("int")
    for idx, height in np.ndenumerate(grid):
        x, y = idx
        height_map[x, y] = elevation[height]
    return height_map


grid = make_grid()
# print(grid)
height_map = update_grid(grid)
print(height_map)

# rows, cols = grid.shape[0], grid.shape[1]
start_position = np.argwhere(grid == "S").flatten()
best_signal = np.argwhere(grid == "E").flatten()
print(start_position, best_signal)

x, y = start_position
# print(height_map[x, y])
# print(height_map[best_signal[0], best_signal[1]])
# print(height_map[x, y:].shape[0])

has_space_right = height_map[x, y:].shape[0] > 1
if has_space_right:
    can_go_right = height_map[x, y] + 1 >= height_map[x, y + 1]
    if can_go_right:
        print(f"{height_map[x, y]} can go to: {height_map[x, y+1]}")


"""
for idx, height in np.ndenumerate(height_map):
    x, y = idx

    has_space_right = height_map[x, y:].shape[0] > 1
    if has_space_right:
        can_go_right = height_map[x, y] >= height_map[x, y + 1] + 1
        if can_go_right:
            print(f"{height_map[x, y]} can go to: {height_map[x, y+1]}")

    # can_go_left = height_map[x, y] >= height_map[x, y - 1] + 1
    # can_go_up = height_map[x, y] >= height_map[x - 1, y] + 1
    # can_go_down = height_map[x, y] >= height_map[x + 1, y] + 1
"""
