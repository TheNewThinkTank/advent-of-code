# operational .
# damaged #
# unknown ?

# from pprint import pprint as pp

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


def get_springs_and_groups_rows():
    springs_and_groups_rows = []
    for line in lines:
        line = line.split(" ")

        springs_and_groups_rows.append((
            line[0],
            [int(i) for i in line[1].split(",")])
            )
        # springs_and_groups_rows.append((line[0], line[1]))

    return springs_and_groups_rows


springs_and_groups_rows = get_springs_and_groups_rows()
springs_and_groups = springs_and_groups_rows[0]
springs = springs_and_groups[0]
groups = springs_and_groups[1]
ic(springs)
ic(groups)


