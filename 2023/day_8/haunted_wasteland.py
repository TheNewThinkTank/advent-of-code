from pprint import pprint as pp

# from tqdm import tqdm
from icecream import ic

datafiles = [
    "input.txt",
    "input_sample_1.txt",
    "input_sample_2.txt",
    ]

datafile = datafiles[1]

with open(datafile, "r") as rf:
    lines = rf.readlines()
lines = [line.removesuffix("\n") for line in lines]
lines = [line for line in lines if line]
left_right_instructions = lines[0]
elements = lines[1:]

# pp(left_right_instructions)
# for element in elements:
#     eval(element)
# pp(elements)

first = elements[0].partition(" = ")

first_node = first[0]
ic(first_node)

first_lr = first[2].strip("()").split(", ")
ic(first_lr)

# for instruction in left_right_instructions:
#     ic(instruction)
