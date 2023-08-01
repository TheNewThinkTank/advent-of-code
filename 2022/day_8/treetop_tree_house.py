# from pprint import pprint as pp
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
# pp(grid)
inner_grid = grid[1 : rows - 1, 1 : cols - 1]
assert inner_grid.shape[0] == inner_grid.shape[1]
num_edge_trees = 2 * rows + 2 * (cols - 2)

num_inner_trees = 0
scenic_scores = []


def part_2():
    left_view = 0
    right_view = 0
    top_view = 0
    bottom_view = 0

    for z in grid[inner_x, :inner_y][::-1]:
        left_view += 1
        if tree <= z:
            break

    for z in grid[inner_x, inner_y + 1 :]:
        right_view += 1
        if tree <= z:
            break

    for z in grid[:inner_x, inner_y][::-1]:
        top_view += 1
        if tree <= z:
            break

    for z in grid[inner_x + 1 :, inner_y]:
        bottom_view += 1
        if tree <= z:
            break

    scenic_score = left_view * right_view * top_view * bottom_view
    scenic_scores.append(scenic_score)


for idx, tree in np.ndenumerate(inner_grid):
    x, y = idx
    inner_x, inner_y = x + 1, y + 1

    # part 1
    left_visible = all(tree > z for z in grid[inner_x, :inner_y])
    right_visible = all(tree > z for z in grid[inner_x, inner_y + 1 :])
    top_visible = all(tree > z for z in grid[:inner_x, inner_y])
    bottom_visible = all(tree > z for z in grid[inner_x + 1 :, inner_y])
    if left_visible or right_visible or top_visible or bottom_visible:
        num_inner_trees += 1

    part_2()


# part 1
print(num_edge_trees + num_inner_trees)

# part 2
print(max(scenic_scores))
