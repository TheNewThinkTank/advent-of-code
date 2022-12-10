import numpy as np

datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[1]

with open(datafile, "r") as rf:
    lines = rf.readlines()

lines = [line.removesuffix("\n") for line in lines]

grid = np.array([[""]])


def update_grid(grid, direction, num):
    rows, cols = grid.shape
    if direction in ("R", "L"):
        grid = np.resize(grid, (rows, cols + num))
    else:
        grid = np.resize(grid, (rows + num, cols))
    return grid


direction, num = "R", 4
grid = update_grid(grid, direction, num)
# print(grid)

# U 4
direction, num = "U", 4
grid = update_grid(grid, direction, num)
print(grid)

# L 3


# D 1

# L 5

# for line in lines:
#     direction, num = line.split()
#     num = int(num)
#     print(direction)
#     print(num)
