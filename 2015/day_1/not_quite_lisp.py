"""
(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3
"""

from collections import Counter
# from icecream import ic
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_full_path import get_full_path  # type: ignore

datafiles = [
    "input.txt",
    ]
datafile = get_full_path("2015", "day_1", datafiles[0])


def get_data():
    with open(datafile, "r") as f:
        data = f.read()
    return data  # .split("\n\n")


data = get_data()
counts = Counter(data)

# puzzle 1
# up = counts['(']
# down = counts[')']
# final_floor = up - down
# ic(final_floor)

# puzzle 2
map = {'(': 1, ')': -1}

floor = 0
for idx, char in enumerate(data):
    floor += map[char]
    if floor == -1:
        print(idx + 1)
        break
