
# import itertools
# from functools import reduce
# from operator import mul
# from pprint import pprint as pp
# from tqdm import tqdm
from icecream import ic

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]

datafile = datafiles[0]

with open(datafile, "r") as rf:
    lines = rf.readlines()
lines = [line.removesuffix("\n") for line in lines]

# part 1
time = [int(i) for i in lines[0].split(":")[1].split(" ") if i]
distance = [int(i) for i in lines[1].split(":")[1].split(" ") if i]

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
