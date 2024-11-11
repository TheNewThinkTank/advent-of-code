"""
operational .
damaged #
unknown ?
"""

# from pprint import pprint as pp
# from tqdm import tqdm
from icecream import ic
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]
datafile = get_full_path("2023", "day_12", datafiles[1])
lines = get_data(datafile)
# pp(lines)


def get_springs_and_groups_rows():
    springs_and_groups_rows = []
    for line in lines:
        line = line.split(" ")

        springs_and_groups_rows.append((
            line[0],
            [int(i) for i in line[1].split(",")])
            )

    return springs_and_groups_rows


springs_and_groups_rows = get_springs_and_groups_rows()
springs_and_groups = springs_and_groups_rows[0]
springs = springs_and_groups[0]
groups = springs_and_groups[1]
ic(springs)
ic(groups)


def reveal_springs(springs, groups):
    ...


test = {
    'input': { 
        'springs': '???.###', 
        'groups': [1, 1, 3]
    },
    'output': '#.#.###'
}

assert reveal_springs(**test['input']) == test['output']
