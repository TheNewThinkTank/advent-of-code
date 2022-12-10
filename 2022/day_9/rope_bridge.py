import numpy as np

datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[1]

with open(datafile, "r") as rf:
    lines = rf.readlines()

lines = [line.removesuffix("\n") for line in lines]

grid = np.array([["H"]])


def move_h(grid, direction, num):
    rows, cols = grid.shape
    h_pos = np.argwhere(grid == "H").flatten()
    assert h_pos.size > 0
    h_y, h_x = h_pos[0], h_pos[1]
    grid[h_y, h_x] = ""

    if direction == "R":
        # print(f"{grid[h_y, h_x:].shape[0] = }")
        free_space = grid[h_y, h_x + 1 :].shape[0]
        if free_space < num:
            missing = num - free_space
            grid = np.resize(grid, (rows, cols + missing))
        h_x += num
    if direction == "L":
        free_space = grid[h_y, :h_x].shape[0]
        if free_space < num:
            missing = num - free_space
            grid = np.resize(grid, (rows, cols + missing))
        h_x -= num
    if direction == "U":
        free_space = grid[:h_y, h_x].shape[0]
        if free_space < num:
            missing = num - free_space
            grid = np.resize(grid, (rows + missing, cols))
    if direction == "D":
        free_space = grid[h_y + 1 :, h_x].shape[0]
        if free_space < num:
            missing = num - free_space
            grid = np.resize(grid, (rows + missing, cols))
        h_y += num

    grid[h_y, h_x] = "H"
    # print(grid)
    return grid


"""
# R4, U4, L3, D1, R4, D1, L5, R2
direction, num = "R", 4
grid = move_h(grid, direction, num)
direction, num = "U", 4
grid = move_h(grid, direction, num)
direction, num = "L", 3
grid = move_h(grid, direction, num)
direction, num = "D", 1
grid = move_h(grid, direction, num)
direction, num = "R", 4
grid = move_h(grid, direction, num)
direction, num = "D", 1
grid = move_h(grid, direction, num)
direction, num = "L", 5
grid = move_h(grid, direction, num)
direction, num = "R", 2
grid = move_h(grid, direction, num)
"""

# print(grid)
# t_pos = np.argwhere(grid == "T").flatten()

for line in lines:
    direction, num = line.split()
    num = int(num)
    grid = move_h(grid, direction, num)
print(grid)
