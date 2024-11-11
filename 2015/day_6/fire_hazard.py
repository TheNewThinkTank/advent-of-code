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
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore


def get_action_and_coords(test):

    pattern = r"^(turn on|turn off|toggle)\s(\d*,\d*)\sthrough\s(\d*,\d*)$"
    regex = re.compile(pattern)
    m = re.search(regex, test)
    action, start_coords, end_coords = m.groups()
    start_coords = tuple(int(i) for i in start_coords.split(","))
    end_coords = tuple(int(i) for i in end_coords.split(","))

    return action, start_coords, end_coords


def get_new_value(action, value) -> int:

    action_map = {
        "turn on": 1,
        "turn off": 0,
        "toggle": np.logical_not(value).astype(
            int
        ),
    }

    return action_map[action]


def update_grid(action, start_coords, end_coords) -> None:

    grid[
        start_coords[0] : end_coords[0] + 1, start_coords[1] : end_coords[1] + 1
    ] = get_new_value(
        action,
        grid[start_coords[0] : end_coords[0] + 1, start_coords[1] : end_coords[1] + 1],
    )


# tests = [
#     "turn on 0,0 through 999,999",
#     "toggle 0,0 through 999,0",
#     "turn off 499,499 through 500,500",
# ]
# test = tests[0]

datafile = get_full_path("2015", "day_6", "input.txt")
tests = get_data(datafile)

# ic(tests)
grid = np.zeros((1_000, 1_000))  # , dtype=np.bool_)
action_map = {
    "turn on": 1,
    "turn off": -1,
    "toggle": 2
}
for test in tests:
    action, start_coords, end_coords = get_action_and_coords(test)
    # ic(action)
    # ic(start_coords)
    # ic(end_coords)

    # part 1
    # update_grid(action, start_coords, end_coords)

    # part 2
    grid[
        start_coords[0] : end_coords[0] + 1,
        start_coords[1] : end_coords[1] + 1
        ] += action_map[action]
    grid[grid < 0] = 0

ic(grid)
lights_on = int(np.sum(grid))
ic(lights_on)
