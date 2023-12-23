# operational .
# damaged #
# unknown ?

from pprint import pprint as pp

# from tqdm import tqdm
from icecream import ic

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]

datafile = datafiles[1]

with open(datafile, "r") as rf:
    lines = rf.readlines()

lines = [line.removesuffix("\n") for line in lines]
# pp(lines)

springs_and_groups_rows = []
for line in lines:
    line = line.split(" ")
    springs_and_groups_rows.append((line[0], line[1]))
# ic(springs_and_groups_rows)

springs_and_groups = springs_and_groups_rows[0]
ic(springs_and_groups)
