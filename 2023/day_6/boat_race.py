
# import itertools
# from functools import reduce
# from operator import mul
# from pprint import pprint as pp
# from tqdm import tqdm
from icecream import ic
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.get_data import get_data  # type: ignore

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]

datafile = datafiles[0]

lines = get_data(datafile)

# part 1


def parse_line_data(line):
    return [int(i) for i in line.split(":")[1].split() if i]


time = parse_line_data(lines[0])
distance = parse_line_data(lines[1])


# ic(time)
# ic(distance)


def get_distance(holding_time, total_time):
    remaining_time = total_time - holding_time
    return holding_time * remaining_time


# part 1
# margin_of_error = []
# for t, d in zip(time, distance):
#     ways_to_win = 0
#     # ic(t, d)
#     for holding_time in range(1, t-1):
#         d_ = get_distance(holding_time, t)
#         if d_ > d:
#             ways_to_win += 1
#     margin_of_error.append(ways_to_win)
# # pp(margin_of_error)
# ic(reduce(mul, margin_of_error, 1))

# part 2:
time = int("".join([str(t) for t in time]))
distance = int("".join([str(d) for d in distance]))

ic(time)
ic(distance)

ways_to_win = 0
for holding_time in range(1, time-1):
    d_ = get_distance(holding_time, time)
    if d_ > distance:
        ways_to_win += 1
ic(ways_to_win)
