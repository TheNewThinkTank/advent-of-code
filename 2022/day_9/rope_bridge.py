
import numpy as np
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore

np.set_printoptions(threshold=sys.maxsize)

datafiles = ["input.txt", "sample.txt"]
datafile = get_full_path("2022", "day_9", datafiles[1])
lines = get_data(datafile)

grid = np.array([["HT"]])


def get_positions(grid):
    """Retrieve positions of 'H' and 'T' on the grid, clearing those cells after."""
    h_pos = np.argwhere((grid == "H") | (grid == "HT")).flatten()
    assert h_pos.size > 0, "No 'H' found on the grid"
    h_y, h_x = h_pos

    # Clear 'H' from current cell
    grid[h_y, h_x] = ""

    t_pos = np.argwhere((grid == "T") | (grid == "HT")).flatten()
    if t_pos.size == 0:
        # Set initial 'T' position if not present
        grid[0, 0] = "T"
        t_pos = np.argwhere((grid == "T") | (grid == "HT")).flatten()
    t_y, t_x = t_pos

    # Clear 'T' from current cell
    grid[t_y, t_x] = ""
    return h_x, h_y, t_x, t_y


def resize_grid(grid, target_x, target_y):
    """Resize the grid to ensure it can fit target coordinates."""
    rows, cols = grid.shape
    new_rows = max(rows, target_y + 1)
    new_cols = max(cols, target_x + 1)

    if new_rows > rows or new_cols > cols:
        new_grid = np.full((new_rows, new_cols), "", dtype=grid.dtype)
        new_grid[:rows, :cols] = grid
        return new_grid
    return grid


def move_h_and_t(grid, direction, num):
    """Move 'H' and 'T' in the specified direction and number of steps."""
    h_x, h_y, t_x, t_y = get_positions(grid)

    # Define movement offsets for each direction
    movement_offsets = {"R": (num, 0), "L": (-num, 0), "U": (0, -num), "D": (0, num)}
    offset_x, offset_y = movement_offsets[direction]

    # Update H position with bounds check
    new_h_x, new_h_y = h_x + offset_x, h_y + offset_y
    grid = resize_grid(grid, new_h_x, new_h_y)

    # Update grid with new 'H' and 'T' positions
    grid[new_h_y, new_h_x] = "H"
    grid[t_y, t_x] = "T"

    return grid


# Example usage: R4, U4, L3, D1, R4, D1, L5, R2
directions = [
    ("R", 4),
    ("U", 4),
    ("L", 3),
    ("D", 1),
    ("R", 4),
    ("D", 1),
    ("L", 5),
    ("R", 2),
    ]
for direction, num in directions:
    grid = move_h_and_t(grid, direction, num)

print(grid)

# for line in lines:
#     direction, num = line.split()
#     num = int(num)
#     grid = move_h_and_t(grid, direction, num)
# print(grid)
