from pprint import pprint as pp
import numpy as np

datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[0]

with open(datafile, "r") as rf:
    lines = rf.readlines()

lines = [line.removesuffix("\n") for line in lines]


def make_grid():
    grid = []
    for row in lines:
        row_trees = []
        for tree in row:
            row_trees.append(int(tree))
        grid.append(row_trees)
    return np.array(grid)


grid = make_grid()
rows, cols = grid.shape[0], grid.shape[1]
assert rows == cols
pp(grid)
# print(grid.shape)

inner_grid = grid[1 : rows - 1, 1 : cols - 1]
# print(inner_grid)
assert inner_grid.shape[0] == inner_grid.shape[1]

num_edge_trees = 2 * rows + 2 * (cols - 2)
# print(num_edge_trees)

num_inner_trees = 0

for idx, tree in np.ndenumerate(inner_grid):
    x, y = idx
    k, l = x + 1, y + 1

    left_visible = all(tree > z for z in grid[k, :l])
    right_visible = all(tree > z for z in grid[k, l + 1 :])
    top_visible = all(tree > z for z in grid[:k, l])
    bottom_visible = all(tree > z for z in grid[k + 1 :, l])

    if left_visible or right_visible or top_visible or bottom_visible:
        # print(x, y, tree)
        num_inner_trees += 1

print(num_edge_trees + num_inner_trees)
