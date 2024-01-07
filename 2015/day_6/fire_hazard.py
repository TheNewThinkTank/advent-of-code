"""
turn on 0,0 through 999,999
would turn on (or leave on) every light.

toggle 0,0 through 999,0
would toggle the first line of 1000 lights, turning off the ones that were on,
and turning on the ones that were off.

turn off 499,499 through 500,500
would turn off (or leave off) the middle four lights
"""

import numpy as np
import re

from icecream import ic


def get_action_and_coords(test):
    pattern = r"^(turn on|turn off|toggle)\s(\d*,\d*)\sthrough\s(\d*,\d*)$"
    regex = re.compile(pattern)
    m = re.search(regex, test)
    action, start_coords, end_coords = m.groups()
    start_coords = tuple(int(i) for i in start_coords.split(","))
    end_coords = tuple(int(i) for i in end_coords.split(","))
    return action, start_coords, end_coords


def get_new_value(action, value) -> int:
    # def toggle(value) -> int:
    #     return 0 if value else 1
    action_map = {
        "turn on": 1,
        "turn off": 0,
        "toggle": np.logical_not(value).astype(int)  # 0 if value else 1  # toggle(value),
    }
    return action_map[action]


grid = np.zeros((1_000, 1_000))

test = "turn on 0,0 through 999,999"
# test = "toggle 0,0 through 999,0"
# test = "turn off 499,499 through 500,500"

action, start_coords, end_coords = get_action_and_coords(test)

# ic(action)
# ic(start_coords)
# ic(end_coords)

# sub_grid = [start_coords[0]:end_coords[0], start_coords[1]:end_coords[1]]
# sub_grid = np.ndarray(start_coords, end_coords)

# grid[start_coords] = get_new_value(action, grid[start_coords])
grid[start_coords[0]:end_coords[0],
     start_coords[1]:end_coords[1]] = get_new_value(action,
                                                    grid[start_coords[0]:end_coords[0],
                                                         start_coords[1]:end_coords[1]
                                                         ]
                                                    )

# np.put(grid,
#        [start_coords[0]:end_coords[0], start_coords[1]:end_coords[1]],
#        [-44, -55]
#        )

# ic(grid[0:5, 0:5])
# ic(grid[start_coords[0]:end_coords[0], start_coords[1]:end_coords[1]])
ic(grid)
