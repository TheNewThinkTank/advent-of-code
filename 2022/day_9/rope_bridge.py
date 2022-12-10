import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[1]
with open(datafile, "r") as rf:
    lines = rf.readlines()
lines = [line.removesuffix("\n") for line in lines]
grid = np.array([["HT"]])


def get_h_and_t_pos(grid):
    h_pos = np.argwhere((grid == "H") | (grid == "HT")).flatten()
    assert h_pos.size > 0
    h_y, h_x = h_pos[0], h_pos[1]
    grid[h_y, h_x] = ""
    t_pos = np.argwhere((grid == "T") | (grid == "HT")).flatten()
    if t_pos.size == 0:
        grid[0, 0] = "T"
        t_pos = np.argwhere((grid == "T") | (grid == "HT")).flatten()
    t_y, t_x = t_pos[0], t_pos[1]
    grid[t_y, t_x] = ""
    return h_x, h_y, t_x, t_y


def move_h_and_t(grid, direction, num):

    h_x, h_y, t_x, t_y = get_h_and_t_pos(grid)

    rows, cols = grid.shape

    if direction == "R":
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
    grid[t_y, t_x] = "T"

    return grid


# R4, U4, L3, D1, R4, D1, L5, R2
direction, num = "R", 4
grid = move_h_and_t(grid, direction, num)
direction, num = "U", 4
grid = move_h_and_t(grid, direction, num)
# direction, num = "L", 3
# grid = move_h_and_t(grid, direction, num)
# direction, num = "D", 1
# grid = move_h_and_t(grid, direction, num)
# direction, num = "R", 4
# grid = move_h_and_t(grid, direction, num)
# direction, num = "D", 1
# grid = move_h_and_t(grid, direction, num)
# direction, num = "L", 5
# grid = move_h_and_t(grid, direction, num)
# direction, num = "R", 2
# grid = move_h_and_t(grid, direction, num)

print(grid)

# for line in lines:
#     direction, num = line.split()
#     num = int(num)
#     grid = move_h_and_t(grid, direction, num)
# print(grid)
