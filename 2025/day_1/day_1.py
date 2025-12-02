
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore
# import numpy as np

datafiles = [
    "input.txt",
    ]
datafile = get_full_path("2025", "day_1", datafiles[0])
data = get_data(datafile)
# print(data)

dial = 50  # start position
MAX = 100  # number of positions: 0..99


def parse_instructions(input_str):
    """
    Parse the puzzle input into a list of (direction, distance) tuples.
    """
    instructions = []
    for line in input_str:  # input_str.strip().splitlines():
        parts = line[0], line[1:]  # line.split()
        if not parts:
            continue
        # print(parts)  # e.g. parts = ['R', '48']
        direction = parts[0]
        # convert distance to integer (or float, as needed)
        distance = int(parts[1])
        instructions.append((direction, distance))
    return instructions


def rotate(dial: int, direction: str, clicks: int) -> int:
    """
    Return the new dial position after rotating 'clicks' steps in 'direction' ('L' or 'R').
    """
    if direction == 'R':
        dial = (dial + clicks) % MAX
    else:  # assume direction 'L'
        dial = (dial - clicks) % MAX
    return dial


# dial = rotate(dial, 'R', 48)

input_str = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

# instructions = parse_instructions(input_str)
instructions = parse_instructions(data)

zeros = 0
for direction, distance in instructions:
    dial = rotate(dial, direction, distance)
    if dial == 0:
        zeros += 1
    # print(f"The dial is rotated {direction}{distance} to point at {dial}.")

print(f"The dial pointed at 0 a total of {zeros} times.")
