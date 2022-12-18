import numpy as np
from pprint import pprint as pp
import string

datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[1]

with open(datafile, "r") as rf:
    lines = rf.readlines()
lines = [line.removesuffix("\n") for line in lines]


def make_grid():
    grid = []
    for row in lines:
        row_heights = []
        for height in row:
            row_heights.append(height)
        grid.append(row_heights)
    return np.array(grid)


grid = make_grid()
print(grid)

# rows, cols = grid.shape[0], grid.shape[1]
start_position = np.argwhere(grid == "S").flatten()
best_signal = np.argwhere(grid == "E").flatten()
# print(start_position, best_signal)

height_values = {letter: i + 1 for i, letter in enumerate(string.ascii_lowercase)}
start_and_end_values = {"S": 1, "E": 26}
elevation = height_values | start_and_end_values
# pp(elevation)

for idx, height in np.ndenumerate(grid):
    x, y = idx
    # print(x, y, height, elevation[height], grid[x, y])
    grid[x, y] = elevation[height]

print(grid)
